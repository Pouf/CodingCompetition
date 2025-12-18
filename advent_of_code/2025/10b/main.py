import re
import numpy as np
from collections import deque
from typing import Iterator, Any
from utils import setup


def main(test_input: Iterator[str]) -> Iterator[Any]:
    result = 0
    for line in test_input:
        _, *raw_buttons, raw_requirement = line.split()
        requirement: np.ndarray = np.array(
            [int(x) for x in re.findall(r"\d+", raw_requirement)]
        )
        print(f"==>> requirement: {requirement}")
        nb_counters: int = len(requirement)
        buttons: list[np.ndarray] = []
        for raw_button in raw_buttons:
            positions: list[int] = [int(x) for x in re.findall(r"\d+", raw_button)]
            button: np.ndarray = np.array([1 if x in positions else 0 for x in range(nb_counters)])
            buttons.append(button)
        buttons.sort(key=sum, reverse=True)
        print(f"==>> buttons: {buttons}")
        result += match_requirement(
            requirement,
            buttons,
        )
    yield result


def match_requirement(requirement: np.ndarray, buttons: list[np.ndarray]) -> int:
    if not requirement.any():
        return 0
    visited = set([tuple(requirement)])
    stack = deque([(requirement, 0)])
    while True:
        print(f"==>> stack: {stack}")
        state, buttons_pressed = stack.popleft()
        print(f"==>> state: {state}")
        by_value, by_value_index = np.unique(state, return_index=True)
        highest_value_index = by_value_index[-1]
        print(f"==>> highest_value_index: {highest_value_index}")
        highest_value = by_value[-1]
        print(f"==>> highest_value: {highest_value}")
        second_highest_value = by_value[-2] if len(by_value) > 1 else 0
        print(f"==>> second_highest_value: {second_highest_value}")
        nb_presses = int(highest_value - second_highest_value)
        print(f"==>> nb_presses: {nb_presses}")
        for button in buttons:
            if button[highest_value_index] == 0:
                continue
            print(f"==>> button: {button}")
            new_state = state - button * nb_presses
            print(f"==>> new_state: {new_state}")
            if not np.any(new_state < 0) and tuple(new_state) not in visited:
                new_buttons_pressed = buttons_pressed + nb_presses
                if not new_state.any():
                    return new_buttons_pressed
                stack.append((new_state, new_buttons_pressed))
                visited.add(tuple(new_state))


if __name__ == "__main__":
    setup(main)
