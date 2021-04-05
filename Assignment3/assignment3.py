from pid_manager import PidManager
from concurrent.futures import ThreadPoolExecutor
from threading import Lock 
import random
from time import sleep

pid_allocation_mutex = Lock()
pid_deallocation_mutex = Lock()
allocated_pids = [] # a list of pids currently allocated 

def race_condition():
  """
  Checks for a race condition by looking for duplicates in the allocated_pids array.
  
  Returns
  ----------
  boolean: true if duplicates found, otherwise, false. 
  """
  if len(allocated_pids) != len(set(allocated_pids)):
    return True
  else:
    return False

def execute(pid_manager):
  """
  The code that each thread executes. Each thread requests a pid number, sleeps
  for a random period of time, then released the pid, allowing another thread to
  pick it up. Each thread sleeps for a random number of seconds before requesting
  a pid so that another thread has the chance to pick up its pid after its released.

  Parameters
  ----------
  pid_manager (PidManager): user-defined object that represents the pid mananger.
  Returns
  ----------
  None
  """
  secs_to_sleep = round(random.uniform(0, 1),3) # a random number of seconds to sleep.  
  sleep(secs_to_sleep)
  pid_allocation_mutex.acquire()
  try: # critical section
    pid = pid_manager.allocate_id() 
    allocated_pids.append(pid)
  finally:
    pid_allocation_mutex.release()
  
  if race_condition():
    print("RACE CONDITON")

  print("worker #{} started. sleeping for {} seconds.".format(pid, secs_to_sleep))
  sleep(secs_to_sleep)

  pid_deallocation_mutex.acquire()
  try:
    pid_manager.release_pid(pid) # release the pid.
    allocated_pids.remove(pid)
  finally:
    pid_deallocation_mutex.release()
  print("worker #{} died.".format(pid))

def start():
  pid_manager = PidManager() # create an instance of the PidManager class.
  pid_manager.allocate_list() # initialize a list to keep track of allocated pids.
  executor = ThreadPoolExecutor(max_workers=500) # create a thread pool with a max of 50 workers. 
  for x in range(500): # execute 50 threads.
    executor.submit(execute, pid_manager)
	
if __name__ == "__main__":
    start()