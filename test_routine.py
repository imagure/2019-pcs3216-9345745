from Maquina.SimuladorMaquina import Simulador

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
