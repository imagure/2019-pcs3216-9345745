
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
        memoria[endereco] = pc + 1
        print("subroutine_call  end:", endereco)
        return endereco

    @staticmethod
    def return_from_subroutine(endereco):
        print("return_from_subroutine: ", endereco)
        return endereco

    @staticmethod
    def jump_if_zero(acumulador, endereco, pc):
        print("acumulador: ", acumulador)
        if acumulador == 0:
            print("jump_if_zero: true  pc:", endereco)
            return endereco
        print("jump_if_zero: false  pc:", pc+1)
        return pc+1

    @staticmethod
    def jump_if_negative(acumulador, endereco, pc):
        if acumulador < 0:
            print("jump_if_negative: true  pc:", endereco)
            return endereco
        print("jump_if_negative: false  pc:", pc+1)
        return pc + 1

    @staticmethod
    def load_value(memory, value):
        print("load_value: ", value)
        return value

    @staticmethod
    def load_from_memory(memory, endereco):
        value = int("0x"+memory[endereco], 0)
        print("load_from_memory: ", value)
        return value

    @staticmethod
    def move_to_memory(acumulador, endereco, memoria):
        memoria[endereco] = acumulador
        print("move_to_memory  end:", endereco,  "value: ", memoria[endereco])
