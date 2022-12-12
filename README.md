# Test Shaped

Este projeto tem a finalidade de criar uma API Rest simples, utilizando o framework Django Rest Framework.

A API contém duas entidades: Paciente e Exame, a fim de testes.

Para executar o projeto, utilizei o `docker`, com python na versão >3.10.

Execute o comando:
```
docker-compose up -d
```

Após subir a aplicação, acesse: http://localhost:8000/docs

Para criar o banco de dados, execute:
```
docker-compose exec web python manage.py migrate
```

Se necessário, crie um usuário, execute:
```
docker-compose exec web python manage.py createsuperuser
```

Essa aplicação teste possui endpoints de `GET, POST, PUT, PATCH e DELETE`, para cada entidade!



