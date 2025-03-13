import unittest
from app import add_task, complete_task  # Asegúrate de importar correctamente las funciones

class TestApp(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        add_task(tareas, "Estudiar Python")
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]["nombre"], "Estudiar Python")
        self.assertFalse(tareas[0]["completada"])

    def test_completar_tarea(self):
        tareas = [{"nombre": "Estudiar Python", "completada": False}]
        complete_task(tareas, 0)
        self.assertTrue(tareas[0]["completada"])

if __name__ == "__main__":
    unittest.main()
