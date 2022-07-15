from time import sleep
from OmniPresence.parallelizer import Parallelizer



def soma(x,y):
    sleep(10)
    result =  x + y 
    #print('o resultado e',result)


p = Parallelizer(instances=5)
for x in range(0,10):
    p.add_function(soma,[x,10])
    

@p.on_all_end
def teste():
    print('executou ao final')
p.start()