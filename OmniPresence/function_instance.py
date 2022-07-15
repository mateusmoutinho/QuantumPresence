

from typing import Callable


class FunctionInstance:

    def __init__(self,function:Callable,args=[],kwargs={}) -> None:
        self._function = function
        self._runing = False 
        self._args = args
        self._kwargs = kwargs
        self._execute_oldest_instance:Callable = None 

    def _execute(self):
        result = self._function(*self._args,**self._kwargs)
        print('result',result)
        self._execute_oldest_instance()

    def then(self):
        pass 

    def catch(self):
        pass 