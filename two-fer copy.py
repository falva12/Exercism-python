
#def to_camel_case(text):
import re
text = 'flavia_kpa-ghg'
palabras = re.split('-|_', text)

cant_palabras = len(palabras)
camel_case = []

for i in range(cant_palabras):
    if i==0: camel_case.append(palabras[i])
    else : camel_case.append(palabras[i].capitalize())

camel_case = ''.join(camel_case)
print(camel_case)