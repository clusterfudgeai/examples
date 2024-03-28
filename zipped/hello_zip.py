import os
import time


def main():
    print(f"Hello, world! {time.time()} {os.environ.get('CLUSTERFUDGE_TASK_ID')}")
    time.sleep(10)
    print(f"Goodbye! {time.time()}{os.environ.get('CLUSTERFUDGE_TASK_ID')}")


if __name__ == "__main__":
    main()
