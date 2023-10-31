from model.ModeloTocadoYHundido import ModeloTocadoYHundido
from vista.VistaTocadoYHundido import VistaTocadoYHundido

class ControladorTocadoYHundido:
    def __init__(self):
        self.modelo_jugador = ModeloTocadoYHundido()
        self.modelo_maquina = ModeloTocadoYHundido()
        self.vista = VistaTocadoYHundido(self)

    def todos_barcos_colocados(self):
        return len(self.modelo_jugador.barcos) == self.modelo_maquina.MAX_SHIP

    def agregar_barco(self, x, y, orientacion):
        agregado = self.modelo_jugador.agregar_barco(x, y, orientacion)
        if self.todos_barcos_colocados():
            self.vista.mostrar_mensaje("¡Todos tus barcos están colocados!")
            self.agregar_barcos_maquina()
            self.vista.cambiar_modo_juego()
        return agregado

    def agregar_barcos_maquina(self):
        barcos_colocados = 0
        while barcos_colocados < 2:
            if self.modelo_maquina.agregar_barco_aleatorio():
                barcos_colocados += 1

    def ataque_maquina(self, x, y):
        for barco in self.modelo_maquina.barcos:
            if (x, y) in barco:
                barco.remove((x, y))
                if not barco:
                    self.modelo_maquina.barcos.remove(barco)
                if not self.modelo_maquina.barcos:
                    self.vista.mostrar_mensaje("¡Has ganado!")
                    self.vista.finalizar_juego()
                return True
        return False

    def ataque_jugador(self, x, y):
        for barco in self.modelo_jugador.barcos:
            if (x, y) in barco:
                barco.remove((x, y))
                if not barco:
                    self.modelo_jugador.barcos.remove(barco)
                if not self.modelo_jugador.barcos:
                    self.vista.mostrar_mensaje("¡Has perdido!")
                    self.vista.finalizar_juego()
                return True
        return False

    def iniciar_juego(self):
        self.vista.run()

    def turno_maquina(self):
        i=0
        while True:
            i+=1
            x, y = self.modelo_maquina.elegir_casilla_aleatoria()
            if self.ataque_jugador(x, y):  # Comprobamos si ha acertado
                self.vista.botones_jugador[x][y].config(text="X", bg="red")
            else:
                self.vista.botones_jugador[x][y].config(text="O", bg="blue")
            break