import random

class ModeloTocadoYHundido:
    def __init__(self, tamano_tablero=5):
        self.tamano_tablero = tamano_tablero
        self.tablero = [['-' for _ in range(tamano_tablero)] for _ in range(tamano_tablero)]
        self.barcos = []
        self.casillas_por_atacar = [(x, y) for x in range(tamano_tablero) for y in range(tamano_tablero)]
        self.MAX_SHIP = 2

    def agregar_barco(self, x, y, orientacion):
        if orientacion == "H":  # Horizontal
            if y+1  < self.tamano_tablero and self.tablero[x][y] == '-' and self.tablero[x][y + 1] == '-':
                self.tablero[x][y] = 'B'
                self.tablero[x][y+1] = 'B'
                self.barcos.append([(x, y), (x, y+1)])
                return True
        elif orientacion == "V":  # Vertical
            if x + 1 < self.tamano_tablero and self.tablero[x][y] == '-' and self.tablero[x+1][y] == '-':
                self.tablero[x][y] = 'B'
                self.tablero[x+1][y] = 'B'
                self.barcos.append([(x, y), (x+1, y)])
                return True
        return False

    def agregar_barco_aleatorio(self):
        orientacion = random.choice(["V", "H"])
        if orientacion == "H":
            x = random.randint(0, self.tamano_tablero - 1)
            y = random.randint(0, self.tamano_tablero - 2)
        else:  # When it's vertical
            x = random.randint(0, self.tamano_tablero - 2)
            y = random.randint(0, self.tamano_tablero - 1)

        return self.agregar_barco(x, y, orientacion)

    def elegir_casilla_aleatoria(self):
        x, y = random.choice(self.casillas_por_atacar)
        self.casillas_por_atacar.remove((x, y))
        return x, y