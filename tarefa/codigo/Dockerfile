# imagem base
FROM python:3.8-slim
#FROM centos/python-36-centos7

# copia tudo dentro do contexto para o diretorio /codigo dentro do container
COPY  . /codigo

# seta o /codigo como diretorio base
WORKDIR /codigo

# instala as dependencias do python
RUN pip install -r requirements

# comando rodado ao iniciar o container
CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]







