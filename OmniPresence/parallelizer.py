

from pyclbr import Function
from typing import Any, Callable, List
from OmniPresence.function_instance import FunctionInstance



class Parallelizer:


    
    def __init__(self,instances:int) -> None:    
        self._total_executed = 0 
        self._avaliable_instances = instances
        self._instances:List[FunctionInstance] = []


    def add_function(self,function:Callable,args:list=[],kwargs:dict={}):    
        instance = FunctionInstance(function,args,kwargs)
        instance._execute_oldest_instance =lambda :self._execute_oldest_instance()
        self._instances.append(instance) 

    def on_end(self,function:Callable,args:list=[],kwargs:dict={}):
        pass 
    

    def _execute_oldest_instance(self):
        total_instances = len(self._instances)
        if self._total_executed < total_instances:
            self._total_executed+=1
            oldest_instance = self._total_executed -1
            self._instances[oldest_instance]._execute()
        else:
            print('executou o final')
            
    def __del__(self):
        for x in range(self._avaliable_instances):
            self._execute_oldest_instance()



