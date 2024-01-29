Obs: Não consegui rodar o python pelo docker, possivelmente tenho que configurar o wsgi no docker e está dando erro socket hang up quando tento executar a URL do Docker

** Test Rizen**
## Instalação e configuração de ambiente

Primeiro de tudo você precisa iniciar a instância docker do MongoDb.

```bash
  docker-compose up db --build
```

Copie o arquivo *.env.example* e tire o *.example* do final do arquivo para ter as variaveis de ambiente

precisa criar e iniciar sua aplicação do Flask, para isso é preciso a versão python >=3.8
Se possivel crie uma virtualização do python
Referência: [virtualenv](https://pypi.python.org/pypi/virtualenv)

```bash
  python -m venv venv
```

Agora ative sua virtualização e instale as dependencias

```bash
  source venv/bin/activate
  pip install -r requirements.txt 
```

Após rodar esses comando e se não houver nenhum erro basta iniciar sua aplicação com:

```bash
  flask run
```

## Rotas
Obs: Todas as rotas precisam ter o Content-Type: application/json

Get All das previsões
```bash
GET http://127.0.0.1:5000/api/weather
```

Crir uma previsão
```bash
POST http://127.0.0.1:5000/api/weather
```
*Precisa passar o body*
```bash
JSON
{
    "lat": -23.5555497,
    "long": -46.6223649
}
```
## Structure

```bash
.
├── Raizen  (MAIN PACKAGE)
│   ├── app.py  (APP FACTORIES)
│   ├── blueprints  (BLUEPRINT FACTORIES)
│   │   ├── __init__.py
│   │   ├── weather  (REST API)
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   ├── ext (EXTENSION FACTORIES)
│   │   ├── commands.py
│   │   ├── configuration.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── external_interfaces  (ACCESS OTHERS APIs)
│   ├── dto  (DATA TRANSFER OBJECT)
│   ├── use_cases  (BUSINESS RULES)
│   ├── models  (DATABASE MODELS)
│   ├── respository  (DATABASE REPOSITORY)
│   ├── utils  (AUXILIARY FUNCTIONS)
├── .env.example (ENVIRONMENT VARIABLES DEFAULT)
├── README.md
├── requirements.txt
└── settings.toml  (SETTINGS)

7 directories, 26 files
```
