Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def numeroPrimo(numero):
    primo = True
    for num in range(2, numero):
        if numero % num == 0:
            primo = False
            break
        if primo: return("El numero es primo")
        else: return("El numero no es primo")

        
print(numeroPrimo(3))
El numero es primo
