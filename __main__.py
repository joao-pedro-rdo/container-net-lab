import docker
import streamlit as st
import pandas as pd
import subprocess
import random

client = docker.from_env()  # simples e para trabalhar localmente
# client = docker.DockerClient() # para trabalhar com o docker remoto

def mostra_container():
    """Função para mostrar os containers que estão rodando"""
    meus_containers = []
    meus_containers_rodando = []
    lista_containers = client.containers.list(all=True)
    for i in lista_containers:
        if i.status == "running":
            aux_rodando = {
                "name": i.name,
                "id": i.id,
                "porta": i.ports,
                "status": i.status,
            }
            meus_containers_rodando.append(aux_rodando)
        else:
            aux = {"name": i.name, "id": i.id, "status": i.status}
            meus_containers.append(aux)
    # Mostrandos os containers que estão rodando
    st.subheader("Containers rodando")
    data_meus_containers_rodando = pd.DataFrame(meus_containers_rodando)
    if data_meus_containers_rodando.empty:
        st.write("Nenhum container rodando.")
    else:
        st.dataframe(data_meus_containers_rodando)
    st.markdown("---")
    
    # Mostrando os containers que não estão rodando
    st.subheader("Containers parados")
    data_meus_containers = pd.DataFrame(meus_containers)
    if data_meus_containers.empty:
        st.write("Nenhum container parado.")
    else:
        st.dataframe(data_meus_containers)


def criar_container(disto: str = ""):
    """Função para criar um container"""
    st.warning("Criando um novo Container.....")

    random_host_port = random.randint(10000, 60000)

    # Define a porta do container e a porta aleatória do host
    ports = {
        "8080/tcp": random_host_port  # Mapeia a porta 8080 no container para uma porta aleatória no host
    }
    # parametros.append(porta)
    container = client.containers.run(
        "joaoprdo/redes-tools:ubuntu",
        detach=True,
        ports=ports,
        remove=True,
        network="bridge",
    )
    st.success(f"Container criado com sucesso!")
    st.write(f"ID: {container.id}")
    abrr_terminal(container)
    return container


def abrr_terminal(container):
    """Função para abrir um terminal no container"""
    #!  Para power shell windows usando o wsl
    comando = f"docker exec -it {container.id} /bin/bash"
    #subprocess.run(["gnome-terminal", "--", "bash", "-c", comando])  #! Para linux
    subprocess.run(
            [
                "powershell.exe",
                "-Command",
                f"Start-Process powershell -ArgumentList 'docker exec -it {container.id} /bin/bash'",
            ]
        )


def apaga_containers():
    """Função para apagar todos os containers"""
    containers = client.containers.list(all=True)
    for i in containers:
        i.stop()
    client.containers.prune(filters=None)

st.set_page_config(
    page_title="Network Tools Docker",
    page_icon="🐳",
    layout="wide",
    initial_sidebar_state="auto",
)

def main():
    st.title("Gerador de Container Docker para aula de redes")
    # Criar as colunas do streamlit
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Criar CT Ubuntu"):
            container = criar_container("ubuntu")  
    with col2:
        if st.button("Criar CT Alpine"):
            container = criar_container("alpine")
    with col3:
        if st.button("Apagar Containers"):
            apaga_containers()
            st.success("Todos os containers foram removidos com sucesso!")

    st.markdown("---")
    mostra_container()
    


if __name__ == "__main__":
    main()
