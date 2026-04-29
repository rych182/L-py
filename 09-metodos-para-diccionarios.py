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

Exercise 3: Reemplaza un dato 



"""

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