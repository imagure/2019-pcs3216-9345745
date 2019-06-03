import sys

class MontadorDoisPassos(object):

    tabela_mnemonicos = {
            "JP": "0",
            "JZ": "1",
            "JN": "2",
            "LV": "3",
            "+": "4",
            "-": "5",
            "*": "6",
            "/": "7",
            "LD": "8",
            "MM": "9",
            "SC": "A",
            "RS": "B",
            "HM": "C",
            "GD": "D",
            "PD": "E",
            "OS": "F",
            "@": None,
            "#": "#",
            "K": "K"
        }

    def __init__(self):
        self.lista_de_eventos = []
        self.tabela_simbolos = {}
        self.index = 0
        self.initial_value = 0
        self.name = None
        self.object_file = None
        self.fim = False

    def set_lista_de_eventos(self, input_file):

        file = open(input_file, "r")
        lines = (line.rstrip() for line in file)
        lines = (line for line in lines if line)
        for line in lines:
            line = self.limpa_comentarios(line)
            self.lista_de_eventos.append(line)

        self.name = input_file.strip("simbolic_code_files").strip(".txt").strip("/")
        self.object_file = open("object_files/"+self.name+".o", "w+")

    def limpa_comentarios(self, line):
        i = 0
        while i < len(line):
            if line[i] == ";":
                return line[0:i]
            i += 1
        return line

    def run(self):

        is_valid = self._verifica_primeira_linha()

        if is_valid:
            self.index = 0
            while self.index < len(self.lista_de_eventos):
                evento = self.lista_de_eventos[self.index]
                lista_simbolos = self.find_symbols(evento)
                self.identify_symbols(lista_simbolos)
                self.index += 1

            self.index = 0
            while self.index < len(self.lista_de_eventos):
                evento = self.lista_de_eventos[self.index]
                lista_simbolos = self.find_symbols(evento)
                self._construct_object_code(lista_simbolos)
                if self.fim:
                    self.index = len(self.lista_de_eventos)
                self.index += 1

            self.object_file.close()

    def _verifica_primeira_linha(self):
        evento = self.lista_de_eventos[0]
        simbolos = self.find_symbols(evento)
        if simbolos[0] == "@":
            self.initial_value = self._find_value(simbolos)
            self.object_file.write("%04x" % self.initial_value+"\n")
            self.lista_de_eventos.remove(evento)
            return True
        else:
            return False

    def find_symbols(self, line):
        return [x.strip() for x in line.split()]

    def _find_value(self, simbolos):
        for simbolo in simbolos:
            if "/" in simbolo:
                valor = simbolo.replace("/", "")
                return int("0x"+valor, 0)

    def identify_symbols(self, lista_simbolos):

        if lista_simbolos[0] not in self.tabela_mnemonicos:
            self.tabela_simbolos[lista_simbolos[0]] = "%04x" % (self.initial_value+self.index*2)

        for simbolo in lista_simbolos:
            if simbolo not in self.tabela_mnemonicos and simbolo[0] != "/":
                if simbolo not in self.tabela_simbolos:
                    self.tabela_simbolos[simbolo] = None

    def _construct_object_code(self, lista_simbolos):
        identificador = ""
        valor = ""

        if lista_simbolos[0] in self.tabela_mnemonicos:
            identificador = self.tabela_mnemonicos[lista_simbolos[0]]
        elif lista_simbolos[1] in self.tabela_mnemonicos:
            identificador = self.tabela_mnemonicos[lista_simbolos[1]]

        for simbolo in lista_simbolos:
            if simbolo not in self.tabela_mnemonicos and simbolo[0] == "/":
                if identificador == "K":
                    valor = simbolo.replace("/", "")[0:4]
                else:
                    valor = simbolo.replace("/", "")[1:4]
            elif simbolo in self.tabela_simbolos and self.tabela_simbolos[simbolo]:
                valor = self.tabela_simbolos[simbolo][1:4]

        if identificador:
            instrucao = ""

            if identificador == "K":
                if valor:
                    instrucao = "" + valor

            elif identificador == "#":
                self.fim = True

            else:
                if valor:
                    instrucao = identificador+valor
                else:
                    instrucao = identificador+"000"

            if instrucao:
                if self.index == len(self.lista_de_eventos)-1:
                    self.object_file.write(instrucao)
                else:
                    self.object_file.write(instrucao+"\n")

    def print_tabela_simbolos(self):
        print("Nome do arquivo: ", self.name)
        print("Inicio do programa: ", self.initial_value)
        print("------------Tabela de símbolos: \n")
        for simbolo in self.tabela_simbolos:
            print("                  | " + simbolo + " <- " + self.tabela_simbolos[simbolo] + " |")
        print("\n------------Fim da tabela de símbolos\n")

        orig_stdout = sys.stdout
        f = open('prints/symbols.txt', 'w')
        sys.stdout = f
        print("------------Tabela de símbolos: \n")
        for simbolo in self.tabela_simbolos:
            print("                  | " + simbolo + " <- " + self.tabela_simbolos[simbolo] + " |")
        print("\n------------Fim da tabela de símbolos\n")
        sys.stdout = orig_stdout
        f.close()
