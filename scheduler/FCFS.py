class Process :
	def __init__(self ,pid,arrival_time ,burst_time):
		self.pid = pid
		self.arrival_time = arrival_time
		self.burst_time = burst_time 
		self.start_time = 0
		self.completion_time = 0
		self.turnaround_time = 0
		self.waiting_time = 0
class FCFS:
	def __init(self ,process_list):
	
	self.processes = [Process(*p) for p in process_lists]
	
	def run(self):
		self.process.sort(key=lambda p: p.arrival )
		current_time = 0
		results =[]
		
		for process in self.processes :
			if current_time < process.arrival_time :
				current_time = process.arrival_time
			process.start_time = current_time
			process.completion_time =current_time + process.burst_time
			process.turnaround_time = process.completion_time - process.arrival_time
			process.waiting_time = process.turnaround_time - process.burst_time
			
			current_time = process.completion_time
			
			results.append({
			"PID":process.pid,
			"Arrival Time":process.arrival_time,
			"Burst Time":process.burst_time,
			"Start Time":process.start_time,
			"Completion Time":process.turnaround_time,
			"Waiting Time":process.waiting_time
			})
		return results
			
