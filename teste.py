from glob import glob
from time import sleep
from QuantumPresence import Parallelizer,FunctionInstance

def soma(x,y):
    sleep(1)
    return  x + y



p = Parallelizer(instances=10)
global total
total = 0 

for x in range(0,20):
    execution_soma = p.add_function(soma,[x,10])
    
    @execution_soma.on_end
    def test(instance:FunctionInstance):
        global total 
        total+=instance.result


p.start_main_loop()
print(total)