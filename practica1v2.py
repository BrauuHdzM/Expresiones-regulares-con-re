##Braulio Hernández Minutti
##Procesamiento de lenguaje natural. Escuela Superior de Cómputo. 7CM1
##Profesor: Dr. Joel Omar Juarez Gambino
##Práctica 1: Expresiones regulares

import pandas as pd
import re

#Leer el archivo tweets 1.txt
df = pd.read_csv('tweets 1.txt', sep='\t', header=None)

#Expresión regular para los hashtags
patronHashtags = re.compile(r'#\w+')
busquedaHashtags = df[1].str.findall(patronHashtags)
hashtagsEncontrados = busquedaHashtags.sum()
cantHashtags = busquedaHashtags.str.len().sum()
#print(hashtagsEncontrados)
print("Cantidad de hashtags: ", cantHashtags)

#Expresión regular para los usuarios
patronUsuarios = re.compile(r'@[^\W][\w.]{0,16}[^\W]')
busquedaUsuarios = df[1].str.findall(patronUsuarios)
usuariosEncontrados = busquedaUsuarios.sum()
cantUsuarios = busquedaUsuarios.str.len().sum()
#print(usuariosEncontrados)
print("Cantidad de usuarios: ", cantUsuarios)

#Expresión regular para las horas
patronHoras = re.compile(r'(0?[1-9]|1[0-2])(:[0-5][0-9])?\s*(am|pm)')
busquedaHoras = df[1].str.findall(patronHoras)
horasEncontradas = busquedaHoras.sum()
cantHoras = busquedaHoras.str.len().sum()
#print(horasEncontradas)
print("Cantidad de horas: ", cantHoras)

#Expresión regular para las fechas
patronFechas = re.compile(r'(\b\d{4}(?![\w-])\b)|\b(ene(?:ro)?|feb(?:rero)?|mar(?:zo)?|abr(?:il)?|mayo?|jun(?:io)?|jul(?:io)?|ago(?:sto)?|sep(?:tiembre)?|oct(?:ubre)?|nov(?:iembre)?|dic(?:iembre)?)\b')
busquedaFechas = df[1].str.findall(patronFechas)
fechasEncontradas = busquedaFechas.sum()
cantFechas = busquedaFechas.str.len().sum()
#print(fechasEncontradas)
print("Cantidad de fechas: ", cantFechas)

#Expresión regular para los emojis con unicode
patronEmojis = re.compile(r'[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F1E0-\U0001F1FF]')
busquedaEmojis = df[1].str.findall(patronEmojis)
emojisEncontrados = busquedaEmojis.sum()
cantEmojis = busquedaEmojis.str.len().sum()
#print(emojisEncontrados)
print("Cantidad de emojis: ", cantEmojis)

#Expresión regular para los emojis con ASCII
patronEmojisASCII = re.compile(r'[:;=x][-^]?[)DPpcvxsSuIX\]\(\{@\|\\\/oO3\*]')
busquedaEmojisASCII = df[1].str.findall(patronEmojisASCII)
emojisASCIIEncontrados = busquedaEmojisASCII.sum()
cantEmojisASCII = busquedaEmojisASCII.str.len().sum()
#print(emojisASCIIEncontrados)
print("Cantidad de emojis ASCII: ", cantEmojisASCII)

