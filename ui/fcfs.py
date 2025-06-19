# fcfs.py

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

class FCFS:
    def __init__(self, processes):
        self.processes = [Process(*p) for p in processes]  # p = (pid, arrival, burst)

    def run(self):
        # Sort processes by arrival time
        self.processes.sort(key=lambda x: x.arrival_time)
        current_time = 0

        for process in self.processes:
            if current_time < process.arrival_time:
                current_time = process.arrival_time

            process.completion_time = current_time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            current_time = process.completion_time

        return self.get_result()

    def get_result(self):
        # Return results as list of dicts
        return [
            {
                "PID": p.pid,
                "Arrival Time": p.arrival_time,
                "Burst Time": p.burst_time,
                "Completion Time": p.completion_time,
                "Turnaround Time": p.turnaround_time,
                "Waiting Time": p.waiting_time
            }
            for p in self.processes
        ]

