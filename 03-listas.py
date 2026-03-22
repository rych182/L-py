"""
LISTAS: son como arrays en JS
Recomendaciones: Guardar mismos tipos de datos en una lista
Sublistas: es cortar una parte de una lista

my_list = [1,"hola",True,[1,2,3]]
print(my_list)
print(type(my_list))

#           0       1       2       3       4   
#           -5      -4      -3      -2      -1
courses =["Python","Django","Flask","Ruby","MongoDB"]
Python nos ofrece lectura de listas con números positivos y negativos
value_nuevo= courses[-1]

Sublistas: es cortar una parte de una lista, pones desde donde quieres que empiece a leer
y donde quieres que termine de leer
sublista = courses[0:3]
sublista = courses[:3] #es lo mismo, python lo detecta
#Puede empezar a mostar desde donde tu le digas
sublista_2 = courses[3:5]
#también puedes eludir el último número
sublista_3 = courses[3:]
# Y también puedes hacer una copia exacta, se le llama shallow copy
sublista_4 = courses[:]
#También sirve para dar saltos de 2 en 2 en el array
sublista_saltos = courses[::2]
#El número negativo te muestra todo la lista pero invertida, y puedes dar saltos de 2en2(-2) y 3en3(-3)
sublista_saltos_negativos = courses[::-1]

#OBJETOS MUTABLES: las listas en python, osea en tiempo de ejecución puedes cambiar sus longuitudes, incrementandola o decreciendola

FUNCIONES PARA LISTAS
courses.append("ruby on rails") : sirve para agregar un dato a un array, lo agrega al final
courses.insert(0,"Java")        : inserta un dato en el indice de la lista que le digas
courses.extend(frameworks)      : Une los arrays
print(courses.index("Python"))  : Te muestra en que posicion del indice se encuentra ese dato
courses.remove("html")          : remueve el dato de la lista
courses.pop()                   : remueve el "último"elemento de la lista, también le puedes indicar en el parentesis que posicion deseas eliminar, también podemos almacenarlo en una variable
print(courses.clear())          : Te borra todos los datos de tu lista
copia = courses.copy()          : Genera una copia
courses.reverse()               : te pone al reves la lista(array)
courses.sort()                  : Ordena la lista de forma ascendente, de la A a la Z
courses.sort(reverse=True)      : Forma descendente



BUSCAR DENTRO DE UNA LISTA
print("Python" in courses) y te responde con un valor boolean

MATRICES === Array multidimencional

"""

courses = ["Python","Javascript","TypeScript","Css","html"]
frameworks =["Laravel","CodeIgniter", "Express JS"]
amigos = ["urrutia","carlos","fulano", "diego", "mengano"]
#así conocemos el último índice de nuestra lista
last_index = len(courses) -1
valor = courses[last_index]
#lo mimsmo pero sin la necesidad de guardarlo en una variable
value = courses[len(courses)-1] 
#Leyendo de derecha a izquierda el array, esto nos lo permite python
value_nuevo= courses[-1]

print(courses)
print(valor)
print(len(courses))
print(last_index)
print(value)
print(value_nuevo)

sublista = courses[:3]
sublista_2 = courses[2:4]
sublista_3 = courses[3:]
sublista_4 = courses[:]
sublista_saltos = courses[::2]
sublista_saltos_negativos = courses[::-1]
courses.append("ruby on rails")
courses.append("Php")
courses.insert(0,"Java")
courses.extend(frameworks)
courses.remove("html")
courses.pop()
courses.pop(0)
variable_pop = courses.pop(1)
copia = courses.copy()
frameworks.reverse()
amigos.sort()
amigos.sort(reverse=True)

print(sublista)
print(type(courses))
print(sublista_2)
print(sublista_3)
print(sublista_4)
print(sublista_saltos)
print(sublista_saltos_negativos)
print(courses)
print("Python" in courses)
print(courses.index("Python"))

print(courses)
print(variable_pop)
print(courses.clear())
print(copia)
print(frameworks)
print(amigos)