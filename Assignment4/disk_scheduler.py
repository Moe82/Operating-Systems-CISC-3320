import sys

class DiskScheduler:
	def __init__(self):
		self.requests = []
		self.algorithm = ""
		self.initial_position = ""
		self.direction = ""
		self.num_head_movements = 0

	def parse_input(self):
		# parses the cmd line arguments 
		args = sys.argv
		self.direction = args.pop().rstrip(',')
		self.initial_position = int(args.pop().rstrip(','))
		self.algorithm = args.pop().rstrip(',')
		for a in args[1:]:
			for part in a.split(","):
				if part.strip():
					self.requests.append(int(part.strip()))

	def service_request(self):
		# calls the function with the same name as self.algorithm
		try:
			algorithm = getattr(self, self.algorithm)
			algorithm()
		except AttributeError:
			print(self.algorithm + " is not a valid algorithm.")
			sys.exit()

	def FCFS(self):
		for i in range(len(self.requests)):
			if i == 0:
				self.num_head_movements += abs(self.requests[0] - self.initial_position)
			else:
				self.num_head_movements += abs(self.requests[i] - self.requests[i-1])
	
	def print(self):
		print(self.num_head_movements)



if __name__ == "__main__":
  disk_scheduler = DiskScheduler()
  disk_scheduler.parse_input()
  disk_scheduler.service_request()
  disk_scheduler.print()
