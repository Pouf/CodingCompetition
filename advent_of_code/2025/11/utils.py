from __future__ import annotations
import logging
import re
import sys
from pathlib import Path
from itertools import zip_longest
from typing import Iterator


LOGGER = logging.getLogger(__name__)


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format_string = "%(asctime)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format_string + reset,
        logging.INFO: green + format_string + reset,
        logging.WARNING: yellow + format_string + reset,
        logging.ERROR: red + format_string + reset,
        logging.CRITICAL: bold_red + format_string + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup(func):
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(CustomFormatter())
    logging.basicConfig(
        level=logging.DEBUG, handlers=[console_handler], datefmt="%H:%M:%S"
    )
    test_numbers = get_test_numbers()
    for test_number in test_numbers:
        LOGGER.debug(f"Running test number {test_number}...")
        test_input = get_test("input", test_number)
        test_output = get_test("output", test_number)
        my_result = write_result(test_number, test_input, func)
        if test_output:
            LOGGER.debug("Test output found, checking results...")
            check_result(test_output, my_result)
        else:
            LOGGER.debug("No test output found.")


def get_test_numbers() -> list[int]:
    input_files = get_test_files()
    suffixes = list(map(get_files_suffix, input_files))
    if not suffixes:
        LOGGER.debug("No input files found.")
        sys.exit()
    input_file_suffix = input(
        f"which test do you want to run ? Options are {suffixes}. Leave empty to run all tests\n"
    )
    if not input_file_suffix:
        return [int(suffix) for suffix in suffixes]
    if input_file_suffix not in suffixes:
        LOGGER.warning(f"Input file with suffix '{input_file_suffix}' not found.")
        sys.exit()
    return [int(input_file_suffix)]


def get_test_files() -> list[Path]:
    this_dir = Path(__file__).parent
    input_files = this_dir.glob("input*.txt")
    return list(input_files)


def get_files_suffix(files: Path) -> str:
    name = files.stem
    suffix_match = re.search(r"\d+", name)
    if suffix_match:
        return suffix_match[0]
    return ""


def get_test(file_type: str, test_number: int) -> Iterator[str]:
    this_dir = Path(__file__).parent
    file_path = this_dir / f"{file_type}{test_number}.txt"
    if file_path.is_file():
        yield from get_file_contents(file_path)
    else:
        yield from ()


def get_file_contents(file_path: Path) -> Iterator[str]:
    with file_path.open("r", encoding="utf-8") as f:
        for line in f.readlines():
            yield line.strip()


def write_result(test_number: int, test_input: Iterator[str], func) -> list[str]:
    this_dir = Path(__file__).parent
    result_file_path = this_dir / f"my_result{test_number}.txt"
    result = [str(line).strip() for line in func(test_input)]
    with result_file_path.open("w", encoding="utf-8") as result_file:
        result_file.write("\n".join(result))
    LOGGER.debug(f"Result written in {result_file_path}")
    return result


def check_result(test_output: Iterator[str], actual_output: list[str]) -> bool:
    errors = []
    for line, (expected_output, my_output) in enumerate(
        zip_longest(test_output, actual_output, fillvalue=""), 1
    ):
        if expected_output != my_output:
            errors.append((line, expected_output, my_output))
    if errors:
        LOGGER.error("Test failed.")
        for line, expected_output, my_output in errors:
            LOGGER.warning(
                f"Line {line + 1}: expected `{expected_output}`, got `{my_output}`"
            )
        return False
    LOGGER.info("Success!")
    return True