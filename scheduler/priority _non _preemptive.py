# priority_non_preemptive.py

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.is_completed = False

class PriorityNonPreemptive:
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

            # Pick process with highest priority (lowest value)
            current = min(ready, key=lambda p: p.priority)

            current.start_time = time
            current.completion_time = time + current.burst_time
            current.turnaround_time = current.completion_time - current.arrival_time
            current.waiting_time = current.turnaround_time - current.burst_time
            current.is_completed = True

            time = current.completion_time
            completed += 1

            result.append({
                "PID": current.pid,
                "Arrival Time": current.arrival_time,
                "Burst Time": current.burst_time,
                "Priority": current.priority,
                "Start Time": current.start_time,
                "Completion Time": current.completion_time,
                "Turnaround Time": current.turnaround_time,
                "Waiting Time": current.waiting_time
            })

        return result

