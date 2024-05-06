from queue import Queue

# Definimos una clase para representar el problema en el espacio de estados
class ProblemaEspacioEstados:
    def __init__(self, estado_inicial, estado_meta, acciones):
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta
        self.acciones = acciones

    def aplicar_accion(self, estado, accion):
        # Esta función simula la aplicación de una acción en un estado dado
        # Aquí deberías implementar la lógica para aplicar la acción y obtener el nuevo estado
        nuevo_estado = estado + accion
        return nuevo_estado

    def es_estado_meta(self, estado):
        # Esta función verifica si un estado dado es el estado meta
        return estado == self.estado_meta

    def generar_sucesores(self, estado):
        # Esta función genera los sucesores alcanzables desde un estado dado aplicando las acciones disponibles
        sucesores = []
        for accion in self.acciones:
            nuevo_estado = self.aplicar_accion(estado, accion)
            sucesores.append((accion, nuevo_estado))
        return sucesores

# Definimos una función para realizar la búsqueda en el espacio de estados
def busqueda_espacio_estados(problema):
    # Inicializamos una cola para la búsqueda en anchura
    cola = Queue()
    # Añadimos el estado inicial a la cola
    cola.put((problema.estado_inicial, []))  # El segundo elemento de la tupla representa el camino hasta este estado

    while not cola.empty():
        estado_actual, camino_actual = cola.get()
        # Verificamos si hemos alcanzado el estado meta
        if problema.es_estado_meta(estado_actual):
            return camino_actual
        # Generamos los sucesores y los añadimos a la cola
        sucesores = problema.generar_sucesores(estado_actual)
        for accion, nuevo_estado in sucesores:
            nuevo_camino = camino_actual + [accion]
            cola.put((nuevo_estado, nuevo_camino))

    # Si no se encontró una solución
    return None

# Definimos el estado inicial y el estado meta
estado_inicial = "A"
estado_meta = "D"

# Definimos las acciones disponibles
acciones = ["->B", "->C", "->D"]

# Creamos el problema en el espacio de estados
problema = ProblemaEspacioEstados(estado_inicial, estado_meta, acciones)

# Realizamos la búsqueda en el espacio de estados
camino_solucion = busqueda_espacio_estados(problema)

# Mostramos el camino solución
if camino_solucion:
    print("Camino solución encontrado:", camino_solucion)
else:
    print("No se encontró un camino solución.")
