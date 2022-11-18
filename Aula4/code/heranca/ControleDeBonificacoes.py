#se der erro talvez seja necessario executar o seguinte comando no terminal
#export PYTHONPATH="${PYTHONPATH}:path_para_a_pasta"
from Funcionario import Funcionario,Gerente

from Funcionario import Motorista

class ControleDeBonificacoes:

    def __init__(self, total_bonificacoes=0):
        self.__total_bonificacoes = total_bonificacoes

    def registra(self, funcionario):
        self.__total_bonificacoes += funcionario.get_bonificacao()

    '''get'''
    @property
    def total_bonificacoes(self):
        return self.__total_bonificacoes


funcionario = Funcionario('João', '111111111-11', 2000.0)
print("bonificacao funcionario: {}".format(funcionario.get_bonificacao()))

gerente = Gerente("José", "222222222-22", 5000.0, '1234', 0)
print("bonificacao gerente: {}".format(gerente.get_bonificacao()))

controle = ControleDeBonificacoes()
controle.registra(funcionario)
controle.registra(gerente)

m1 = Motorista("marcos", "23123123123", 3000)

print(m1.get_bonificacao())

print("total: {}".format(controle.total_bonificacoes))
