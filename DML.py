import re
#Porciento
cadena="""Estos datos positivos también tienen su correlación con la salud. La tasa de
mortalidad entre los recién nacidos era de 64,8 por cada 1.000 en 1990. Pero
en 2016, la realidad era bien diferente, ya que solo 30,5B fallecían por cada 1.000
(en 26 años se ha reducido un 53%). Igual de positivo es la caída de la mortalidad
entre los menores de 5A; en 26 años se ha pasado de una tasa de 93,4 fallecidos
por 1.0E2 a un 40,8 (una reducción del 56%).
De igual manera, el número de mujeres que fallece durante el parto también ha
decrecido (en 1990 el número de muertes fue de 532.000 y en 2015 de 303.00.0,
una disminución del 43%)."""
#print(cadena)
#print("Introduzca texto")
#cadena = input()
lines =cadena.split("\n")
print("Number of lines is {}".format(len(lines)))
#cuenta lineas
sub_cadena= re.search(r"\d*%", cadena)
#clear
# print(sub_cadena.group())
palabra=sub_cadena.group()

sub_cadena= re.findall(r"[\d\d,\d]*[\d.\d\d\d]*[\d\d.\d*[A-B]*[\dE\d]*[\d*%+-]", cadena)

for chain in sub_cadena:
    for i,line in enumerate(lines):
        if chain in line: 
            print("No de linea:\"{}\" Cadena {}".format(i+1,chain)) 
            break
    #dice que linea es



