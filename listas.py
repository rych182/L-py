"""
LISTAS: son como arrays
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

"""

courses = ["Python","Javascript","TypeScript","Css","html"]
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
print(sublista)
print(type(courses))
print(sublista_2)
print(sublista_3)
print(sublista_4)