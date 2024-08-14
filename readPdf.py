import os
import csv
from PyPDF2 import PdfReader

import employees


def get_complete_path(path):
  current_dir = os.path.dirname(__file__)
  return os.path.join(current_dir, path)


if __name__ == "__main__":

  # Criar um objeto de leitura do PDF
  reader = PdfReader('./contra_cheques/Contra-Cheque.pdf')

  # Número da página que você deseja ler as informações
  page_number = 1

  number_of_pages = len(reader.pages)

  funcionarios = []

  for page in reader.pages:
    page_text = page.extract_text()
    lines = page_text.split("\n")

    line_with_name_employee = lines[2]
    parts = line_with_name_employee.split()
    name = parts[0] + " " + parts[-3] #" ".join(parts[:-2])
    code = employees.found_codigo_by_nome(name) #parts[-2]
    salario_liquido=0
    for line in lines:

      if line.__contains__("LÍQUIDO"):
        if line.startswith("VALOR LÍQUIDO"):
          salario_liquido = line.split(" ")[2]
        elif line.startswith(" ____ /"):
          temp = line.split("LÍQUIDO")[1]
          salario_liquido = temp.strip().split(" ")[0]
          break
        else:
          salario_liquido = "ERROR"
        break
    
    funcionarios.append({"code": code if code else "###", "name": name, "salario_liquido": salario_liquido})

  print(funcionarios)

  with open('funcionarios.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["code", "name", "salario_liquido"], delimiter=';')
        writer.writeheader()
        for funcionario in funcionarios:
            writer.writerow(funcionario)


  # Obter a página do número da página selecionada
  #page = reader.pages[0]



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