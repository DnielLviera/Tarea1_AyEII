from commit import Commit
from rama import Rama
import random

class Repositorio:
    def __init__(self):
        self.rama = Rama()              # Instancia de la clase Rama, por defecto con el nombre 'main'
        self.rama_uso = self.rama       # Rama de uso
        self.lista_ramas = [self.rama]  # Lista de ramas

    def add(self, archivo):        
        self.rama_uso.lista_archivos.append(archivo)  # Agrega el archivo a la lista de archivos

    def hacer_commit(self, comentario):
        # crear id unico
        while True:
            id_commit = str(random.randint(1000000, 9999999))  # Genera un id aleatorio de 7 digitos

            # verificar si el id ya existe
            if id_commit not in self.rama_uso.lista_id:
                self.rama_uso.lista_id.append(id_commit)
                break

        # crear commit con id y comentario
        commit = Commit(id_commit, comentario)

        # agregar commit a la lista de commits
        self.rama_uso.lista_commits.append(commit)

        # Agrega un puntero del commit actual al anterior
        if len(self.rama_uso.lista_commits) > 1:
            commit.conectar_anterior(self.rama_uso.lista_commits[-2])

    def crear_rama(self, nombre_rama):
        nueva_rama = Rama(nombre_rama)       # Crea una nueva rama
        self.lista_ramas.append(nueva_rama)  # Agrega la nueva rama a la lista de ramas

    def cambiar_rama(self, nombre_rama):
        # Buscar la rama en la lista de ramas
        for rama_i in self.lista_ramas:
            if nombre_rama == rama_i.nombre:
                self.rama_uso = rama_i
    
    def merge(self, nombre_rama):
        # Buscar la rama en la lista de ramas
        for rama_i in self.lista_ramas:
            if nombre_rama == rama_i.nombre:
                rama_merge = rama_i

        # Combina la lista de id de la rama a fusionar a la rama actual
        self.rama_uso.lista_id.extend(rama_merge.lista_id)

        # Combina la lista de commits de la rama a fusionar a la rama actual
        self.rama_uso.lista_commits.extend(rama_merge.lista_commits)

    def mostrar_historial(self):
        # Mostrar el historial de commits de la rama actual
        print(f'Historial de commits de la rama: {self.rama_uso.nombre}')
        for commit in self.rama_uso.lista_commits:
            print(f'{commit.id}: {commit.mensaje}')
        