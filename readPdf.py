import os
from PyPDF2 import PdfReader

import employees


def get_lista_comprovantes():
  return os.listdir(get_complete_path("comprovantes"))

def get_complete_path(path):
  current_dir = os.path.dirname(__file__)
  return os.path.join(current_dir, path)

def get_favorecido_from_comprovante(filename):
  if not filename.endswith(".pdf"):
    return None
  
  comprovante_path = get_complete_path("comprovantes")
  file = os.path.join(comprovante_path, filename)
  reader = PdfReader(file)
  page = reader.pages[0]
  page_text = page.extract_text()
  lines = page_text.split("\n")
  favorecido = ""

  for line in lines:
    x = line.split(":")
    if x and x[0] == "FAVORECIDO":
      temp = x[1].strip().split(" ")
      favorecido = temp[0] # first name
      break
  
  return favorecido

if __name__ == "__main__":
  comprovante_list = get_lista_comprovantes()

  for comprovante_filename in comprovante_list:
    favorecido = get_favorecido_from_comprovante(comprovante_filename)
    print(favorecido)

# Criar um objeto de leitura do PDF
reader = PdfReader('./contra_cheques/contra_cheque.pdf')

# Número da página que você deseja ler as informações
page_number = 1

number_of_pages = len(reader.pages)

# Obter a página do número da página selecionada
page = reader.pages[0]

# Ler o conteúdo do texto da página
page_text = page.extract_text()


# Conteudo do pdf em array
lines = page_text.split("\n")

line_with_name_employee = lines[2]
parts = line_with_name_employee.split()
name = parts[0] + " " + parts[-3] #" ".join(parts[:-2])
code = employees.found_codigo_by_nome(name) #parts[-2]



#for idx, line in enumerate(lines, start=0):
#  print(f"{idx}: {line}")
'''
line_dados_funcionario = lines[2].strip().split(" ")
print(line_dados_funcionario)

codigo_funcionario = line_dados_funcionario[len(line_dados_funcionario)-2].zfill(3)
nome_funcionario = line_dados_funcionario[0]

salario = lines[19].strip().split(" ")[2]
print(salario)
'''