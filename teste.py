from time import sleep
from QuantumPresence import Parallelizer



def soma(x,y):
    sleep(1)
    result =  x + y 
    print('o resultado e',result)
    return result

p = Parallelizer(instances=10)
atributes = {'total':0}

for x in range(0,20):
    execution_soma = p.add_function(soma,[x,10])
    @execution_soma.on_end
    def test(event:dict):
        atributes['total']+= event['return']



p.start_main_loop()
print(atributes)