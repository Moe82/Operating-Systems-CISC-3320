import sys

class DiskScheduler:
  def __init__(self):
    self.requests = []
    self.algorithm = ""
    self.initial_position = ""
    self.direction = ""
    self.num_head_movements = 0
    self.MAX_CYLINDERS = 4999

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
      self.algorithm = getattr(self, self.algorithm)
      self.algorithm()
    except AttributeError:
      print(self.algorithm + " is not a valid algorithm.")
      sys.exit()

  def CSCAN(self):
    self.requests.append(self.initial_position)
    self.requests.append(self.MAX_CYLINDERS)
    self.requests.append(0)
    self.requests.sort()
    index_of_current_head = self.requests.index(self.initial_position)
    while len(self.requests) > 1:
      if (index_of_current_head == len(self.requests) - 1):
        self.num_head_movements += self.MAX_CYLINDERS
        index_of_current_head = 0
        del self.requests[len(self.requests) - 1]
      else :
        self.num_head_movements += (self.requests[index_of_current_head + 1] - self.requests[index_of_current_head])
        del self.requests[index_of_current_head]

  def print(self):
    print(self.algorithm.__name__ + ": " + str(self.num_head_movements))

if __name__ == "__main__":
  disk_scheduler = DiskScheduler()
  disk_scheduler.parse_input()
  disk_scheduler.service_request()
  disk_scheduler.print()
 