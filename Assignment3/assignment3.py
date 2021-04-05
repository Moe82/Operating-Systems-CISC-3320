from pid_manager import PidManager
from concurrent.futures import ThreadPoolExecutor
from threading import Lock 
import random
from time import sleep

mutex = Lock()

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
  secs_to_sleep = round(random.uniform(0, 10),3) # a random number of seconds to sleep.  
  sleep(secs_to_sleep)
  mutex.acquire()
  try: 
    pid = pid_manager.allocate_id() # critical section
  finally:
    mutex.release();
  print("worker #{} started. sleeping for {} seconds.".format(pid, secs_to_sleep))
  sleep(secs_to_sleep)
  pid_manager.release_pid(pid) # release the pid.
  print("worker #{} died.".format(pid))

def start():
  pid_manager = PidManager() # create an instance of the PidManager class.
  pid_manager.allocate_list() # initialize a list to keep track of allocated pids.
  executor = ThreadPoolExecutor(max_workers=50) # create a thread pool with a max of 50 workers. 
  for x in range(50): # execute 50 threads.
    executor.submit(execute, pid_manager)
	
if __name__ == "__main__":
    start()