from MotorEventosBase import MotorEventos
from MetodosSimulador import Rotinas


class Simulador(MotorEventos):

    rotinas_dict = {
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
        "B": {"rotina": "return_from_subroutine", "tipo": "J"},
        "C": {"rotina": "halt_machine", "tipo": "HM"},
        "D": {"rotina": "get_data", "tipo": "I"},
        "E": {"rotina": "put_data", "tipo": "O"},
        "F": {"rotina": "operating_system_call", "tipo": "E"},
    }

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
            argumento2 = int("0x"+self.memory[int("0x" + instrucao[1:4], 0)], 0)
            self.acumulador = rotina(argumento1, argumento2)
            self.pc += 1

        elif tipo_instrucao == "J":
            argumento1 = int("0x" + instrucao[1:4], 0)
            self.pc = rotina(argumento1)

        elif tipo_instrucao == "SR":
            argumento1 = self.pc
            argumento2 = int("0x" + instrucao[1:4], 0)
            argumento3 = self.memory
            self.pc = rotina(argumento1, argumento2, argumento3)

        elif tipo_instrucao == "JIF":
            argumento1 = self.acumulador
            argumento2 = int("0x" + instrucao[1:4], 0)
            argumento3 = self.pc
            self.pc = rotina(argumento1, argumento2, argumento3)

        elif tipo_instrucao == "L":
            argumento1 = self.memory
            argumento2 = int("0x" + instrucao[1:4], 0)
            self.acumulador = rotina(argumento1, argumento2)
            self.pc += 1

        elif tipo_instrucao == "S":
            argumento1 = self.acumulador
            argumento2 = int("0x" + instrucao[1:4], 0)
            argumento3 = self.memory
            rotina(argumento1, argumento2, argumento3)
            self.pc += 1

        elif tipo_instrucao == "I":
            self.acumulador = rotina()
            self.pc += 1

        elif tipo_instrucao == "O":
            argumento1 = self.acumulador
            rotina(argumento1)
            self.pc += 1

        elif tipo_instrucao == "HM":
            argumento1 = int("0x" + instrucao[1:4], 0)
            self.pc = rotina(argumento1)


if __name__=='__main__':
    simulador = Simulador()
    simulador.memory[10] = '0001'
    simulador.memory[11] = '000E'
    exemplo = ['D000', '400A', '500B', 'E000', '2000', 'C000']
    for item in exemplo:
        simulador.memory[exemplo.index(item)] = item
    simulador.run()
