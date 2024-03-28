import clusterfudge

_FILE_NAME = "checkout_and_run.sh"


def _get_bash_script() -> str:
    with open(_FILE_NAME, "r") as file:
        return file.read()


def main():
    bash_contents = _get_bash_script()

    client = clusterfudge.Client()

    launch = client.create_launch(
        clusterfudge.CreateLaunchRequest(
            name="hello-world-example",
            description="Just testing out clusterfudge! 🎉",
            jobs=[
                clusterfudge.Job(
                    short_name="bash",
                    replicas=1,
                    processes=[
                        clusterfudge.Process(
                            command=[
                                "/bin/bash",
                                "-c",
                                bash_contents,
                            ],
                            resource_requirements=clusterfudge.Resources(
                                cpus=1,
                            ),
                        ),
                    ],
                ),
            ],
        )
    )
    print(f"Launched: launch/{launch.launch_id} 🎉")
    print(f"https://clusterfudge.clusterfudge.com/dashboard/launches/")


if __name__ == "__main__":
    main()
