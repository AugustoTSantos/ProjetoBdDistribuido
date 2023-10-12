# python3 version
import rsa

print('\\-------------------------------//')
print('**Prj Banco de Dados Distribuidos**')
print('\\-------------------------------//')
print('Cifrador de mensagens')
print('Digite as seguintes informacoes')

# pergunta lugar onde ele vai buscar a chave publica
arqnomepub = input('Endereco da chave publica (c:\chaves\myPub.txt): ')
# escreve a mensagem a ser cifrada
msg = input('Mensagem a ser cifrada: ').encode('utf-8')
# lugar onde a msg vai ser salva e seu nome
arqnomemsg = input('Endereco e nome da mensagem (c:\msg.txt): ')

# abro o arquivo com a chave
arq = open(arqnomepub,'rb')
# carrego a chave e salva em txt
txt = arq.read()
# fecho o arquivo
arq.close()

#decodifico para o formato expoente e modulo
pub = rsa.PublicKey.load_pkcs1(txt, format='PEM')

#cifro a msg
msgc = rsa.encrypt(msg,pub)

#salvo a msgc no arquvio
arq = open(arqnomemsg,'wb')
# escreve a mensagem cifrada
arq.write(msgc)
# fecha o arquivo
arq.close()

# printa local da mensagem salva
print('Mensagem cifrada no arquivo ' + arqnomemsg)
