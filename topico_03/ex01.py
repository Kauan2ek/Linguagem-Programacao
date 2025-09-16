# Escreva um programa que cadastre o estado civil 
# de uma pessoa, entretanto, o programa deve continuar
# perguntando enquanto o valor informado for diferente 
# de "solteiro" ou "casado".
estado_civil = None

while(estado_civil != 'solteiro' and estado_civil != 'casado'):
    estado_civil = input('Estado Civil: ').lower()
    print(estado_civil)