class Commit:
    def __init__(self, id, mensaje):
        self.id = id            # id unico del commit
        self.mensaje = mensaje  # mensaje del commit
        self.anterior = None    # puntero al commit anterior

    # metodo para conectar un commit con su commit anterior
    def conectar_anterior(self, anterior):
        self.anterior = anterior