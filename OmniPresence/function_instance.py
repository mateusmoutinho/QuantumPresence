

from typing import Callable


class FunctionInstance:

    def __init__(self,function:Callable,args=[],kwargs={}) -> None:
        self._function = function
        self._runing = False 
        self._args = args
        self._kwargs = kwargs

    def start(self):
        self._runing = True
        pass 

    def then(self):
        pass 

    def catch(self):
        pass 