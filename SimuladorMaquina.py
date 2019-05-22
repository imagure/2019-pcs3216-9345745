from MotorEventosBase import MotorEventos
from MetodosSimulador import Rotinas


class Simulador(MotorEventos):

    def set_rotinas_dict(self):
        self.rotinas_dict = {
            "0": {"rotina": "jump", "tipo": "J"},
            "1": {"rotina": "jump_if_zero", "tipo": "JIF"},
            "2": {"rotina": "jump_if_negative", "tipo": "JIF"},
            "3": {"rotina": "load_value", "tipo": "L"},
            "4": {"rotina": "add", "tipo": "R"},
            "5": {"rotina": "subtract", "tipo": "R"},
            "6": {"rotina": "multiply", "tipo": "R"},
            "7": {"rotina": "divide", "tipo": "R"},
            "8": {"rotina": "load_from_memory", "tipo": "L"},
            "9": {"rotina": "move_to_memory", "tipo": "S"},
            "A": {"rotina": "subroutine_call", "tipo": "SR"},
            "B": {"rotina": "return_from_subroutine", "tipo": "SR"},
            "C": {"rotina": "halt_machine", "tipo": "HM"},
            "D": {"rotina": "get_data", "tipo": "I"},
            "E": {"rotina": "put_data", "tipo": "O"},
            "F": {"rotina": "operating_system_call", "tipo": "E"},
        }

    def set_lista_de_eventos(self, lista):
        self.lista_de_eventos = lista

    def _identifica_instrucao(self, instrucao):
        if instrucao:
            return instrucao[0]
        else:
            return

    def _executa_rotina(self, tipo_instrucao, instrucao):
        nome_rotina = self.rotinas_dict[tipo_instrucao]["rotina"]
        rotina = getattr(Rotinas, nome_rotina)
        tipo_instrucao = self.rotinas_dict[tipo_instrucao]["tipo"]

        if tipo_instrucao == "R":
            argumento1 = self.acumulador
            endereco = int("0x"+(('%04x' % self.pc)[0:2]), 0) + int("0x" + instrucao[1:4], 0)
            argumento0x = self.lista_de_eventos[endereco]
            argumento2 = int("0x"+argumento0x, 0)
            self.acumulador = rotina(argumento1, argumento2)
            self.pc += 2

        elif tipo_instrucao == "J":
            argumento1 = int("0x"+(('%04x' % self.pc)[0:2]), 0) + int("0x" + instrucao[1:4], 0)
            self.pc = rotina(argumento1)

        elif tipo_instrucao == "SR":
            argumento1 = self.pc
            argumento2 = int("0x"+(('%04x' % self.pc)[0:2]), 0) + int("0x" + instrucao[1:4], 0)
            argumento3 = self.lista_de_eventos
            self.pc = rotina(argumento1, argumento2, argumento3)

        elif tipo_instrucao == "JIF":
            argumento1 = self.acumulador
            argumento2 = int("0x"+(('%04x' % self.pc)[0:2]), 0) + int("0x" + instrucao[1:4], 0)
            argumento3 = self.pc
            self.pc = rotina(argumento1, argumento2, argumento3)

        elif tipo_instrucao == "L":
            argumento1 = self.lista_de_eventos
            argumento2 = int("0x"+(('%04x' % self.pc)[0:2]), 0) + int("0x" + instrucao[1:4], 0)
            argumento3 = int("0x" + instrucao[1:4], 0)
            self.acumulador = rotina(argumento1, argumento2, argumento3)
            self.pc += 2

        elif tipo_instrucao == "S":
            argumento1 = self.acumulador
            argumento2 = int("0x"+(('%04x' % self.pc)[0:2]), 0) + int("0x" + instrucao[1:4], 0)
            argumento3 = self.lista_de_eventos
            rotina(argumento1, argumento2, argumento3)
            self.pc += 2

        elif tipo_instrucao == "I":
            self.acumulador = rotina()
            self.pc += 2

        elif tipo_instrucao == "O":
            argumento1 = self.acumulador
            rotina(argumento1)
            self.pc += 2

        elif tipo_instrucao == "HM":
            argumento1 = int("0x"+(('%04x' % self.pc)[0:2]), 0) + int("0x" + instrucao[1:4], 0)
            self.pc = rotina(argumento1)
            return "FIM"
        return "CONTINUE"


if __name__=='__main__':
    simulador = Simulador()
    simulador.set_lista_de_eventos((['00']*(2 ** 10)))
    simulador.set_rotinas_dict()
    simulador.lista_de_eventos[64] = '01'
    simulador.lista_de_eventos[65] = '01'
    simulador.lista_de_eventos[66] = '01'
    simulador.lista_de_eventos[67] = '01'
    exemplo = ['D0', '00', '90', '44', '60', '40', 'A0', '12', '70', '41', '40', '42', '50', '43', 'E0', '00', 'C0', '00']
    exemplo2 = ['00', '00', '80', '44', '60', '40', '70', '41', '40', '42', '50', '43', 'E0', '00', '20', '00', 'B0', '12']
    for i in range(len(exemplo)):
        simulador.lista_de_eventos[i] = exemplo[i]
    for i in range(len(exemplo2)):
        simulador.lista_de_eventos[i+len(exemplo)] = exemplo2[i]
    simulador.run()
