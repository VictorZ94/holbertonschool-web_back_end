#!/usr/bin/python3

def greetings(name: str) -> str:
    return f"Hello {name}!"

print(greetings("Víctor"))


def new_greetings(name: str) -> None:
    print(f"Hello {name}!")

new_greetings("Mom")

# type annotation int typed

a: int = 20 # annotation to variable
print(a)

def add(a: int, b: int) -> int:
    return a + b

""" type annotation no son reglas solamente anotaciones que indican
el tipo de dato que la funcion debería recibir, pero no importa si se pasa otro tipo
no dara error
"""
print(add(20.80, 50.15))

# default values

def sustraction(a: int, b: int = 20) -> int:
    return a - b

print(sustraction(50))