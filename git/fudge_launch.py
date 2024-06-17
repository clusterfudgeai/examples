import clusterfudge


def main():
    client = clusterfudge.Client()
    launch = client.create_launch(
        clusterfudge.CreateLaunchRequest(
            name="git example",
            description="Example showing how we can clone git repos",
            deployment=clusterfudge.GitRepo(
                repo="https://github.com/clusterfudgeai/examples",
                branch="main",
            ),
            jobs=[
                clusterfudge.Job(
                    short_name="git",
                    replicas=1,
                    processes=[
                        clusterfudge.Process(
                            command=[
                                "python3",
                                "git/hello_git.py",
                            ],
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
