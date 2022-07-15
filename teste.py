from OmniPresence.parallelizer import Parallelizer



def soma(x,y):
    return x + y 



p = Parallelizer(instances=2)
for x in range(0,10):
    p.add_function(soma,[x,10])
    

@p.on_all_end
def teste():
    print('executou ao final')
