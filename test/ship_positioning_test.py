import unittest
from controlador.ControladorTocadoYHundido import ControladorTocadoYHundido  # Replace 'your_module' with the actual module name

class TestControladorTocadoYHundido(unittest.TestCase):

    def setUp(self):
        self.controller = ControladorTocadoYHundido()

    def test_agregar_barco(self):
        self.assertTrue(self.controller.agregar_barco(1, 1, 'H'))
        self.assertTrue(self.controller.agregar_barco(3, 3, 'V'))
        self.assertFalse(self.controller.agregar_barco(1, 1, 'H'))  # Falla
        self.assertFalse(self.controller.agregar_barco(6, 5, 'V'))  # Falla

    def test_todos_barcos_colocados(self):
        self.controller.agregar_barco(1, 1, 'H')
        self.controller.agregar_barco(3, 3, 'V')
        self.assertTrue(self.controller.todos_barcos_colocados())
        self.controller.agregar_barco(3, 0, 'H')
        self.assertFalse(self.controller.todos_barcos_colocados())

if __name__ == '__main__':
    unittest.main()