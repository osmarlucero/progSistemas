import re
#Porciento
cadena="""SELECT ANOMBRE, CALIFICACION, TURNO 
FROM ALUMNOS, INSCRITOS, MATERIAS, CARRERAS 
WHERE MNOMBRE=’LENAUT2’ AND TURNO = ‘TM’ 
AND CNOMBRE=’ISC’ AND SEMESTRE=’2020I’ AND CALIFICACION >= 70"""
print(cadena)
print("Introduzca texto")
cadena = input()
lines =cadena.split("\n")
print("Number of lines is {}".format(len(lines)))
#cuenta lineas
#sub_cadena= re.search(r"\d*%", cadena)
#clear
# print(sub_cadena.group())
#palabra=sub_cadena.group()

sub_cadena= re.findall(r"(\bSELECT\b|\bANOMBRE\b|[,=]|\bCALIFICACION\b|\bTURNO\b|\bFROM\b|\bAND\b|\bALUMNOS\b|\bINSCRITOS\b|\bMATERIAS\b|\bCARRERAS\b|\bWHERE\b|\bMNOMBRE\b|\bCONSTANTE\b|\bCNOMBRE\b|[=>]|70|\bSEMESTRE\b)", cadena)
cont=0
for chain in sub_cadena:
    cont+=1
    print("no. {} No de linea:\"{}\" Cadena {}".format(cont,cont,chain)) 
    #dice que linea es  


