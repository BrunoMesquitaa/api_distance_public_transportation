
<img src="api_distance_public_transportation.jpeg" width="500">

# API Distância do Transporte público em São Paulo-BR 🚌

[![Python tests](https://github.com/BrunoMesquitaa/api_distance_public_transportation/actions/workflows/pytest.yml/badge.svg)](https://github.com/BrunoMesquitaa/api_distance_public_transportation/actions/workflows/pytest.yml)

---

### **English version**: <a target="_blank" href="https://github.com/BrunoMesquitaa/api_distance_public_transportation/blob/main/README-eng.md">README.md</a>

---
## Sobre a API:
> #### O principal objetivo dessa API REST é calcular a distância entre um ponto específico (latitude, longitude) e o transporte público mais próximo.
>
> Usando como base: 
>
>> Framework FastAPI:
>>> Documentação: https://fastapi.tiangolo.com
>>>
>>> Código Fonte: https://github.com/tiangolo/fastapi
>>
>> GeoPandas:
>>> Documentação: https://geopandas.org/en/stable/
>>>
>>> Código Fonte: https://github.com/geopandas/geopandas
>
> Dados:
>
>> Shapefiles: https://geosampa.prefeitura.sp.gov.br/PaginasPublicas/_SBC.aspx

---

## Rodando o Projeto:
> ### Local 🥉 :
>
> Recomendo utilizar um virtualenv.
>
> Instalação dos pacotes:
>```console
> poetry install
> ```
> ou
>```console
> pip install --no-cache-dir --upgrade -r requirements.txt
> ```
>
> Run:
> ```console
> uvicorn api_distance_public_transportation.main:app --reload
> ```
> 
> Documentação 👇
>> http://127.0.0.1:8000/docs
>>
>> http://127.0.0.1:8000/redoc
>
> ---
> 
> ### Docker 🥈 :
>
> Build e Run:
> ```console
> docker build -t {name_docker} .
> docker run -p 8080:8080 {name_docker}
> ```
> Documentação 👇
>> http://127.0.0.1:8080/docs
>>
>> http://127.0.0.1:8080/redoc
>
> ---
> 
> ### K8s 🥇 :
> Eu usei o Minikube então pode ser necessário adaptar dependendo do caso.
>
> Algumas configurações interessantes se for usar Minikube:
> ```console
> minikube start
> minikube addons enable ingress
> alias kubectl="minikube kubectl --"
> ```
> Criando nossos recursos no K8s:
> ```console
> kubectl apply -f k8s/kube_deployment.yaml
> ```
> Pegando informações do nosso ingress:
> ```console
> kubectl get ingress
> ```
> 
> Utilizando a IP do ADDRESS podemos acessar a aplicação.
> ![get ingress](images/ingress.png)
>
> Documentação 👇
>> http://192.168.49.2/docs
>>
>> http://192.168.49.2/redoc
>
> Observação usamos uma imagem no DockerHub 👉 <a target="_blank" href="https://hub.docker.com/repository/docker/bmesquitaa/api_distance_public_transportation/general">bmesquitaa</a>

---

## Exemplo:
> ### Request body
> ```console
> {
>    "lat": -23.563949,
>    "lon": -46.6568110
> }
> ```
> ### Responses
> ```console
> {
>    "estacao_metro_km": 0.45,
>    "estacao_trem_km": 3.31,
>    "ponto_onibus_km": 0.26,
>    "terminal_onibus_km": 2.35
> }
> ```
