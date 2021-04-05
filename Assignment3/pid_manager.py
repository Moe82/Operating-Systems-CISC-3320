class PidManager:
	"""
    A class to represent a PID Manager

    Attributes
    ----------
    __MIN_PID : int
        Smallest pid number
    self.__MAX_PID : int
        Largest pid number
    __pid_list : list
        A list to keep track of allocated pids. If the value at index 10 is equal to 1,
        then the pid number 10 __MIN_PID has been allocated. If the value at that same index
        is 0, then pid number is avaiable. 

    Methods
    -------
    allocate_list(self)
        Initializes a list, which is used to keep track of allocated pid's.
    allocate_id(self)
    	Allocates an pid from __MIN_PID to __MAX_PID (in order).
    release_pid(self, id):
    	Releases a pid. 
    """
	def __init__(self):
		"""
		Constructs the __MIN_PID and __MAX_PID attributes
		
		Parameters
        ----------
        None

        Returns 
        ----------
        None
        """

		self.__MIN_PID = 300
		self.__MAX_PID = 5000
	
	def allocate_list(self):
		"""
		Initializes a list, which is used to keep track of allocated pid's.
		
		Parameters
        ----------
        None

        Returns 
        ----------
        	int: 1 if list initialized successfully, 0 otherwise.
        """
		try:
			self.__pid_list = [0] * (self.__MAX_PID - self.__MIN_PID + 1)
			return 1
		except Exception:
			return -1

	def allocate_id(self):
		"""
		Allocates a pid from __MIN_PID and __MAX_PID (in order).
		
		Parameters
        ----------
        None

        Returns 
        ----------
        	int: the pid number if it was allocated successfully, -1 if __pid_list is full. 
        """
		try:
			try:
				for pid_id in range(self.__MAX_PID):
					if self.__pid_list[pid_id] == 0:
						self.__pid_list[pid_id] = 1
						return pid_id + self.__MIN_PID
			except IndexError:
				return -1
		except AttributeError:
			self.allocate_list()
			return self.allocate_id()

	def release_pid(self, id):
		"""
		Releases a pid. 
		
		Parameters
        ----------
        id (int): pid id to be released. 

        Returns 
        ----------
        	int: 1 if id released successfully, 0 otherwise.
        """
		try:
			try:
				self.__pid_list[id - self.__MIN_PID] = 0
				return 1
			except IndexError:
				print("IndexError: id must be between {} and {}".format(self.__MIN_PID, self.__MAX_PID))
				return -1
		except AttributeError:
			self.allocate_list()
			return self.release_pid(pid_id)