from MotorEventosBase import MotorEventos
from MetodosSimulador import Rotinas


class Simulador(MotorEventos):

    memory = [None]*(2 ** 16)

    rotinas_dict = {
        "0": {"rotina": "jump", "tipo": "J"},
        "1": {"rotina": "jump_if_zero", "tipo": "B"},
        "2": {"rotina": "jump_if_negative", "tipo": "B"},
        "3": {"rotina": "load_value", "tipo": "L"},
        "4": {"rotina": "add", "tipo": "R"},
        "5": {"rotina": "subtract", "tipo": "R"},
        "6": {"rotina": "multiply", "tipo": "R"},
        "7": {"rotina": "divide", "tipo": "R"},
        "8": {"rotina": "load_from_memory", "tipo": "L"},
        "9": {"rotina": "move_to_memory", "tipo": "S"},
        "A": {"rotina": "subroutine_call", "tipo": "SR"},
        "B": {"rotina": "return_from_subroutine", "tipo": "J"},
        "C": {"rotina": "halt_machine", "tipo": "E"},
        "D": {"rotina": "get_data", "tipo": "E"},
        "E": {"rotina": "put_data", "tipo": "E"},
        "F": {"rotina": "operating_system_call", "tipo": "E"},
        "@": {"rotina": "origin", "tipo": "@"},
        "#": {"rotina": "end", "tipo": "#"},
        "K": {"rotina": "constant", "tipo": "K"}
    }

    def _identifica_instrucao(self, instrucao):
        return instrucao[0]

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

        elif tipo_instrucao == "B":
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


if __name__=='__main__':
    simulador = Simulador()
    simulador.memory[1] = '000F'
    simulador.memory = ['8001', '4001', '5001', '2000']
    simulador.run()

