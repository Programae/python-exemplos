# Compartilhe arquivos na rede local
# Utilize este script para compilhar arquivos com as máquinas do laboratório.
#
# Como utilizar?
# 1. Copie o arquivo compartilhar.py para a pasta onde você quer disponibilizar
# 2. Execute o programa e espere o browser iniciar
# 3. Pegue o endereço da URL e compartilhe com os alunos

from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("programae.org.br",80))
ip = s.getsockname()[0]
s.close()

httpd = HTTPServer((ip, 5000), SimpleHTTPRequestHandler)

webbrowser.open_new("http://" + ip + ":5000")
httpd.serve_forever()
