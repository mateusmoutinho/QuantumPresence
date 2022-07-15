
from multiprocessing import Process, Manager
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
        self._status = 'uninitialized'
        self._on_end_function = None 

    def _execute(self):
        self._status = 'running'
        self._event = Manager().dict()

        def target(event:dict):
            event['error'] = None 
            event['result'] = None 
            try:
                event['result'] = self.function(*self.args,**self.kwargs)
            except Exception as e:
                event['error'] = e
                
        self._process  = Process(target=target,args=[self._event],daemon=True)
        self._process.start()
    


    def _update_satus(self)->str:
        if not self._process.is_alive():
            self._status = 'executed'
            self._process.join()
            self.error = self._event['error']
            self.result = self._event['result']
            if self._on_end_function:
                self._on_end_function()

        return self._status


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
        


