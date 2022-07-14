

from typing import Any, Callable, List
from OmniPresence.function_instance import FunctionInstance
from OmniPresence.global_parallelizer import GlobalParallelizer




class Parallelizer(GlobalParallelizer):


    
    def __init__(self,mode='process') -> None:
        self._mode = mode     
        self._instances:List[FunctionInstance] = []



    def add_function(self,function:Callable,args:list=[],kwargs:dict={}):    
        instance = FunctionInstance(function,args,kwargs)
        self._instances.append(instance) 


    def start_oldest_instance(self):
        pass 


    def start(self):
        pass 


    def then(self,function:Callable,args=[],kwargs={}):
        pass 

    def catch(self,function:Callable,args=[],kwargs={}):
        pass 

    
