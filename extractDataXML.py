import xml.etree.ElementTree as ET
import pandas as pd
import os


def obter_arquivos_xml(diretorio):
    global ret
    ret = []
    for arq in os.listdir(diretorio):
        if arq.endswith('.xml'):
            ret.append(os.path.join(diretorio, arq))

def arqsXML():
    identificacao = Minfra = secao = tipo_documento = data = publciacao =None
    listaDic = []
    dic = {
        'orgao': Minfra,
        'secao': secao,
        'tipo_documento': tipo_documento,
        'texto': publciacao,
        'identificacao': identificacao,
        'data': data
    }
    i = 0
    while i < len(ret):
        doc = ET.parse(ret[i])
        root = doc.getroot()

        for categ in root:
            tipo_documento = categ.attrib['artType']
            secao = categ.attrib['pubName']
            data = categ.attrib['pubDate']
            orgao = categ.attrib['artCategory']

            dic['secao'] = secao
            dic['tipo_documento'] = tipo_documento
            dic['data'] = data

            if 'Ministério da Infraestrutura/' in orgao:
                Minfra = orgao
                dic['orgao'] = orgao

                for identifica in root.iter('Identifica'):
                    identificacao = identifica.text
                    dic['identificacao'] = identificacao

                for info in root.iter('Texto'):
                    texto = info.text
                    publciacao = texto.replace('<p class="identifica">', ' ').replace('</p><p class="ementa">', ' ').replace('</p><p>', ' ').replace('</p><p class="assina">', ' ').replace('</p><p class="cargo">', ' - ')[:-4]
                    dic['texto'] = publciacao


        csvXml = pd.DataFrame({'Orgão': [Minfra], 'Identificação': [identificacao],
                               'Tipo Documento ': [tipo_documento], 'Seção': [secao],
                               'Data': [data], 'Texto': [publciacao]})

        listaDic.append(dic)

        df = pd.DataFrame(csvXml, columns=['Orgão', 'Identificação', 'Tipo Documento', 'Seção', 'Data', 'Texto'])
        df.to_csv('DouSecao1.csv', sep=';', encoding='utf-8')
        print(df)
        i += 1

obter_arquivos_xml('C:\\Users\\reinan.oliveira\\Downloads\\2020-02-28-DO1')
arqsXML()
