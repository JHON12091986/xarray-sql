class MutableTable:
    """
    Clase para manejar tablas mutables/añadibles en SQL.
    Permite almacenar y actualizar estado iterativo.
    """
    def __init__(self, name, schema):
        self.name = name
        self.schema = schema
        self.data = []

    def append(self, row):
        """Añade una fila a la tabla."""
        self.data.append(row)

    def get_state(self):
        """Obtiene el estado actual de la tabla."""
        return self.data

    def clear(self):
        """Limpia la tabla."""
        self.data = []