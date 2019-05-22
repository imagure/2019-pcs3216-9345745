
class Rotinas(object):

    @staticmethod
    def add(a, b):
        print("add: ", a, "+", b, "=", a + b)
        return a+b

    @staticmethod
    def subtract(a, b):
        print("subtract: ", a, "-", b, "=", a - b)
        return a - b

    @staticmethod
    def multiply(a, b):
        print("multiply: ", a, "x", b, "=", a * b)
        return a * b

    @staticmethod
    def divide(a, b):
        print("divide: ", a, ":", b, "=", a / b)
        return a / b

    @staticmethod
    def jump(endereco):
        print("jump: ", endereco)
        return endereco

    @staticmethod
    def subroutine_call(pc, endereco, memoria):
        memoria[endereco] = ('%04x' % (pc + 2))[0:2]
        memoria[endereco+1] = ('%04x' % (pc + 2))[2:]
        print("subroutine_call  end:", endereco)
        return endereco + 2

    @staticmethod
    def return_from_subroutine(pc, endereco, memoria):
        print("return_from_subroutine: ", endereco)
        return int("0x"+memoria[endereco]+memoria[endereco+1], 0)

    @staticmethod
    def jump_if_zero(acumulador, endereco, pc):
        print("acumulador: ", acumulador)
        if acumulador == 0:
            print("jump_if_zero: true  pc:", endereco)
            return endereco
        print("jump_if_zero: false  pc:", pc+2)
        return pc + 2

    @staticmethod
    def jump_if_negative(acumulador, endereco, pc):
        if acumulador < 0:
            print("jump_if_negative: true  pc:", endereco)
            return endereco
        print("jump_if_negative: false  pc:", pc+2)
        return pc + 2

    @staticmethod
    def load_value(memory, endereco,  value):
        print("load_value: ", value)
        return value

    @staticmethod
    def load_from_memory(memory, endereco, value):
        value = int("0x"+memory[endereco]+memory[endereco+1], 0)
        print("load_from_memory: ", value)
        return value

    @staticmethod
    def move_to_memory(acumulador, endereco, memoria):
        memoria[endereco] = ('%04x' % acumulador)[0:2]
        memoria[endereco + 1] = ('%04x' % acumulador)[2:]
        print("move_to_memory  end:", endereco,  "value: ", memoria[endereco]+memoria[endereco+1])

    @staticmethod
    def get_data():
        input_value = input("---------> get_data: ")
        value = int("0x"+input_value, 0)
        print("get_data  value: ", value)
        return value

    @staticmethod
    def put_data(acumulador):
        print("---------> put_data: ", acumulador)

    @staticmethod
    def halt_machine(operando):
        print("halt_machine  end: ", operando)
        return operando
