import clusterfudge


def main():
    client = clusterfudge.Client()
    launch = client.create_launch(
        clusterfudge.CreateLaunchRequest(
            name="zip example",
            description="Clusterfudge example of zipping a local directory and running it on a remote machine",
            # LocalDir finds the root of this project, by walking up the directory tree until it finds a
            # .git folder, pyproject.toml or "requirements.txt" file.
            # It then zips the contents of the directory and sends it, via Clusterfudge, to the remote machine.
            # The folder is reuploaded every time the launch is created.
            deployment=clusterfudge.LocalDir(),
            jobs=[
                clusterfudge.Job(
                    short_name="zip",
                    replicas=1,
                    processes=[
                        clusterfudge.Process(
                            command=["python3","hello_zip.py"],
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
