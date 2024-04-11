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
      favorecido = f"{temp[0]} {temp[-1]}" # first and last name
      break
  
  return favorecido

def rename_comprovante(actual_name, new_name):
  comprovante_path = get_complete_path("comprovantes")
  actual = os.path.join(comprovante_path,actual_name)
  novo = os.path.join(comprovante_path,new_name)
  os.rename(actual,novo)

if __name__ == "__main__":
  comprovante_list = get_lista_comprovantes()

  for comprovante_filename in comprovante_list:
    favorecido = get_favorecido_from_comprovante(comprovante_filename)
    if favorecido:
      codigo = employees.found_codigo_by_nome(favorecido)
      rename_comprovante(comprovante_filename, f"{codigo}-{favorecido}-pagamento.pdf")
