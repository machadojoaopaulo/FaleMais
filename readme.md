Para rodar o projeto executar as etapas a seguir:
 - pip3 install mysql-connector-python
 - docker build -t telzir .
 - docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123mudar -e MYSQL_DATABASE=TELZIR -e MYSQL_USER=telzir -e MYSQL_PASSWORD=123mudar telzir
 - python main.py

O banco de dados será automaticamente populado durante a subida do docker