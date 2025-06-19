# srtf.py

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.is_completed = False

class SRTF:
    def __init__(self, process_list):
        self.processes = [Process(*p) for p in process_list]

    def run(self):
        time = 0
        completed = 0
        n = len(self.processes)
        result = []

        while completed < n:
            # Get ready processes
            ready = [p for p in self.processes if p.arrival_time <= time and not p.is_completed]
            
            if not ready:
                time += 1
                continue

            # Pick the process with shortest remaining time
            current = min(ready, key=lambda p: p.remaining_time)

            # First time it's running
            if current.start_time is None:
                current.start_time = time

            # Run for 1 unit time
            current.remaining_time -= 1
            time += 1

            if current.remaining_time == 0:
                current.completion_time = time
                current.turnaround_time = current.completion_time - current.arrival_time
                current.waiting_time = current.turnaround_time - current.burst_time
                current.is_completed = True
                completed += 1

                result.append({
                    "PID": current.pid,
                    "Arrival Time": current.arrival_time,
                    "Burst Time": current.burst_time,
                    "Start Time": current.start_time,
                    "Completion Time": current.completion_time,
                    "Turnaround Time": current.turnaround_time,
                    "Waiting Time": current.waiting_time
                })

        return result

