'''
  Compartilhe arquivos na rede local
  Utilize este script para compilhar arquivos com as máquinas do laboratório.

  Como utilizar?
  1. Copie o arquivo compartilhar.py para a pasta onde você quer disponibilizar.
  2. Execute o programa e espere o browser iniciar.
  3. Pegue o endereço da URL e compartilhe com os alunos.
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
