

from typing import Any, Callable, List
from OmniPresence.function_instance import FunctionInstance




class Parallelizer:

    max_instances = 10
    global_runing_instances = 0 
    
    
    def __init__(self,mode='process') -> None:
        self._mode = mode     
        self._instances:List[FunctionInstance] = []


    @staticmethod
    def set_max_instances(max_instances:int):
        Parallelizer.max_instances = max_instances



    def _start_oldest_instance(self):
        Parallelizer.global_runing_instances+=1
        



        
    def add_function(self,function:Callable,args:list=[],kwargs:dict={}):    
        instance = FunctionInstance(function,args,kwargs)
        self._instances.append(instance) 
        if Parallelizer.global_runing_instances < Parallelizer.max_instances:
            self._start_oldest_instance()
        

    def then(self,result:Any,function:Callable,args=[],kwargs={}):
        pass 

    def catch(self,result:Any,function:Callable,args=[],kwargs={}):
        pass 

    
