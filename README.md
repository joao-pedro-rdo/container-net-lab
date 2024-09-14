
# Container Net Lab
## TODO

- [ ] Usar Docker SDK 
  - [ ] Dockerfile e Dockercompos
- [ ] Arrumar o publish de porta
  - [ ] Exibição da porta  

## Descrição:

Este projeto foi desenvolvido para explorar e testar o SDK do Docker usando Python, com o objetivo de facilitar a criação e gerenciamento de containers para testes de ferramentas de redes. A ideia surgiu a partir de uma necessidade nas aulas de redes da faculdade, onde frequentemente é necessário criar diversos containers e realizar testes de conectividade, tráfego e outros aspectos de redes.

A ferramenta possui uma interface gráfica simples e intuitiva, permitindo aos usuários:
- **Criar containers**
- **Apagar containers**
- **Visualizar containers em execução**
- **Visualizar containers parados**
- **Acessar o terminal dos containers ao cria-los**

Tudo isso sem a necessidade de inserir comandos no terminal. O projeto utiliza duas imagens Docker personalizadas, que incluem as principais ferramentas de rede utilizadas em sala de aula, otimizando a experiência de aprendizado e prática.

## Pré-requisitos

- Docker: [Instalação do Docker](https://docs.docker.com/get-docker/)
- Python 3.6 ou superior: [Instalação do Python](https://www.python.org/downloads/)
- Poetry(Recomendado): [Instalação do Poetry](https://python-poetry.org/docs/)

## Execução

Para executar o projeto, siga os passos abaixo:
```bash
poetry install #  Instala as dependências do projeto com poetry
streamlit run __main__.py # Executa a aplicação
```
Abra o navegador e acesse o endereço `http://localhost:8501` para visualizar a aplicação. Ou siga as instruções exibidas no terminal.

## Docker Images
As imagens Docker utilizadas no projeto estão disponíveis no Docker Hub:
[joaoprdo/redes-tools](https://hub.docker.com/repository/docker/joaoprdo/redes-tools/general)

A imagem `redes-tools` contém as seguintes ferramentas:
```bash
iproute2         # Ferramentas para visualização e manipulação de rotas e interfaces
net-tools        # Ferramentas como ifconfig, netstat, route, etc.
tcpdump          # Ferramenta para captura e análise de pacotes
traceroute       # Para traçar rotas até um host
iputils-ping     # Ferramenta de ping
dnsutils         # Ferramentas como nslookup, dig, etc.
curl             # Para testar conexões HTTP/HTTPS
wget             # Para download de arquivos via HTTP/HTTPS/FTP
nmap             # Ferramenta para escanear redes
telnet           # Para conexões remotas
iptables   
```

E esta disponvivel em duas versões:
- `latest` e `ubuntu` = Imagem base ubuntu
- `alpine` = Imagem base alpine

os  arquivos dockerfile estão disponíveis nesse repositorio.

## Imagem da aplicação

<p align="center">
  <img src="https://github.com/joao-pedro-rdo/container-net-lab/blob/main/images/container-net-lab.png" alt="Imagem" style="border: 5px solid rgba(0, 0, 0, 0.2); border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);"/>
</p>





