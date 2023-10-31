import tkinter as tk
from tkinter import messagebox

class VistaTocadoYHundido:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Tocado y Hundido")


        # Títulos de los tableros
        tk.Label(self.ventana, text="Tablero del Jugador").grid(row=0, column=0, columnspan=5)
        tk.Label(self.ventana, text="Tablero de la Máquina").grid(row=0, column=7, columnspan=5)

        # Creando tableros (botones) para el jugador y la máquina
        self.botones_jugador = [[None for _ in range(5)] for _ in range(5)]
        self.botones_maquina = [[None for _ in range(5)] for _ in range(5)]

        # Tablero del jugador
        for i in range(5):
            for j in range(5):
                self.botones_jugador[i][j] = tk.Button(self.ventana, text="-", width=4, height=2,
                                                       command=lambda i=i, j=j: self.onClick(i, j))
                self.botones_jugador[i][j].grid(row=i+1, column=j)

        # Tablero de la máquina (inicialmente inactivo)
        for i in range(5):
            for j in range(5):
                self.botones_maquina[i][j] = tk.Button(self.ventana, text="-", width=4, height=2, state=tk.DISABLED,
                                                       command=lambda i=i, j=j: self.intento_ataque(i, j))
                self.botones_maquina[i][j].grid(row=i+1, column=j+7)

        # Espaciado (Separador) entre los tableros
        for i in range(5):
            tk.Label(self.ventana, text="   ").grid(row=i+1, column=5)

        # Radiobuttons para la orientación de los barcos
        self.orientacion = tk.StringVar(value="H")
        tk.Radiobutton(self.ventana, text="Horizontal", variable=self.orientacion, value="H").grid(row=7, column=0, columnspan=2)
        tk.Radiobutton(self.ventana, text="Vertical", variable=self.orientacion, value="V").grid(row=7, column=3, columnspan=2)

    def onClick(self, x, y):
        orientacion = self.orientacion.get()
        if self.controlador.agregar_barco(x, y, orientacion):
            if orientacion == "H":
                self.botones_jugador[x][y].config(text="B")
                self.botones_jugador[x][y + 1].config(text="B")
            else:
                self.botones_jugador[x][y].config(text="B")
                self.botones_jugador[x + 1][y].config(text="B")
            if self.controlador.todos_barcos_colocados():
                messagebox.showinfo("Listo", "¡Juego listo!")
                self.cambiar_modo_juego()
        else:
            messagebox.showerror("Error", "¡Posición inválida para el barco!")

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información", mensaje)

    def cambiar_modo_juego(self):
        # Desactivar botones del jugador
        for fila in self.botones_jugador:
            for btn in fila:
                btn.config(state=tk.DISABLED)

        # Activar botones de la máquina para que el jugador pueda atacar
        for fila in self.botones_maquina:
            for btn in fila:
                btn.config(state=tk.NORMAL)

    def intento_ataque(self, x, y):
        if self.botones_maquina[x][y]['state'] == tk.DISABLED:
            return
        if self.controlador.ataque_maquina(x, y):
            self.botones_maquina[x][y].config(text="X", bg="red")
        else:
            self.botones_maquina[x][y].config(text="O", bg="blue")
        self.botones_maquina[x][y].config(state=tk.DISABLED)

        self.controlador.turno_maquina()

    def finalizar_juego(self):
        for fila in self.botones_maquina:
            for btn in fila:
                btn.config(state=tk.DISABLED)

    def run(self):
        self.ventana.mainloop()
