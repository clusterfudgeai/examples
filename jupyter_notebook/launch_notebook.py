import clusterfudge


def main():
    client = clusterfudge.Client()
    launch = client.create_launch(
        clusterfudge.CreateLaunchRequest(
            name="jupyter notebook",
            description="Running a notebook",
            jobs=[
                clusterfudge.Job(
                    short_name="jupyter",
                    replicas=1,
                    processes=[
                        clusterfudge.Process(
                            command=[
                                "/home/clusterfudge/.local/bin/jupyter",
                                "notebook",
                            ],
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
    print(f"https://clusterfudge.clusterfudge.com/dashboard/launches/")


if __name__ == "__main__":
    main()
