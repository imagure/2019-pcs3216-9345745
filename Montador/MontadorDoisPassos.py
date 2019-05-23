import json


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
            "#": None,
            "K": None
        }

    def __init__(self):
        self.lista_de_eventos = []
        self.tabela_simbolos = {}

    def set_lista_de_eventos(self, input_file):
        file = open(input_file, "r")
        for line in file:
            line = self.limpa_comentarios(line)
            self.lista_de_eventos.append(line)

    def limpa_comentarios(self, line):
        i = 0
        while i < len(line):
            if line[i] == ";":
                return line[0:i]
            i += 1
        return line

    def run(self):
        for evento in self.lista_de_eventos:
            lista_simbolos = self.find_symbols(evento)
            # print(lista_simbolos)
            self.identify_symbols(lista_simbolos)
        self.print_tabela_simbolos()

    def find_symbols(self, line):
        return [x.strip().strip(':') for x in line.split()]

    def identify_symbols(self, lista_simbolos):
        valor = None
        for simbolo in lista_simbolos:
            if simbolo[0] == "/":
                valor = simbolo.strip("/")
        for simbolo in lista_simbolos:
            if simbolo not in self.tabela_mnemonicos and len(simbolo) < 4:
                if simbolo not in self.tabela_simbolos:
                    if valor:
                        self.tabela_simbolos[simbolo] = valor
                    else:
                        self.tabela_simbolos[simbolo] = None
                elif valor:
                    self.tabela_simbolos[simbolo] = valor
        print(self.tabela_simbolos)

    def print_tabela_simbolos(self):
        print(json.dumps(self.tabela_simbolos, sort_keys=True, indent=4))
