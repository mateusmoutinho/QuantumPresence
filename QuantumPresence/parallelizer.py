

from pyclbr import Function
from typing import Any, Callable, List
from QuantumPresence.function_instance import FunctionInstance



class Parallelizer:


    
    def __init__(self,instances:int) -> None:    
        self._total_executed = 0 
        self._avaliable_instances = instances
        self._instances:List[FunctionInstance] = []


    def add_function(self,function:Callable,args:list=[],kwargs:dict={})->FunctionInstance:    
        instance = FunctionInstance(function,args,kwargs)
        self._instances.append(instance) 
        return instance
        
    def start_main_loop(self):
        while self._total_executed < len(self._instances):
            for instance in self._instances:
                status = instance._status
                
                if status == 'uninitialized' and self._avaliable_instances > 0:
                    instance._execute()
               
                    self._avaliable_instances-=1
                
                if status == 'running':
                    if instance._update_satus() ==  'executed':
                        self._avaliable_instances+=1
                        self._total_executed+=1

        





