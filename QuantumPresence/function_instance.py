
from inspect import ArgSpec
from multiprocessing import Process, Manager

from typing import Callable


class FunctionInstance:

    def __init__(self,function:Callable,args=[],kwargs={}) -> None:
        self._function = function
        self._status = 'uninitialized'
        
        self._args = args
        self._kwargs = kwargs
        self._event = None

    def _execute(self):
        self._status = 'running'
        self._event = Manager().dict()
        def target(event:dict):
            event['function_name'] =self._function.__name__
            event['function'] = self._function
            event['args'] = self._args
            event['kwargs'] = self._kwargs
            event['error'] = None 
            event['return'] = None 
 
            try:
                return_value = self._function(*self._args,**self._kwargs)
                event['return'] = return_value
            except Exception as e:
                event['error'] = e
                
        self._process  = Process(target=target,args=[self._event])
        self._process.start()
    


    def _update_satus(self)->str:
        if not self._process.is_alive():
            self._status = 'executed'
            self._process.join()
            
        return self._status


    def then(self,function:Callable):
        pass 


