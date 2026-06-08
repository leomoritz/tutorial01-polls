# Tutorial 01 - Django Polls com Docker

Este repositorio prepara um ambiente de desenvolvimento para seguir o Tutorial 01 do Django:

- https://docs.djangoproject.com/pt-br/6.0/intro/tutorial01/

## Objetivo

Executar uma aplicacao Django dentro de container Docker usando Docker Compose, com inicio rapido para desenvolvimento local.

## Stack

- Python 3.14 (imagem `python:3.14-slim`)
- Django 6.0.x
- Docker Compose

## Pre-requisitos

- Docker instalado
- Docker Compose habilitado (`docker compose`)

## Como subir o ambiente

Na raiz do projeto, execute:

```bash
docker compose up --build
```

Depois abra no navegador:

- http://localhost:8000

## O que acontece na primeira execucao

Ao iniciar o container `web`, o comando de entrada:

1. Cria o projeto Django `mysite` caso `manage.py` ainda nao exista.
2. Executa `python manage.py migrate`.
3. Inicia o servidor de desenvolvimento em `0.0.0.0:8000`.

## Comandos uteis

Criar o app `polls` (tutorial):

```bash
docker compose exec web python manage.py startapp polls
```

Criar novas migracoes:

```bash
docker compose exec web python manage.py makemigrations
```

Aplicar migracoes:

```bash
docker compose exec web python manage.py migrate
```

Criar superusuario:

```bash
docker compose exec web python manage.py createsuperuser
```

Parar os containers:

```bash
docker compose down
```

## Estrutura inicial esperada

Depois da primeira subida, voce deve ver arquivos Django gerados na raiz (como `manage.py` e pasta `mysite/`).

## Proximo passo no tutorial

Com o ambiente em pe, siga o tutorial para:

1. Criar views no app `polls`.
2. Configurar URLs do app e do projeto.
3. Testar resposta inicial no navegador.