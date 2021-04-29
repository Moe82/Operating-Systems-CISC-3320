import sys

class DiskScheduler:
	def __init__(self):
		self.requests = []
		self.algorithm = ""
		self.initial_position = ""
		self.direction = ""
		self.parse_input()

	def parse_input(self):
		# parses the cmd line arguments 
		args = sys.argv
		self.algorithm = args.pop().rstrip(',')
		self.initial_position = args.pop().rstrip(',')
		self.direction = args.pop().rstrip(',')
		for a in args[1:]:
			for part in a.split(","):
				if part.strip():
					self.requests.append(int(part.strip()))

if __name__ == "__main__":
    disk_scheduler = DiskScheduler()