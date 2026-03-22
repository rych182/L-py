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

BUSCAR DENTRO DE UNA LISTA
print("Python" in courses) y te responde con un valor boolean

"""

courses = ["Python","Javascript","TypeScript","Css","html"]
frameworks =["Laravel","CodeIgniter", "Express JS"]
courses.reverse()
print(courses)