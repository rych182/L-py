"""
NOTA: Si repites una "propiedad", se guardará el valor de la última propiedad

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'name': "Nuevo Nombre"
}

Esto también funciona pero es poco usable:

user = { 
    10: "Rick",
    3.1416: "PI",
    True: False,
    (1,2,3): "Tupla"
}

En Python: clave o llave


-----------------------------------

EXERCISE 1: busca si una llave existe dentro de un diccionario

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

print("name" in user)

-------------------------------------------------------

EXERCISE 2: Acceder a alguna llave de un diccionario
user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}
print(user['name'])

-----------------------------------------------------

Exercise 3: Mete nuevas llaves con datos a un diccionario

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}
user['apellido'] = "Garrido"
print(user)

--------------------------------------------------------

Exercise 4: reescribe un valor de una llave en un diccionario

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}
user['apellido'] = "Garrido"
user['name'] = "ricky"
print(user)

----------------------------------------------------------

"""
user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}
print(user['name'])