


class GlobalParallelizer:

    max_instances = 10
    global_runing_instances = 0 
    

    
    @staticmethod
    def set_max_instances(max_instances:int):
        GlobalParallelizer.max_instances = max_instances

    @staticmethod
    def increase_runing_instances():
        GlobalParallelizer.global_runing_instances+=1

    @staticmethod
    def decrease_running_instances():
        GlobalParallelizer.global_runing_instances-=1      
    
    @staticmethod
    def permitted_execution()->bool:
        if GlobalParallelizer.global_runing_instances < GlobalParallelizer.max_instances:
            return True 
        return False 

    
