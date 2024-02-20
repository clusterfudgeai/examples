from clusterfudge import FudgeClient, launches_pb2


def main():
    cf = FudgeClient()
    launch = cf.create_launch(
        launches_pb2.CreateLaunchRequest(
            command=["python3", "-c", "print('Hello, from Clusterfudge!')"],
            hostnames=["examplehost001"],
        )
    )

    print(f"Launched: launch/{launch.launch_id} 🎉")
    print(f"https://clusterfudge.clusterfudge.com/dashboard/launches/")


if __name__ == "__main__":
    main()
