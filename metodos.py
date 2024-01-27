#Metodo Capitalize
texto = "Hola mundo"
resultado = texto.capitalize()
print(resultado)

#Metodo find
texto = "Hola mundos"
resultado2 = texto.find("m")
print(resultado2)

#Metodo center (centra el texto en un conjunto de resultados)
texto = "Hola mundose"
resultado3 = texto.center(20,'?')
print(resultado3)

#Metodo isalnum() Devuelve True si todos los carecteres de la cadena son alfanumericos
texto4 = "Python12345"
resultado4 = texto4.isalnum()
print(resultado4)

#Metodo isdigt() Devuelve True si todos los caracteres de la cadena son digitos
texto5 = "2345"
resultado5 = texto5.isdigit()
print(resultado5)

#Metodo islower Devuelve True si todos los caracteres de la cadena estan en miniscula
texto6 = "asadfdsf"
resultado6 = texto6.islower()
print(resultado6)

#Metodo isspace() Devuelve True si todos los caracteres de la cadena son espacios en blanco
texto7 = "          "
resultado7 = texto7.isspace()
print(resultado7)