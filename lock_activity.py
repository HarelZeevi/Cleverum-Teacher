import os 
import psutil
import getpass

class LockActivity(): 
    ''' 
    This class takes responsibilty over the remote supervision
    The class is responsible for two main things: 
    1) make sure that the student is not cheating by opening 
        other files in the computer.
    2) make sure that the student doesn't have any internet activity 
        that might be used for cheating by getting help from external resources
    '''
   
    def __init__(self):
        pass  

    def kill_external_programs(self):
        for process in psutil.process_iter():
            try:
                # if it is the current process - don't kill it 
                if process.pid == os.getpid():
                    pass 
                # otherwise, if the process is run by the current user - kill it
                if process.username() == getpass.getuser():
                    process.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def lock_internet_activity():
        pass 


a = LockActivity()
a.kill_external_programs()

        
