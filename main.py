from Maquina.Maquina import Simulador
from Loader.Loader import Loader
from Montador.MontadorDoisPassos import MontadorDoisPassos

maquina = Simulador()
maquina.set_lista_de_eventos((['00'] * (2 ** 10)))
loader = Loader(maquina.lista_de_eventos)
montador = MontadorDoisPassos()


def executar_codigo(file):
    montador.set_lista_de_eventos('simbolic_code_files/'+file+'.txt')
    assembly_success, error = montador.run()
    montador.print_tabela_simbolos()
    if assembly_success:
        loader.set_lista_de_eventos('object_files/'+file+'.o')
        loader.run()
        maquina.print_memoria(64)
        maquina.set_pc(loader.get_initial_pc())
        maquina.set_rotinas_dict()
        maquina.run()
    else:
        print(error)


def main():
    while True:
        print("\n" + "-" * 30)
        file = input("Qual código deseja executar? \n >")
        executar_codigo(file)


if __name__=='__main__':
    main()
