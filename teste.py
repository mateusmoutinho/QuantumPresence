from time import sleep
from QuantumPresence import Parallelizer



def soma(x,y):
    sleep(1)
    result =  x + y 
    print('o resultado e',result)
    return result

p = Parallelizer(instances=10)
for x in range(0,20):
    p.add_function(soma,[x,10])
    

p.start_main_loop()
for x in p._instances:
    print(x._event)