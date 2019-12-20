#Imports
import unidecode

ini = #Informar aqui o caminho completo do arquivo ex.: c:\arquivo.txt

#Abre o arquivo indicado
arq = open(ini,'r',encoding='utf-8').readlines()

#Remove caracteres especiais
dec = [unidecode.unidecode(linhas) for linhas in arq]

#Cria novo arquivo no formato ANSI
arq2 = open(ini.replace('.csv','_U.txt'), 'w',encoding='iso-8859-1')

#Escreve as linhas no novo arquivo
arq2.writelines(dec)

#Fecha arquivo
arq2.close()
