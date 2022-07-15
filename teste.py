from time import sleep
from OmniPresence.parallelizer import Parallelizer



def soma(x,y):
    sleep(1)
    result =  x + y 
    print('o resultado e',result)


p = Parallelizer(instances=10)
for x in range(0,60):
    p.add_function(soma,[x,10])
    

p.start_main_loop()