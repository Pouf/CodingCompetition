import sys

def main():
    while True:
        IN = sys.stdin.readline()
        if not IN or IN.strip() == '42':
            break
        sys.stdout.write(IN)
        sys.stdout.flush()

if __name__ == "__main__":
    main()
