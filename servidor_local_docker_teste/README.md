# Titulo

## Construindo um Contêiner

Estando no mesmo diretorio do arquivo `dockerfile`...

### Via 'manual'

#### Criando um imagem com base no dockerfile

```bash
docker build -t <nome_img> .
```

#### Criando Conteiner

```bash
docker run -d -it --name <nome_contêiner> <nome_img>
```

### Via Docker-Compose

Execute:
```bash
sudo docker compose up --build -d --force-recreate
```

docker exec -it <nome_contêiner> sh

remover conteiners:
docker rm -vf $(docker ps -aq)

remover imagens
docker rmi -f $(docker images -aq)

remover tudo
docker rm -vf $(docker ps -aq) ; docker rmi -f $(docker images -aq)