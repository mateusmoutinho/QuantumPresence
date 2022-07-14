

from typing import Any, Callable, List




class Parallelizer:

    max_instances = 10
    global_runing_instanes = 0 
    
    
    def __init__(self,mode='process') -> None:

        self._runing_instances = 0
        self._mode = mode     
        self._instances:List[dict] = []


    @staticmethod
    def set_max_instances(max_instances:int):
        Parallelizer.max_instances = max_instances



    def _start_oldest_instance(self):
        Parallelizer.global_runing_instanes+=1
        self._runing_instances+=1
        self._instances[0].start()
        

    def add_function(self,function:Callable,args=[],kwargs={}):    
        instance = {
            'function':function,
            'args':args,
            'kwargs':kwargs
        }
        self._instances.append(instance) 
        if self._runing_instances < Parallelizer.max_instances:
            self._start_oldest_instance()
        

    def then(self,result:Any,function:Callable,args=[],kwargs={}):
        pass 

    def catch(self,result:Any,function:Callable,args=[],kwargs={}):
        pass 

    
