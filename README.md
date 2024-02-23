# CodeLeap API (Back End para Teste Django)

Bem-vindo à API simples, mas direta, para o teste Django. Embora o uso de genéricos do Django pudesse simplificar as rotas, acredito que a abordagem que utilizei ofereça mais controle sobre a saída

## Inicialização do Projeto

Se o Docker estiver instalado em sua máquina, basta executar o seguinte comando:

```bash

docker-compose up - d

```

Aproveite a API em sua rota padrão > http://localhost:8000

\_\_

Caso contrário, siga os passos abaixo em sua máquina:

- 1 Navegue até o diretório raiz do projeto e execute o seguinte comando:

```bash
python -m venv env
```

**Observação**: Se estiver usando Python 3, substitua `python` por `python3`

- 2 Em seguida, ative o ambiente virtual com:

```bash
source env/bin/activate
```

- 3 Agora, instale as dependências. Certifique-se de estar no diretório CodeLeap:

```bash
pip install -r requirements.txt
```

- 4 Em seguida, aplique as migrações. Garanta que você esteja no diretório CodeLeap:

```bash
python manage.py migrate
```

-6 Finalmente, execute o projeto:

```bash
python3 manage.py runserver
```

### Teste

Para executar os testes:

```bash
python manage.py test app/tests
```

Isso executará a suíte de testes localizada no diretório `app/tests`.
