import csv
import unicodedata
import re

def found_codigo_by_nome(employee_name):
  with open('employees.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        nome_completo = remover_caracteres_especiais_e_acentos(row['NOME COMPLETO'].strip().upper())
        temp = nome_completo.split(" ")
        first_last_name = temp[0]  + " " + temp[-1]
        if first_last_name == remover_caracteres_especiais_e_acentos(employee_name).upper():
            codigo = row['CODIGO']
            codigo_com_zeros = codigo.zfill(3)
            return codigo_com_zeros
  return None

def remover_caracteres_especiais_e_acentos(texto):
    texto_sem_acentos = ''.join(
        letra for letra in unicodedata.normalize('NFD', texto)
        if unicodedata.category(letra) != 'Mn'
    )
    texto_sem_especiais = re.sub(r'[^a-zA-Z0-9\s]', '', texto_sem_acentos)
    
    return texto_sem_especiais
