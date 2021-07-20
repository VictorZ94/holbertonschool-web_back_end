#!/usr/bin/env python3
from typing import (List, Set, Dict, Tuple)

# Para las listas y los sets solo basta especificar
# el tipo entre corchetes
l: List[int] = [10, 20, 30]
print(l)

s: Set[int] = {3, 6}
print(s)

# Para los diccionarios debemos definir el tipo de datos para
# la clave y su valor

d: Dict[str, int] = {'item': 30}
print(d)

# Para las tuplas podemos definir el tipo de dato
# para cada elemento en caso de que la tupla sea de tamaño fijo
t : Tuple[int, str, float, bool] = (1, 'Hola', 15.6, True)
print(t)

# Si la tupla es de tamaño variable debemos definir el tipo
# seguido de puntos suspensivos
t : Tuple[float, ...] = (12.2, 15.3, 18.4, 16.2)
print(t)
