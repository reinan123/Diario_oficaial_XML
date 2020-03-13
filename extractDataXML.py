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
        i += 1


obter_arquivos_xml('caminho da pasta')
arqsXML()

n = 0
while n < len(informacoes):

    csv.register_dialect('myDialect', delimiter=';')
    with open('DouSecao1.csv', 'w', newline='', encoding='windows-1252', errors='ignore') as saida:  # iso-8859-1  windows-1252  utf-8
        escrever = csv.writer(saida, dialect='myDialect')
        escrever.writerow(['Orgão', 'Identificação', 'Tipo Documento', 'Seção', 'Data', 'Texto'])
        while n < len(informacoes):
            escrever.writerow(
                [informacoes[n], informacoes[n + 1], informacoes[n + 2], informacoes[n + 3], informacoes[n + 4], informacoes[n + 5]])
            n += 6
    n += 6
