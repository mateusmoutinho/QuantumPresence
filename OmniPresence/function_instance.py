
from inspect import ArgSpec
from multiprocessing import Process, Queue

from typing import Callable


class FunctionInstance:

    def __init__(self,function:Callable,args=[],kwargs={}) -> None:
        self._function = function
        self._runing = False 
        self._args = args
        self._kwargs = kwargs
        self._result = None
        self._execute_oldest_instance:Callable = None 

    def _execute(self):
        queue = Queue()
        def target(queue:Queue):
            try:
                result = self._function(*self._args,**self._kwargs)
                queue.put(result)
            except Exception as e:
                pass

        p = Process(target=target,args=[queue])
        p.start()
        p.join() # this blocks until the process terminates
        self._result = queue.get()
        print(self._result)
        
        self._execute_oldest_instance()

    def then(self):
        pass 

    def catch(self):
        pass 