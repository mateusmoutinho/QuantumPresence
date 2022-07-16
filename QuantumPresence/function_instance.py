

from typing import Callable


class FunctionInstance:

    def __init__(self,function:Callable,args=[],kwargs={}) -> None:
        self.function = function
        self.name = function.__name__ 
        self.args = args
        self.kwargs = kwargs
        self.error = None 
        self.result = None 
        self.event = None
        self._on_end_function = None 


    def __repr__(self) -> str:
        return f"""\
=====================================================
    name:{self.name},
    args:{self.args},
    kwargs:{self.kwargs},
    error:{self.error},
    result:{self.result}  
"""
         
    def on_end(self,function:Callable):
        self._on_end_function = lambda :function(self)
        


