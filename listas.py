"""
LISTAS: son como arrays
Recomendaciones: Guardar mismos tipos de datos en una lista

my_list = [1,"hola",True,[1,2,3]]
print(my_list)
print(type(my_list))

#           0       1       2       3       4   
#           -5      -4      -3      -2      -1
courses =["Python","Django","Flask","Ruby","MongoDB"]

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