#!/bin/bash

# Function to kill all child processes
cleanup() {
    echo "Terminating all child processes"
    pkill -P $$
}

# Trap SIGINT (Ctrl+C) and SIGTERM (default kill signal)
trap cleanup SIGINT SIGTERM

for i in {1..8}
do
  python3 hello_zip.py &
done

echo "waiting for all processes to finish"

wait

echo "all done"
