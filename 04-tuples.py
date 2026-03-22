

""""
APUNTES
#Puedes ver las posiciones en las tuplas con número positivios y negativos
#No puedes sobreescribir el espacio de memoria de una tupla
#Aunque no le pongas parentesis pero les pongas "comas", Python se da cuenta de que es una Tupla
#Si quieres crear una Tupla de 1 solo dígito, ponle una "coma" al final, así: numero = 0,
#No se puede "añadir o quitar" elementos en una tupla



-----------------------------------------------------------------------
Exercise 0: Muestra el tipo de dato de la tupla y sus distintas maneras de escribirla

settings = ("localhost","5500",True)
numeros = 1, 2, 3, 4, 5
numero = 0,

print(type(settings))
print(numeros)
print(numero)
print(type(numeros))
print(type(numero))
---------------------------------------------------------------

Exercise 1: Imprime las posiciones de las duplas con número positivos y negativos
settings = ("localhost","5500",True)

print(settings[0])
print(settings[1])
print(settings[2])
print("--------------")
print(settings[-1])
print(settings[-2])
print(settings[-3])
print("--------------")

-------------------------------------------------------------------------------------------

Exericise 2: Desempaquetado de Tuplas

animales= ("perro","gato","Pez","perico","liebre","tortuga")

#   ESTO:
#var1 = animales[0]
#var2 = animales[1]
#var3 = animales[2]
#var4 = animales[3]
#var5 = animales[4]

# ES LO MISMO QUE ESTO: "Desempaquetado de Tuplas"
#var1,var2,var3,var4,var5 = animales[0],animales[1],animales[2],animales[3],animales[4]
#var1,var2,var3,var4,var5 = animales

------------------------------------------------------------------------------------------------

Exercise 3: Omite valores y agrupa el desempaquetado 

animales= ("perro","gato","Pez","perico","liebre","tortuga")

#Omitiendo valores
#var1,_,var3,var4,_ = animales

#Agrupando un desempaquetado
#var1,var2,*restoAnimales = animales

#Agrupando un desempaquetado
var1,var2,*restoAnimales,_,var3 = animales

print(var1,var2,restoAnimales,var3)

--------------------------------------------------------------------

Exercise 4: empareja elemento por elemento, 

alumnos = ["ric","Hugo","Peralta"]
cursos = ("python","ruby","js")
calificacion = [10,9,8]

notas = list(zip(alumnos,cursos,calificacion))
print(notas)


#ZIP(): empareja elemento por elemento 
#("mex", "localhost")
#("usa", "5500")
#("canada", True)

#LIST(): Convierte ese objeto iterable en una lista real:
# respuesta = [
#     ("mex", "localhost"),
#     ("usa", "5500"),
#     ("canada", True)
# ]




"""