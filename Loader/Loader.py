

class Loader(object):

    def __init__(self, memoria):
        self.lista_de_eventos = []
        self.eventos_index = 0
        self.memoria = memoria
        self.memoria_index = 0

    def set_lista_de_eventos(self, input_file):
        file = open(input_file, "r")
        for line in file:
            self.lista_de_eventos.append(line)

    def run(self):
        for instrucao in self.lista_de_eventos:
            self._executa_rotina(instrucao)

    def _executa_rotina(self, instrucao):
        if self.eventos_index == 0:
            self.memoria_index = int("0x"+instrucao, 0)
        else:
            self.memoria[self.memoria_index] = instrucao[0:2].rstrip('\n')
            self.memoria[self.memoria_index+1] = instrucao[2:].rstrip('\n')
            self.memoria_index += 2
        self.eventos_index += 1
