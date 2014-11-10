'''  aulas.py

     Ao iniciar a aula execute este arquivo no seu computador e compartilhe
     a URL com os alunos.

     Tiago Maluta <tiago.maluta@gmail.com>
'''
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import socket
import glob
import os
import codecs

lessons = ["Aula1","Aula2"]
pyfiles = []
pyfiles_len = []

html = ""
preface = '''<!DOCTYPE html>
            <html>
              <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <meta name="description" content="Programaê">
                <meta name="author" content="Tiago Maluta">
                <link rel="icon" href="../../favicon.ico">

                <title>Programaê - Introdução ao Python</title>

                <!-- Bootstrap core CSS -->
                <link href="web/bootstrap.min.css" rel="stylesheet">

                <!-- Custom styles for this template -->
                <link href="web/sticky-footer.css" rel="stylesheet">

              </head>

              <body>

            <!-- Begin page content -->
            <div class="container">
            <div class="page-header">
            <h1>Python - Aulas</h1>
            </div>
            <p class="lead">Exercícios referentes as aulas</p>


           '''

suffix = '''
            </div>
            <div class="footer">
            <div class="container">
              <p class="text-muted">http://www.programae.org.br</p>
            </div>
            </div>


            <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
            <script src="web/ie10-viewport-bug-workaround.js"></script>

            <script src="web/jquery.min.js"></script>
            <script src="web/bootstrap.min.js"></script>
            </body>
            </html>
        '''


html = preface

for i in lessons:
    os.chdir(i)
    p = glob.glob("*py")
    pyfiles.append(p)
    pyfiles_len.append(len(p))
    os.chdir("../")

pyfiles_len.reverse()
html += '<div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">'

for files in zip(lessons,pyfiles):
    s_m = '<ul class="list-group">'
    for f in files[1]:
        if "resposta" in f:
            pass
        else:
            s_m += '<li class="list-group-item"><a href="{1}/{0}">{0}</a></li>'.format(f,files[0])
    s_i = '''
            <!-- -->
            <div class="panel panel-default">
            <div class="panel-heading" role="tab" id="heading_{0}">
            <h4 class="panel-title">
              <a data-toggle="collapse" data-parent="#accordion" href="#collapse_{0}" aria-expanded="false" aria-controls="collapse_{0}">
                {0}
              </a>
            </h4>
            </div>
            <div id="collapse_{0}" class="panel-collapse collapse" role="tabpanel" aria-labelledby="heading_{0}">
            <div class="panel-body">'''.format(files[0])
    s_m += '</ul>'

    s_f = '''
             </div>
             </div>
             </div>
             <!-- -->'''

    html += s_i
    html += s_m
    html += s_f

html += '    </div>'
html += suffix

with codecs.open('index.html','w',encoding='utf8') as f:
    f.write(html)

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
