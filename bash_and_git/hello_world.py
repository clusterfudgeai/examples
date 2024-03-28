import os


def main():
    task_id = os.environ.get("CLUSTERFUDGE_TASK_ID")
    print(f"Hello from TASK_ID={task_id}")


if __name__ == "__main__":
    main()
