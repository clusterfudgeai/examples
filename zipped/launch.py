import clusterfudge


def main():
    client = clusterfudge.Client()
    launch = client.create_launch(
        clusterfudge.CreateLaunchRequest(
            name="zip example",
            description="Example showing how we can zip our current directory, ship it to the node and run the files from it",
            # deployment=clusterfudge.LocalDir(),
            jobs=[
                clusterfudge.Job(
                    short_name="bash",
                    replicas=2,
                    processes=[
                        clusterfudge.Process(
                            command=["/bin/bash", "-c", "echo", "Hello from Bash!"],
                        ),
                    ],
                ),
                clusterfudge.Job(
                    short_name="python",
                    replicas=1,
                    processes=[
                        clusterfudge.Process(
                            command=["python3", "-c", "print('Hello from Python!')"],
                            resource_requirements=clusterfudge.Resources(
                                rtx3090=1,
                            ),
                        ),
                    ],
                ),
            ],
        )
    )

    print(f"Launched: launch/{launch.launch_id} 🎉")
    print("https://clusterfudge.clusterfudge.com/dashboard/launches")


if __name__ == "__main__":
    main()
