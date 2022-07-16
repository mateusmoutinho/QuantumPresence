from multiprocessing import Process, Manager
from typing import List

from QuantumPresence.function_instance import FunctionInstance

class Processor:
    pass 

    def __init__(self) -> None:
        self._instances:List[FunctionInstance] = []
        
    def total_instances(self):
        return len(self._instances)

    def add_instance(self,instance:FunctionInstance):
        self._instances.append(instance)


    def run_all_instances(self):
        
        def target(instances:List[FunctionInstance]):
            
            for instance in instances:
                pass 
                
        p = Process(target=target,args=[self._instances])
        p.start()
