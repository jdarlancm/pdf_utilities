from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

reader = PdfReader('./Contra-Cheque.pdf')

for page in range(len(reader.pages)):
    writer = PdfWriter('./Contra-Cheque.pdf')
    writer.add_page(reader.pages[page])

    # Ler o conteúdo do texto da página
    page_text = reader.pages[page].extract_text()

    # Conteudo do pdf em array
    lines = page_text.split("\n")

    line_dados_funcionario = lines[2].strip().split(" ")

    codigo_funcionario = line_dados_funcionario[len(line_dados_funcionario)-2].zfill(3)
    nome_funcionario = line_dados_funcionario[0]

    output_filename = '{}-{}-Contra Cheque.pdf'.format(codigo_funcionario,nome_funcionario)
    with open(output_filename, 'wb') as out:
        writer.write(out)

reader.close()