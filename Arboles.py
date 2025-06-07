# TRABAJO PRACTICO INTEGRADOR: ARBOL BINARIO
# Clase que representa un nodo del arbol
class Nodo:
    def __init__(self, valor):
        # Valor del nodo
        self.valor = valor
        # Hijo izquierdo e hijo derecho
        self.izq = None
        self.der = None

# Clase que representa el arbol binario
class Arbol:
    # Funcion que inicia el nodo raiz del arbol
    def __init__(self):
        self.raiz = None

    # Funcion para ubicar un valor en el arbol
    def ubicar(self, valor):
        # Si el arbol esta vacio, crea la raiz con el primer numero o letra
        if self.raiz is None:
            self.raiz = Nodo(valor)
        # Si no, llama al metodo recursivo para ubicar el valor correctamente
        else:
            self._ubicar_recursivo(self.raiz, valor)

    # Funcion para insertar el valor en la posicion correcta
    def _ubicar_recursivo(self, nodoActual, valor):
        # Insertar a la izquierda si el valor es menor al nodo actual
        if valor < nodoActual.valor:
            if nodoActual.izq is None:
                nodoActual.izq = Nodo(valor)
            else:
                self._ubicar_recursivo(nodoActual.izq, valor)
        # Insertar a la derecha si el valor es mayor al nodo actual
        else:
            if nodoActual.der is None:
                nodoActual.der = Nodo(valor)
            else:
                self._ubicar_recursivo(nodoActual.der, valor)

    # Funcion para hacer recorrido preorden: raiz, izquierda, derecha
    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izq)
            self.preorden(nodo.der)
    
    # Funcion para hacer recorrido inorden: izquierda, raiz, derecha
    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izq)
            print(nodo.valor, end=" ")
            self.inorden(nodo.der)

    # Funcion para hacer recorrido postorden: izquierda, derecha, raiz
    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            print(nodo.valor, end=" ")

# Función para preguntar con que trabajar
def obtener_tipo_dato():
    while True:
        tipo = input("¿Con qué deseas trabajar, letras(L) o números(N)? ").strip().lower()
        if tipo in ["l", "n"]:
            return "letras" if tipo == "l" else "numeros"
        print("Opción inválida. Escribe 'L' o 'N'.")

# Valida la entrada
def validar_entrada(lista, tipo):
    if tipo == "letras":
        return all(elem.isalpha() for elem in lista)
    else:
        return all(elem.isdigit() for elem in lista)

# Inicio 
tipo_dato = obtener_tipo_dato() 
entrada = input(f"Ingresá {'letras separadas' if tipo_dato == 'letras' else 'números separados'} por espacios: ").split()

# Si ingresa mal, sale un aviso, sino se crea el arbol
if not validar_entrada(entrada, tipo_dato):
    print(f"Error: Ingresaste valores que no son {tipo_dato}.")
else:
    arbol = Arbol()
    if tipo_dato == "letras":
        for letra in entrada:
            arbol.ubicar(letra.upper())
    else:
        for numero in entrada:
            arbol.ubicar(int(numero))

# Opciones para que el usuario eliga que quiere ver raiz, ramas o hojas o todo.
opcion = int(input("\nPara ver cual es Raiz, cual es Rama y cual es Hoja ingresa:\n1. Ver Nodo Raiz.\n2. Ver Nodo Rama.\n3. Ver Nodo Hoja.\nPara ver todas las opciones presione cualquier otro número.\n"))

# Lista para almacenar los nodos
raiz = []
rama = []
hoja = []

# Funcion recursiva para clasifica los nodos del arbol y guardarlos en las listas
def clasificar_nodos(nodo, es_raiz = False):
    if nodo:
        # El primero es el nodo raiz, luego sigue con los rama y los ultimos son los hijos
        if es_raiz:
            raiz.append(nodo.valor)
        # Nodo con hijos
        elif nodo.izq or nodo.der:
            rama.append(nodo.valor)
        # Nodo sin hijos
        else:
            hoja.append(nodo.valor)

        # Recorre hijo izquierdo
        clasificar_nodos(nodo.izq)
        # Recorre hijo derecho
        clasificar_nodos(nodo.der)

# Se llama a la funcion con es_raiz True para que el primero sea la raiz
clasificar_nodos(arbol.raiz, es_raiz = True)

# Convierte numeros a string para imprimir porque .join no anda con con int
if tipo_dato == "numeros":
    raiz = [str(v) for v in raiz]
    rama = [str(v) for v in rama]
    hoja = [str(v) for v in hoja]

# Muestra los nodos segun la opcion elegida
if opcion == 1:
    print(f"\nNodo Raiz: {' '.join(raiz)}")
elif opcion == 2:
    print(f"\nNodo/s Rama: {' '.join(rama)}")
elif opcion == 3:
    print(f"\nNodo/s Hoja: {' '.join(hoja)}")
else:
    print(f"\nNodo Raiz: {' '.join(raiz)}")
    print(f"Nodo/s Rama: {' '.join(rama)}")
    print(f"Nodo/s Hoja: {' '.join(hoja)}")

# Pregunta al usuario que tipo de recorrido mostrar
opcion = int(input("\nPara ver recorridos ingresa:\n1. Recorrido Preorden.\n2. Recorrido Inorden.\n3. Recorrido Postorden.\nPara ver todas las opciones presione cualquier otro número.\n"))

# Ejecuta el recorrido elegido
if opcion == 1:
    print("\nRecorrido Preorden:")
    arbol.preorden(arbol.raiz)
elif opcion == 2:
    print("\nRecorrido Inorden:")
    arbol.inorden(arbol.raiz)
elif opcion == 3:
    print("\nRecorrido Postorden:")
    arbol.postorden(arbol.raiz)
else:
    print("\nRecorrido Preorden:")
    arbol.preorden(arbol.raiz)
    print("\nRecorrido Inorden:")
    arbol.inorden(arbol.raiz)
    print("\nRecorrido Postorden:")
    arbol.postorden(arbol.raiz)