

from pyclbr import Function
from time import sleep
from typing import Any, Callable, List
from QuantumPresence.function_instance import FunctionInstance
from QuantumPresence.processor import Processor
import numpy as np

class Orquestrer:


    
    def __init__(self,process:int) -> None:    
        self._processors:List[Processor] = list(map(
            lambda index:Processor(),
            range(process)
        ))
    

    def get_lower_processor(self)->int:
        instances = list(map(
            lambda processor:processor.total_instances(),
            self._processors
        ))
        return np.argmin(instances)
        
    def add_function(self,function:Callable,args:list=[],kwargs:dict={})->FunctionInstance:    
        instance = FunctionInstance(function,args,kwargs)
    
        index = self.get_lower_processor()
        self._processors[index].add_instance(instance)
        return instance
        
    def start_all_processors(self):
        for processor in self._processors:
            processor.run_all_instances()
        




