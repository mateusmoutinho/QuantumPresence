

from typing import Callable


class Paralizer:

    
    def __init__(self,max_instances=10) -> None:
        self._max_instances = max_instances
        self._actual_instances = 0 
        self._pending_instances = []
    

    def start_function(self,function:Callable,args=[],kwargs={}):
        pass 
    
    
