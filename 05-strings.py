"""
Exercise 1: Probar inmutabilidad en strings
NOTAS:
-Los strings son inmutables, puedes cambiar el dato pero no el espacio de memoria 
ESTO SE PUEDE:
message = "hola mundo"
message = 2

ESTO NO SE PUEDE:
message = "hola mundo"
message[0] = "k"

no modificaste el string, "creaste uno nuevo y lo reasignaste"

texto = "me llamo "
texto = texto + "ric"
print(texto)

Regla de oro
❌ No puedes cambiar un string existente
✔️ Sí puedes crear uno nuevo y reasignar la variable

---------------------------------------------------------------
Exercise 1: Preguntar si el caracter dentro de una variable existe

name = "ric!"
print("!" in name)
-----------------------------------------------------------------

Exercise 2: Encontrar el indice de un caracter de texto en una variable
name = "ric!"
print(name.index("!"))

----------------------------------------------------------------------
Exercise 3: Muestra el penultimo caracter de una variable
name = "ric!"
print(name[-2])

---------------------------------------------------------------------------
Exercise 4: Recorta la primer palabra de tu texto en la variable sin utilizar una función
name = "ric!"
print(name[0:2])

------------------------------------------------------------------------------------------
Exercise 5: Concatena un texto con una variable
name = "ric!"
print("hola " + name)

--------------------------------------------------------------------
Exercise 6: Corta un pedazo del texto de una variable y usalo en una variable nueva, luego concatena esa nueva variable con un texto
name = "hola ric!"
nueva_variable = name[0:4]
print(nueva_variable + " fulanito")

------------------------------------------------------------------------------
Exercise 7:



"""
