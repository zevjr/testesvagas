# README - API para o Golden Raspberry Awards

Este projeto é uma API RESTful desenvolvida em Flask para fornecer informações sobre os produtores com maior e menor intervalo entre dois prêmios consecutivos na categoria "Pior Filme" do Golden Raspberry Awards. A aplicação lê os dados de um arquivo CSV, armazena-os em um banco de dados SQLite em memória e fornece um endpoint para consultar os intervalos de prêmios.

---

## 📋 **Descrição do Projeto**

O objetivo deste projeto é desenvolver uma API que processe um arquivo CSV contendo informações sobre filmes indicados e vencedores do Golden Raspberry Awards (Razzie Awards) na categoria "Pior Filme". A API deve calcular e retornar:

1. O produtor com o maior intervalo entre dois prêmios consecutivos.
2. O produtor com o menor intervalo entre dois prêmios consecutivos.

O formato da resposta deve seguir o padrão especificado no desafio.

---

## 🎯 **Requisitos do Desafio**

### Requisitos Funcionais
1. Ler um arquivo CSV e carregar os dados em um banco de dados ao iniciar a aplicação.
2. Fornecer um endpoint que retorne:
   - O produtor com o maior intervalo entre dois prêmios consecutivos.
   - O produtor com o menor intervalo entre dois prêmios consecutivos.

### Requisitos Não Funcionais
1. A API deve seguir o nível 2 de maturidade de Richardson para RESTful APIs.
2. A aplicação deve usar um banco de dados em memória (SQLite).
3. A aplicação deve incluir testes de integração.
4. O código deve ser disponibilizado em um repositório Git.

---

## � **Como Executar o Projeto**

Abaixo estão as instruções para rodar o projeto de três maneiras diferentes: usando Flask com `venv`, usando Poetry e usando Docker.

### 1. **Usando Flask com `venv`**

#### Pré-requisitos
- Python 3.9 ou superior instalado.
- `pip` instalado.

#### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute a aplicação:
   ```bash
   python run.py
   ```

6. Acesse a API em:
   ```
   http://localhost:5000/award/intervals
   ```

---

### 2. **Usando Poetry**

#### Pré-requisitos
- Poetry instalado. Se não tiver, instale com:
  ```bash
  pip install poetry
  ```

#### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Instale as dependências com o Poetry:
   ```bash
   poetry install
   ```

3. Ative o ambiente virtual do Poetry:
   ```bash
   poetry shell
   ```

4. Execute a aplicação:
   ```bash
   poetry run python run.py
   ```

5. Acesse a API em:
   ```
   http://localhost:5000/award/intervals
   ```

---

### 3. **Usando Docker**

#### Pré-requisitos
- Docker instalado.

#### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Construa a imagem Docker:
   ```bash
   docker build -t flask-app .
   ```

3. Execute o contêiner:
   ```bash
   docker run -p 5000:5000 flask-app
   ```

4. Acesse a API em:
   ```
   http://localhost:5000/award/intervals
   ```

---

## 🧪 **Testes**

A aplicação inclui testes de integração para garantir que o endpoint `/award/intervals` funcione corretamente. Para rodar os testes:

### Usando `venv` ou Poetry
1. Ative o ambiente virtual (se necessário).
2. Execute os testes com:
   ```bash
   pytest
   ```

### Usando Docker
1. Construa a imagem Docker (se ainda não tiver feito):
   ```bash
   docker build -t flask-app .
   ```
2. Execute os testes dentro do contêiner:
   ```bash
   docker run flask-app pytest
   ```

---

## 🧠 **Detalhes de Implementação**

### Estrutura do Projeto
O projeto foi organizado seguindo boas práticas de desenvolvimento, como Clean Architecture, SOLID e DRY. A estrutura do projeto é a seguinte:

```
.
├── app
│   ├── __init__.py          # Inicialização do Flask e configuração do banco de dados
│   ├── config.py            # Configurações da aplicação
│   ├── models.py            # Definição do modelo de dados (Movie)
│   ├── controllers          # Controladores (endpoints da API)
│   │   └── award_controller.py
│   ├── services             # Lógica de negócio
│   │   ├── award_service.py # Cálculo dos intervalos de prêmios
│   │   └── data_loader.py   # Carregamento dos dados do CSV
│   └── database.py          # Configuração do banco de dados
├── data
│   └── movielist.csv        # Arquivo CSV com os dados dos filmes
├── tests
│   ├── __init__.py
│   └── test_integration.py  # Testes de integração
├── Dockerfile               # Configuração do Docker
├── pyproject.toml           # Dependências do Poetry
├── requirements.txt         # Dependências do pip
├── run.py                   # Ponto de entrada da aplicação
└── README.md                # Documentação do projeto
```

### Decisões de Código
1. **Banco de Dados em Memória**: Optamos por usar SQLite em memória para atender ao requisito de não precisar de instalação externa. Isso facilita a execução em diferentes ambientes.
2. **Separação de Responsabilidades**: A lógica de negócio foi separada em serviços (`award_service.py` e `data_loader.py`), enquanto os controladores (`award_controller.py`) lidam apenas com a interação HTTP.
3. **Testes de Integração**: Os testes garantem que o endpoint retorne os resultados corretos com base nos dados fornecidos.
4. **Dockerização**: A aplicação foi dockerizada para facilitar a execução em qualquer ambiente com Docker instalado.

### Endpoint da API
O endpoint `/award/intervals` retorna um JSON no seguinte formato:

```json
{
  "min": [
    {
      "producer": "Producer A",
      "interval": 5,
      "previousWin": 2000,
      "followingWin": 2005
    }
  ],
  "max": [
    {
      "producer": "Producer B",
      "interval": 10,
      "previousWin": 2010,
      "followingWin": 2020
    }
  ]
}
```

---

## 🛠 **Tecnologias Utilizadas**
- **Flask**: Framework web para criar a API RESTful.
- **SQLAlchemy**: ORM para interagir com o banco de dados SQLite.
- **Poetry**: Gerenciador de dependências e ambiente virtual.
- **Docker**: Para conteinerização da aplicação.
- **Pytest**: Para testes de integração.

---

## 📄 **Licença**
Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 🤝 **Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## 📧 **Contato**
Para dúvidas ou sugestões, entre em contato:
- **Email**: zejunior.py@gmail.com
- **GitHub**: [zevjr](https://github.com/zevjr)

