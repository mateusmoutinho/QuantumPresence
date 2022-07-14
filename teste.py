from OmniPresence.parallelizer import Parallelizer



def soma(x,y):
    return x + y 



p = Parallelizer()
for x in range(0,10000):
    p.add_function(soma,[10,20])