from abc import ABC, abstractmethod

class Funcionario(ABC):
    nome : str
    cpf : str
    __senha : str

    def __init__(self, n:str, cpf:str, senha:int):
        self.nome = n
        self.cpf = cpf 
        self.__senha = senha 

    def __str__(self):
        info = f'Nome: {self.nome}\n'
        info += f'CPF: {self.cpf}'
        return info 
    
    def get_senha(self):
        return self.__senha
    
    @abstractmethod
    def autenticar(self, user:str, senha:int):
        pass


class Gerente(Funcionario):
    def autenticar(self, user: str, senha: int):
        if user == self.cpf and senha == self.get_senha() :
            return True
        return False 
            
    def cancelar(self):
        return "Operacao cancelada"
    
class Operador_Caixa(Funcionario):
    numero_caixa:int

    def __init__(self, n: str, cpf: str, senha: int, numero_caixa:int):
        super().__init__(n, cpf, senha)
        self.numero_caixa = numero_caixa
    
    def __str__(self):
        info = super().__str__()
        info += f'\nNumero Caixa{self.numero_caixa}\n'
        return info

    def autenticar(self, user: str, senha: int):
        if int(user) == self.numero_caixa and senha == self.get_senha() :
            return True
        return False 
    
    def registrar_produto(self):
        return "Produto Registrado"

class Seguranca(Funcionario):
     
    posto:int

    def __init__(self, n: str, cpf: str, senha: int, posto:int):
        super().__init__(n, cpf, senha)
        self.posto = posto

    def __str__(self):
        info = super().__str__()
        info += f'\nPosto: {self.posto}\n'
        return info

    def autenticar(self, user: str, senha: int):
        if int(user) == self.posto and senha == self.get_senha() :
            return True
        return False
    
    def acionar_alarme(self):
        return "Alarme acionado"