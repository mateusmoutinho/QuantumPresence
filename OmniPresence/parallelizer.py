

from pyclbr import Function
from typing import Any, Callable, List
from OmniPresence.function_instance import FunctionInstance



class Parallelizer:


    
    def __init__(self,instances:int) -> None:    
        self._total_executed = 0 
        self._avaliable_instances = instances
        self._instances:List[FunctionInstance] = []
        self._on_all_end_function = None 
        self._on_all_end_function_executed = False 

    def add_function(self,function:Callable,args:list=[],kwargs:dict={})->FunctionInstance:    
        instance = FunctionInstance(function,args,kwargs)
        self._instances.append(instance) 
        return instance
        
    def on_all_end(self,function:Callable,args:list=[],kwargs:dict={}):
        self._on_all_end_function = lambda: function(*args,**kwargs) 
    

    def _execute_on_all_end_function(self):
        if self._on_all_end_function and not self._on_all_end_function_executed:
            self._on_all_end_function()
            self._on_all_end_function_executed = True 


    def start(self):
        for x in range(self._avaliable_instances):
            self._execute_oldest_instance()



