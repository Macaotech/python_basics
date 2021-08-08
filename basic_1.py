'''
Tutorial basico de Python.
'''

'''
Comenzaremos aprendiendo a imprimir texto en la consola.
Para hacerlo vamos a utilizar algo llamado una función.
Python trae muchas funciones por defecto, para imprimir utilizaremos:
'''

print('Bienvenidos al curso basico de Python.')

'''
Si reemplazan el texto entre comillas pueden escribir en la consola lo que ustedes deseen. 
'''

print('Este es otro ejemplo')

'''
La función print puede utilizarse para imprimir diferentes tipos de datos y operaciones.
'''
print(32)
print(True)
print(2+2)

'''
Ahora aprenderemos a guardar datos dentro de Python. Para hacerlo utilizaremos algo llamado 'variable'
hay muchos tipos de variables:
De texto (str)
Numerica (Enteros, flotantes, Complejos)
Booleanos (True or False)
Listas, Tuplas y Diccionarios.
'''

a = 'Soy un texto'
b = 123
c = 1.50
d = 5j

'''
Lo genial de las variables es que pueden ser sobreescritas, y pueden utilizarse para realizar operaciones o en funciones.
Hay multiples operaciones en Python, Logicas y Aritmeticas.
Las operaciones logicas son: and, or, ==, >, <, >=, <=, in, not in, is
Existen tambien operadores binarios, pero eso no lo tocaremos en este taller basico.
Los operadores aritmeticos inluyes: +, -, *, /, %, etc.
La "Libreria" de funciones matematica incluye muchos mas.
'''

a = 3
b = 4
print(a+b)

'''
Si quisieramos pedirle a un usuario que ingrese algo podemos usarlo mediante la funcion input y una variable.
'''
print('Usuario, por favor ingrese una variable.')
mi_variable = input()

'''
Por ultimo aprenderemos lo que son las estructuras de control. Estas nos permiten evaluar condiciones y actuar acorde.
Estas incluyen, if, elif, else, for, while, etc.
En el mundo de la programacion se bromea mucho sobre los puntos y comas, pero en python no los utilizamos. Tampoco utilizamos llaves
como en otros lenguajes de programacion. En lugar de eso utilizamos 'indentacion'.
'''

print('Estamos en la ejecucion principal de codigo')
if True:
    print('Entramos a ejecutar lo que este en la indentacion')
if False:
    print('Esta linea no se mostrara, porque ha sido evaluada como falsa.')
print('Volvemos a la ejecucion principal, linea por linea')

'''
Podemos jugar con las condiciones.
'''

if 2 + 2 == 6:
    print('Denzel Crocker tenia razon!')
elif 2+2 == 5:
    print('Stephen Hawking tenia razon!')
else:
    print('Los Padrinos Magicos no son un buen maestro de matematicas')

contador = 0
while contador < 6:
    print('Hola')
    contador += 1

'''
Vamos a utilizar todo este conocimiento adquirido para construir una calculadora basica!
'''
print('Bienvenidos a mi calculadora.')
while True:
    x = int(input('Ingrese un numero '), 0)
    y = int(input('Ingrese un segundo numero '), 0)
    operacion = input('¿Que operacion desea realizar? ')
    if operacion == 'suma':
        print(x+y)
    elif operacion == 'resta':
        print(x-y)
    elif operacion == 'multiplicacion':
        print(x*y)
    elif operacion == 'division' and y is not 0:
        print(x/y)
    else:
        print('No podemos realizar esta operacion ')
    print('Intente de nuevo ')


'''
¿Porque deberia invertir mi tiempo aprendiendo Python?
Es un lenguaje de programación muy utilizado hoy en dia con diferentes aplicaciones.
Conocerlo puede ayudarte a desarrollar tu cerebro en la parte logico-matematica.
Es un lenguaje muy elegante y sencillo de aprender, pero poderoso en las manos de un programador experto.
'''
