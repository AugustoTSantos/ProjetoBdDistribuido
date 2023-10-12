#python3 version
# importa o que é usada para en e des critografar
import rsa

print ('\\-------------------------------//')
print (' **Prj Banco de Dados Distribuidos**')
print (' \\-------------------------------//')
print ('Gerador de chaves assimetricas')
print ('Digite as seguintes informacoes')

# tamanho 512 ou maior
size = input('Tamanho da chave: ')
# define onde vão ser geradas as chaves
end = input('Endereco do arquivo (c:\chaves\): ')
# define qual vai ser o nome das chaves
nome = input('Nome do arquivo: ')

# gero as chaves com o tamanho informado
(pub,pri) = rsa.newkeys(int(size))

##crio o arquivo pub
arqnomepub = end + nome + 'Pub.txt'
#codifico o exponente e modulo da chave para o formate PEM
arq = open(arqnomepub,'wb')
# muda e escreve a chave no formato PEM
arq.write(pub.save_pkcs1(format='PEM'))
# fecha o arquivo
arq.close()

##crio o arquivo pri
arqnomepri = end + nome + 'Pri.txt' 
# abre o arquivo
arq = open(arqnomepri,'wb')
##codifico o exponente e modulo da chave para o formate PEM
arq.write(pri.save_pkcs1(format='PEM'))
# fecha o arquivo
arq.close()

print ('Chaves geradas com sucesso')
# printa a chave publica
print (arqnomepub)
# printa a chave privada
print (arqnomepri)
