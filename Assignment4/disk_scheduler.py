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

  def FCFS(self):
    for i in range(len(self.requests)):
      if i == 0:
        self.num_head_movements += abs(self.requests[0] - self.initial_position)
      else:
        self.num_head_movements += abs(self.requests[i] - self.requests[i-1])

  def SSTF(self):
    min_seek = float('inf')
    request_with_min_seek = 0
    current_head = self.initial_position
    while len(self.requests) != 0:
      for request in self.requests:
        if (abs(request - current_head) < min_seek):
          min_seek = abs(request - current_head)
          request_with_min_seek = request
      self.num_head_movements += abs(current_head - request_with_min_seek)
      current_head = request_with_min_seek
      self.requests.remove(request_with_min_seek)
      min_seek = float('inf')
    
  def SCAN(self):
    self.requests.append(self.initial_position)
    if self.direction == "left":
      self.requests.append(0)
    elif self.direction == "right":
      self.requests.append(self.MAX_CYLINDERS)
    self.requests.sort()
    index_of_current_head = self.requests.index(self.initial_position)
    while len(self.requests) != 1:
      if self.direction == "left":
        if index_of_current_head == 0:
          self.direction = "right"
        else:
          self.num_head_movements += (self.requests[index_of_current_head] - self.requests[index_of_current_head - 1])
          del self.requests[index_of_current_head]
          index_of_current_head -= 1
      if self.direction == "right":
        if index_of_current_head == len(self.requests) - 1:
          self.direction = "left"
        else:
          self.num_head_movements += (self.requests[index_of_current_head + 1] - self.requests[index_of_current_head])
          del self.requests[index_of_current_head]
         
  def print(self):
    print(self.algorithm.__name__ + ": " + str(self.num_head_movements))

if __name__ == "__main__":
  disk_scheduler = DiskScheduler()
  disk_scheduler.parse_input()
  disk_scheduler.service_request()
  disk_scheduler.print()
 