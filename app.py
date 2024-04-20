"""""
Importando as bibliotecas necessárias
"""""
import openpyxl
from PIL import Image, ImageDraw, ImageFont

# Carregando o arquivo de planilha do Excel e selecionando a planilha
workbook_alunos = openpyxl.load_workbook('./planilha/planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']

# Iterando sobre cada linha na planilha
for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):

    # Extraindo os dados da linha atual
    nome_curso = linha[0].value
    nome_participante = linha[1].value
    tipo_participacao = linha[2].value
    data_inicio = linha[3].value
    data_final = linha[4].value
    carga_horaria = linha[5].value
    data_emissao = linha[6].value

    # Configurando as fontes para renderização de texto
    fonte_nome = ImageFont.truetype('./fontes/tahomabd.ttf', 90)
    fonte_geral = ImageFont.truetype('./fontes/tahoma.ttf', 80)
    fonte_data = ImageFont.truetype('./fontes/tahoma.ttf', 55)

    # Abrindo a imagem do certificado modelo
    image = Image.open('./certificado/certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(image)

    # Desenhando texto na imagem do certificado
    desenhar.text((1020, 825), nome_participante,
                  fill='black', font=fonte_nome)

    desenhar.text((1080, 955), nome_curso, fill='black', font=fonte_geral)

    desenhar.text((1445, 1070), tipo_participacao,
                  fill='black', font=fonte_geral)

    desenhar.text((1500, 1190), str(carga_horaria),
                  fill='black', font=fonte_geral)

    desenhar.text((750, 1770), data_inicio,
                  fill='blue', font=fonte_data)

    desenhar.text((750, 1930), data_final,
                  fill='blue', font=fonte_data)

    desenhar.text((2200, 1930), data_emissao,
                  fill='black', font=fonte_data)

    # Salvando a imagem do certificado modificado
    image.save(f'./resultado/{indice}_{nome_participante}_certificado.png')
