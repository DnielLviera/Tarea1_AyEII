class Rama:
    def __init__(self, nombre_rama = 'main'):
        self.nombre = nombre_rama   # nombre de la rama
        self.lista_archivos = []    # Crea una lista para guardar los archivos que fueron añadidos a través del comando "add"
        self.lista_id = []          # Crea una lista para guardar los id de los commits
        self.lista_commits = []     # Crea una lista para guardar los commits