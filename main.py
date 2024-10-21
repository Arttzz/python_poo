from funcionarios import *

if __name__ == "__main__":
    g1 = Gerente("Arthur", "1234341", 345)
    print(g1)
    if g1.autenticar("1234341", 345):
        print(g1.cancelar())
    else:
        print("Falha de autenticação")

    op1 = Operador_Caixa("Cleber", "12314241", 234, 2)

    if op1.autenticar("2", 234):
        print (op1.registrar_produto())

    else: 
        print("Falha de autenticação")

    s1 = Seguranca("Cleber", "12314241", 234, 5)

    if s1.autenticar("5", 234):
        print (s1.acionar_alarme())

    else:
        print("Falha ao acionar alarme")
