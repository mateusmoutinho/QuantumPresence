from json import dump
from os import mkdir
from shutil import rmtree
from QuantumPresence.orquestrer import Orquestrer
rmtree('teste',ignore_errors=True)
mkdir('teste')

def executar_sem_paralelizacao():
    for x in range(0,10000):
        with open(f'teste/{x}.json','w') as arq:
            lista = []
            for y in range(0,10000):
                lista.append(y)
            dump(lista,arq)
        print(f'lista {x} completada')



def executa_com_paralelizacao():
    p = Orquestrer(processors=10)
    def criar_arquivo(num:int):
        with open(f'teste/{num}.json','w') as arq:
            lista = []
            for y in range(0,10000):
                lista.append(y)
            dump(lista,arq)
        print(f'lista {num} completada')
    
    for x in range(10000):
        instance = p.add_function(criar_arquivo,args=[x])


    p.start_all_processors()

executa_com_paralelizacao()