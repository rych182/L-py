"""
METODOS

split   -> string a lista (puedes indicarle a partir de que caracter de texto quieres cortar)
join    -> lista a string    

%s  -> (se usa mucho para los logs, cuando queremos saber que paso en el servidor y en que momento)

f string(FORMA MAS ACTUAL Y RECOMENDADA) -> Permite la "interpolacion"(osea permite poner llaves con nombres de variables)

parametro sep: sirve para separar datos de variables 
ejemplo:
print("texto",var1,var2,sep="") 

----------------------------------
Exercise 1: cortar un texto y convertirlo en lista con split
name = "Ricardo Garrido Cruz"
nombre_cortado= name.split()
print(nombre_cortado)

-------------------------------------------
Exercise 2: cortar un texto y convertirlo en lista con split pero indicandole donde cortar
NOTA: dejo un espacio después de la "coma" para que no se guarde en la lista con un espacio "al inicio"
texto = "Hola! Mi nombre es Ricardo, vivo en cuernavaca, soy programador, tengo 39 años, estoy casado y soy mexicano."
texto_cortado= texto.split(",")
print(texto_cortado)

----------------------------------------------------
Exercise 3: Convierte una lista a texto y separalo
NOTA: poner las comillas de string antes de la función "join", nos sirve como separador,
le puedes poner una COMA, un ESPACIO o AMBOS y la "lista" dentro de la función

cursos = ["ruby","python","sql","html","css"]
lista = ", ".join(cursos)
print(lista)

-----------------------------------------------------------------
Exercise 4: Concatena un entero y un texto
name= "ric"
numero = 2
concatenar = name + str(numero)
print(concatenar)

--------------------------------------------------------------------------
Exercise 5: Concatena 2 variables usando el metodo "join"

name= "ric"
last_name = "garrido"
concatenar = " ".join([name,last_name])
print(concatenar)

-----------------------------------------------------------------------------
Exercise 6: concatena dos textos sin usar una funcion ni signo de "+"
genera un valor dinamico con 2 strings

name= "ric"
last_name = "garrido"

full_name = '%s %s' %(name,last_name)
print(full_name)
------------------------------------------------

Exercise 7: Agregar valores a un string de forma dinámica
name= "ric"
last_name = "garrido"
full_name = 'El nombre completo es: {} {}'
agregando_datos = full_name.format(name,last_name)
print(agregando_datos)

----------------------------------------------------------

Exercise 8: Agrega un dato al ejercicio anterior sin usar una variable

name= "ric"
last_name = "garrido"
full_name = 'El nombre completo es: {} {}. Mi edad es {}'
agregando_datos = full_name.format(name,last_name, 39)
print(agregando_datos)

----------------------------------------------------------

Exercise 9: has un programa que te pregunte, nombre, apellidos, edad y que los guarde en una 
variable que los imprima junto con un texto


name= input("¿Cómo te llamas? ")
last_name = input("¿Cuál es tu apellido? ")
age= input("¿Cuál es tu edad? ")
full_name = 'El nombre completo es: {} {}. Mi edad es {}'
agregando_datos = full_name.format(name,last_name,age)
print(agregando_datos)

----------------------------------------------------------

Exercise 10: imprime un texto usando "f strings"

name= "ric"
last_name ="garrido"
texto = f"Hola mi nombre es {name} {last_name}"
print(texto)

-----------------------------------------------------------
Exercise 11: has una operación en un f string
texto = f"El resultado es: {10+10}"
print(texto)

----------------------------------------------------

Exercise 12: utiliza el parametro "sep" para separar un texto

"""

name = "Ric"
apellido = "Garrido"
print("Mi nombre completo es: ",name,apellido, sep="...")