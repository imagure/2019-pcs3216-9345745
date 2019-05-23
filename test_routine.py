from Maquina.Maquina import Simulador
from Loader.Loader import Loader
from Montador.MontadorDoisPassos import MontadorDoisPassos

maquina = Simulador()
maquina.set_lista_de_eventos((['00'] * (2 ** 10)))
loader = Loader(maquina.lista_de_eventos)
montador = MontadorDoisPassos()


def testa_maquina():
    maquina.set_rotinas_dict()
    maquina.lista_de_eventos[64] = '01'
    maquina.lista_de_eventos[65] = '01'
    maquina.lista_de_eventos[66] = '01'
    maquina.lista_de_eventos[67] = '01'
    exemplo1 = ['D0', '00', '90', '44', '60', '40', 'A0', '12', '70', '41',
               '40', '42', '50', '43', 'E0', '00', 'C0', '00']
    exemplo2 = ['00', '00', '80', '44', '60', '40', '70', '41', '40', '42',
                '50', '43', 'E0', '00', '20', '00', 'B0', '12']
    for i in range(len(exemplo1)):
        maquina.lista_de_eventos[i] = exemplo1[i]
    for i in range(len(exemplo2)):
        maquina.lista_de_eventos[i + len(exemplo1)] = exemplo2[i]
    maquina.run()


def testa_loader():
    loader.set_lista_de_eventos('object_files/test_code.o')
    loader.run()
    maquina.print_memoria(64)


def testa_loader_maquina():
    loader.set_lista_de_eventos('object_files/test_code.o')
    loader.run()
    maquina.set_rotinas_dict()
    maquina.lista_de_eventos[64] = '01'
    maquina.lista_de_eventos[65] = '01'
    maquina.lista_de_eventos[66] = '01'
    maquina.lista_de_eventos[67] = '01'
    maquina.run()


def testa_montador():
    montador.set_lista_de_eventos('simbolic_code_files/test_code.txt')
    montador.run()


if __name__=='__main__':
    # testa_maquina()
    # testa_loader()
    # testa_loader_maquina()
    testa_montador()