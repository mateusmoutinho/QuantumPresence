
from inspect import ArgSpec
from multiprocessing import Process, Queue

from typing import Callable


class FunctionInstance:

    def __init__(self,function:Callable,args=[],kwargs={}) -> None:
        self._function = function
        self._status = 'uninitialized'
        self._args = args
        self._kwargs = kwargs
        self._result = None

    def _execute(self):
        self._queue = Queue()
        self._status = 'running'
        def target(queue:Queue):
            try:
                result = self._function(*self._args,**self._kwargs)
                queue.put(result)
            except Exception as e:
                pass

        self._process  = Process(target=target,args=[self._queue])
        self._process.start()
    

    def _update_satus(self)->str:
        if not self._process.is_alive():
            self._status = 'executed'
        return self._status

    def then(self):
        pass 

    def catch(self):
        pass 