# Define a imagem base para o contêiner, usando uma imagem oficial do Python 3.14 em versão slim para reduzir o tamanho da imagem final.
FROM python:3.14-slim

# Definindo variáveis de ambiente para evitar a criação de arquivos bytecode e para garantir que a saída do Python seja exibida imediatamente no console.
ENV PYTHONDONTWRITEBYTECODE=1 \ 
    PYTHONUNBUFFERED=1

# Criando um diretório de trabalho dentro do contêiner onde o código da aplicação será armazenado.    
WORKDIR /app

# Atualizando o gerenciador de pacotes e instalando as dependências necessárias para compilar pacotes Python que possam ter componentes nativos. Após a instalação, os arquivos de cache do apt são removidos para reduzir o tamanho da imagem final.
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiando o arquivo de requisitos para o diretório de trabalho do contêiner e instalando as dependências listadas no arquivo usando pip. A opção --no-cache-dir é usada para evitar o armazenamento em cache dos pacotes, o que ajuda a reduzir o tamanho da imagem final.    
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiando todo o conteúdo do diretório atual (que deve conter o código da aplicação Django) para o diretório de trabalho do contêiner. Isso inclui arquivos como manage.py, as pastas de aplicativos Django, templates, etc.
COPY . .

# Expondo a porta 8000, que é a porta padrão usada pelo servidor de desenvolvimento do Django. Isso permite que o contêiner seja acessado externamente através dessa porta.
EXPOSE 8000

# Definindo o comando de entrada para o contêiner. O comando verifica se o arquivo manage.py existe; se não existir, ele cria um novo projeto Django chamado "mysite". Em seguida, ele executa as migrações do banco de dados para garantir que a estrutura do banco de dados esteja atualizada e, finalmente, inicia o servidor de desenvolvimento do Django, ouvindo em todas as interfaces de rede na porta 8000.
CMD ["sh", "-c", "if [ ! -f manage.py ]; then django-admin startproject mysite .; fi && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]