import clusterfudge


def main():
    workload = 'import os, time; replica_index = os.environ.get("CLUSTERFUDGE_REPLICA_INDEX"); print(f"Hello from REPLICA={replica_index}"); time.sleep(60)'

    client = clusterfudge.Client()
    launch = client.create_launch(
        clusterfudge.CreateLaunchRequest(
            name="hello-world-example",
            description="Sleep 60 on 2 replicas with 1 CPU each.",
            jobs=[
                clusterfudge.Job(
                    short_name="hello_world",
                    replicas=2,
                    processes=[
                        clusterfudge.Process(
                            command=["python3", "-c", workload],
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
    print("https://clusterfudge.clusterfudge.com/dashboard/launches/")


if __name__ == "__main__":
    main()
