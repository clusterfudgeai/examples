import clusterfudge


def main():
    workload = 'import os, time; replica_index = os.environ.get("CLUSTERFUDGE_REPLICA_INDEX"); print(f"Hello from REPLICA={replica_index}"); time.sleep(60)'

    client = clusterfudge.Client()
    launch = client.create_launch(
        clusterfudge.CreateLaunchRequest(
            name="hello-world-example",
            description="Sleep 60 on 2 replicas with 1 CPU each.",
            # jobs is a list of jobs that are scheduled together
            # i.e. gang-scheduled.
            jobs=[
                clusterfudge.Job(
                    # short_name must be unique within the same launch.
                    # It is used to identify the job in the dashboard.
                    short_name="hello_world",
                    # replicas=2 requests two copies of this job. The requested
                    # processes may run on the same or different machines.
                    replicas=2,
                    # processes is a list of processes that run concurrently on
                    # a single machine. There can be any number of processes
                    # per job.
                    processes=[
                        clusterfudge.Process(
                            command=["python3", "-c", workload],
                            # resource_requirements specifies the resources
                            # required for this process.
                            # This can be empty, in which case the workload
                            # can be scheduled on any machine.
                            resource_requirements=clusterfudge.Resources(
                                # cpus=1 requests 1 CPU.
                                # other resources we currently support are:
                                # - a100_40gb
                                # - a100_80gb
                                # - h100
                                # - rtx3090
                                # - t4
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
