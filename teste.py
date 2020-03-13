import xml.etree.ElementTree as ET
import csv
import os

informacoes = []
def obter_arquivos_xml(diretorio):
    global ret
    ret = []
    for arq in os.listdir(diretorio):
        if arq.endswith('.xml'):
            ret.append(os.path.join(diretorio, arq))

def arqsXML():
    identificacao = minfra = secao = tipo_documento = data = publciacao = None

    i = 0
    while i < len(ret):
        doc = ET.parse(ret[i])
        root = doc.getroot()

        for categ in root:
            orgao = categ.attrib['artCategory']

            if 'Ministério da Infraestrutura/' in orgao:
                minfra = orgao
                tipo_documento = categ.attrib['artType']
                secao = categ.attrib['pubName']
                data = categ.attrib['pubDate']

                for identifica in root.iter('Identifica'):
                    identificacao = identifica.text

                for info in root.iter('Texto'):
                    texto = info.text
                    publciacao = texto.replace('<p class="identifica">', ' ').replace('</p><p class="ementa">', ' ').replace('</p><p>', ' ').replace('</p><p class="assina">', ' ').replace('</p><p class="cargo">', ' - ')[:-4]

                    informacoes.append(minfra)
                    informacoes.append(identificacao)
                    informacoes.append(tipo_documento)
                    informacoes.append(secao)
                    informacoes.append(data)
                    informacoes.append(publciacao)

                '''print(minfra)
                print(identificacao)
                print(tipo_documento)
                print(secao)
                print(data)
                print(publciacao)
                print('--------------------------------------')'''


        i += 1

obter_arquivos_xml('C:\\Users\\reinan.oliveira\\Downloads\\2020-02-28-DO1')
arqsXML()

for n, item in enumerate(informacoes):
    x1 = informacoes[n]
    x2 = informacoes[n+1]
    x3 = informacoes[n+2]
    x4 = informacoes[n+3]
    x5 = informacoes[n+4]
    x6 = informacoes[n+5]

    print(x1)
    print(x2)
    print(x3)
    print(x4)
    print(x5)
    print(x6)
    print()

'''a = 0
while a < len(informacoes):
    csv.register_dialect('myDialect', delimiter=';')
    with open('totalComentario.csv', 'w', newline='', encoding='windows-1252',
              errors='ignore') as saida:  # iso-8859-1  windows-1252  utf-8
        escrever = csv.writer(saida, dialect='myDialect')
        escrever.writerow(['Orgão', 'Identificação', 'Tipo Documento', 'Seção', 'Data', 'Texto'])
        for i, item in enumerate(informacoes):
            escrever.writerow([informacoes[a], informacoes[a+1], informacoes[a+2], informacoes[a+3], informacoes[a+4], informacoes[a+5]])
    a+=6
'''