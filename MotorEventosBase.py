import abc


class MotorEventos(object):

    __metaclass__ = abc.ABCMeta

    lista_de_eventos = []

    rotinas_dict = {}

    acumulador = 0

    pc = 0

    def run(self):
        while self.pc < len(self.lista_de_eventos):
            execucao = "CONTINUE"
            instrucao = self.lista_de_eventos[self.pc] + self.lista_de_eventos[self.pc+1]
            if instrucao:
                tipo_instrucao = self._identifica_instrucao(instrucao)
                execucao = self._executa_rotina(tipo_instrucao, instrucao)
            if execucao == "FIM":
                break

    @abc.abstractmethod
    def _identifica_instrucao(self, instrucao):
        return

    @abc.abstractmethod
    def _executa_rotina(self, tipo_instrucao, instrucao):
        return

    @abc.abstractmethod
    def set_lista_de_eventos(self, lista):
        return

    @abc.abstractmethod
    def set_rotinas_dict(self):
        return
