'''
  COMPARTILHE ARQUIVO NA REDE LOCAL

  Utilize este script para compilhar arquivos entre as máquinas do laboratório.

  Pré-requisito: ter o Python 3.x instalado na máquina

  Como utilizar?
  1. Copie o arquivo "compartilhar.py" para a pasta onde você quer compartilhar
     os arquivos.
  2. Duplo clique no arquivo "compartilhar.py" e espere o navegador iniciar.
  3. Pegue o endereço da URL e compartilhe com os alunos.

  Importante:

  - Este endereço só é válido na rede local
  - Se você fechar o programa o compartilhamento irá parar
  - Se você constatar problemas de acentuação nos arquivos verifique a codificação
    da página. TODOS os arquivos .py são codificador em UTF-8.

    Se tiver algum problema escreva para:
    Tiago Maluta <tiago.maluta@gmail.com>
'''
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import socket

try:
    ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
except:
    print("*** VERIFIQUE SUA CONEXÃO COM A INTERNET ***")
    ip = socket.gethostbyname(socket.gethostname())

print("Compartilhe o seguinte endereço:")
print("+---------------------------+")
print(" http://" + ip + ":5000")
print("+---------------------------+")

httpd = HTTPServer((ip, 5000), SimpleHTTPRequestHandler)

# abre o navegador
webbrowser.open_new("http://" + ip + ":5000")

try:
    httpd.serve_forever()
except:
    print("OOPS... aconteceu algum erro na inicialização!")
    print("Verifique com a equipe do Programaê!")
    print("http://programae.org.br")
