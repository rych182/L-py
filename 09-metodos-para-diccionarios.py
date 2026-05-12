""""
EXERCISE 1: Usa el metodo get() para conseguir el valor de una llave dentro de un diccionario

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}
print(user.get('name'))

-------------------------------------------------------

EXERCISE 2: Muestra un mensaje de error si no se encuentra la llave dentro de un objeto usando el metodo "get()"

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}
print(user.get('apellido', "El dato no existe dentro del diccionario"))

-------------------------------------------------------------------

Exercise 3: muestrame todas las claves que contiene un diccionario
keys()
Te muestra un objeto de tipo dict_keys con las claves que tiene dentro el diccionario
Pero puedes transformarlo a listas

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

print( list(user.keys()))

--------------------------------------------------------
Exercise 4: Muestrame los valores del diccionario

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

print( tuple(user.values()))
---------------------------------------------------------

eXERCISE 5: Muestrame todos los valores en tuplas pares dentro de una lista
, osea su clave y su valor

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

print( list(user.items()))

-------------------------------------------------------

Exercise 6: contar cuantas claves tiene el diccionario

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

print( len(user))

-----------------------------------------------------

Exercise 7: Cuenta cuantas claves hay en un diccionario

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

print( len(user))

---------------------------------------------------------

Exercise 8: agrega una nueva clave y modifica otra ya existente usando una función

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

user.update({
    'name': "Ricardo",
    'plantas': "cactus"
})
print( user)

--------------------------------------------

eXercise 9: agrega una clave a un diccionario usando una función pero sin utilizar llaves
NOTA: setdefault primero intenta "encontrar" el valor de la "clave" y si no la encuentra, la "agrega" y si si esta, solo te muestra el valor
user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

user.setdefault('id',100)
print( user)

id = user.setdefault('id',100)
print(id)

dato = user.setdefault('gata','chana')
print(dato)
------------------------------------------------------------------------------

Exercise 10: Agrega 2 cursos a la clave de cursos en el diccionario usando 2 funciones aprendidas

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}



---------------------------------------------------------------

Exercise 11: eliminar una llave de un diccionario

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

del user['cursos']
print(user)

---------------------------------------------------------------

Exercise 12: otra manera de eliminar una llave en un diccionario 

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

user.pop('name')
print(user)

----------------------------------------------------------------

Exercise 13: Eliminar todas las llaves de un diccionario

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

user.clear()
print(user)

"""

user = {
    'name': 'Ric',
    'age': 39,
    'estado_civil': True,
    'cursos': ["js","python","typescript"],
    'tupla_apellidos': (123,True,"garrido","cruz"),
    'settings': (123,True)
}

user.clear()
print(user)