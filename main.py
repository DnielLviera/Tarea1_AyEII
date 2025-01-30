from repositorio import Repositorio
from archivo import Archivo

class Main:
    # Ejemplo de uso
    repo = Repositorio() # Instancia de la clase Repositorio
    archivo = Archivo() # Instancia de la clase Archivo

    repo.add(archivo) # Agregar un archivo

    repo.hacer_commit('primer commit') # Crea un commit con el mensaje 'primer commit' en la rama 'main'
    repo.hacer_commit('segundo commit') # Crea un commit con el mensaje 'segundo commit' en la rama 'main'

    repo.crear_rama('develop') # Crea una rama llamada 'develop'
    repo.cambiar_rama('develop') # Cambia a la rama 'develop'
    repo.hacer_commit('otro commit') # Crea un commit con el mensaje 'otro commit' en la rama 'develop'

    repo.cambiar_rama('main') # Cambia a la rama 'main'
    repo.mostrar_historial() # Muestra el historial de commits de la rama 'main'

    repo.cambiar_rama('develop') # Cambia a la rama 'develop'
    repo.mostrar_historial() # Muestra el historial de commits de la rama 'develop'

    print() # Salto de línea
    repo.cambiar_rama('main') # Cambia a la rama 'main'
    repo.merge('develop') # Une la rama 'develop' con la rama 'main'
    repo.mostrar_historial() # Muestra el historial de commits de la rama 'main'