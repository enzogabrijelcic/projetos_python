class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        
    def __repr__(self):
        return self.descricao
    
    @staticmethod
    def from_string(task_str):
        return Tarefa(task_str)