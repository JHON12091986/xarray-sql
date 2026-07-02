class SubscriptAccess:
    """
    Clase para manejar el acceso a tablas mediante subíndices en SQL.
    """
    def __init__(self, table_name, subscript):
        self.table_name = table_name
        self.subscript = subscript

    def get_column(self):
        """Obtiene la columna a partir del subíndice."""
        return f"{self.table_name}.{self.subscript}"

    def get_row(self, index):
        """Obtiene la fila a partir del subíndice."""
        return f"{self.table_name}[{index}]"