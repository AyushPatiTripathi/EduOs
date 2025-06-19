class RoundRobin:
	def __init__(self , process_list , time_quantum):
	
	self.process = [Process(*p) for p in process_list]
	self.time_quantum = time_quantum 
	
	
	
   	 def run(self):
   	     time = 0
   	     queue = []
   	     arrived = []
   	     completed = []
   	     n = len(self.processes)
   	     processes = sorted(self.processes, key=lambda x: x.arrival_time)
   	     i = 0
	
   	     while len(completed) < n:
   	         # Enqueue all processes that have arrived by current time
   	         while i < n and processes[i].arrival_time <= time:
   	             queue.append(processes[i])
   	             i += 1
	
   	         if not queue:
   	             time = processes[i].arrival_time
   	             continue
	
   	         current = queue.pop(0)

   	         # First time execution
   	         if current.start_time is None:
   	             current.start_time = time

            # Execution
   	         exec_time = min(self.time_quantum, current.remaining_time)
   	         current.remaining_time -= exec_time
   	         time += exec_time

            # Enqueue any new processes arrived during this exec
   	         while i < n and processes[i].arrival_time <= time:
   	             queue.append(processes[i])
                i += 1

            # Re-queue if not done
   	         if current.remaining_time > 0:
   	             queue.append(current)
   	         else:
   	             current.completion_time = time
   	             current.turnaround_time = current.completion_time - current.arrival_time
   	             current.waiting_time = current.turnaround_time - current.burst_time
   	             completed.append(current)

        # Final Output
   	     return [
   	         {
   	             "PID": p.pid,
   	             "Arrival Time": p.arrival_time,
   	             "Burst Time": p.burst_time,
               	 "Completion Time": p.completion_time,
               	 "Turnaround Time": p.turnaround_time,
   	             "Waiting Time": p.waiting_time
            }
            	for p in completed
        ]
