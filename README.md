# 🛍️ API com TDD: Gerenciamento de Produtos Robusto e Eficiente

Bem-vindo(a) ao repositório da Product API! Este projeto foi cuidadosamente desenvolvido para oferecer uma solução de backend completa e performática para o gerenciamento de produtos. Utilizando as melhores práticas do mercado, ele se destaca pela sua robustez, flexibilidade e atenção aos detalhes.

Este projeto é fruto do meu aprendizado e dedicação no **Bootcamp Santander 2025 - Back-End com Python da DIO**, e tive o prazer de desenvolvê-lo junto com as aulas da **Professora Nayanna Nara**! 🎓 É uma honra aplicar todo o conhecimento adquirido em um projeto tão prático e funcional.


## ✨ Funcionalidades em Destaque

  * **Criação Segura de Produtos**: Adicione novos produtos com validação rigorosa e tratamento de exceções para erros de inserção no banco de dados. Qualquer falha na gravação é capturada e informada de forma clara. ✅
  * **Atualização Inteligente**: Mantenha seus registros sempre atualizados\! O campo `updated_at` é preenchido automaticamente com a data e hora da última modificação, mas com a flexibilidade de ser ajustado manualmente se necessário. ⏰
  * **Consulta Avançada de Produtos**: Encontre exatamente o que você precisa. O endpoint de consulta de produtos agora permite filtrar por um **intervalo de preço** (`min_price` e `max_price`), tornando suas buscas mais precisas e eficientes. 🔎
  * **Gestão Completa**: Além das funcionalidades mencionadas, a API oferece operações completas de leitura, atualização parcial e exclusão de produtos, garantindo controle total sobre seus dados. 📝🗑️
  * **Estrutura Limpa e Escalável**: Desenvolvida com arquitetura modular, facilitando a manutenção, expansão e compreensão do código. 🏗️

-----

## 💻 Tecnologias Utilizadas

  * **[FastAPI](https://fastapi.tiangolo.com/)**: O framework web de alta performance para construir APIs com Python 3.8+. Escolhido por sua velocidade e facilidade de uso com tipagem. 🚀
  * **[Motor (MongoDB driver)](https://motor.readthedocs.io/en/stable/)**: Um driver assíncrono para MongoDB, ideal para operações de I/O não bloqueantes. 🍃
  * **[Pydantic](https://pydantic-docs.helpmanual.io/)**: Essencial para a validação de dados e gerenciamento de schemas, garantindo que os dados que entram e saem da API estejam sempre corretos. 🔒
  * **MongoDB**: O banco de dados NoSQL flexível e escalável, perfeito para armazenar dados de produtos. 📊

-----

## 🚀 Primeiros Passos

Siga estas instruções para colocar a API de produtos funcionando em sua máquina local.

### Pré-requisitos

Certifique-se de ter:

  * **Python 3.8+** instalado.
  * Uma instância do **MongoDB** (local ou remota) rodando e acessível.

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone <https://github.com/V4lciJr/FastAPI-com-TDD>
    cd product-api # ou o nome do diretório do seu projeto
    ```
****
2.  **Crie um ambiente virtual (altamente recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate # No Windows: `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    # Se não tiver um requirements.txt, instale manualmente:
    # pip install fastapi uvicorn motor pydantic pymongo
    ```

4.  **Configuração do Banco de Dados:**

      * Crie um arquivo `.env` na raiz do projeto e adicione a string de conexão do seu MongoDB. Exemplo:
        ```
        MONGO_DB_URL="mongodb://localhost:27017/products_db"
        ```
      * Certifique-se de que o **servidor MongoDB** está em execução.

### Executando a Aplicação

Para iniciar a API utilizando o Uvicorn:

```bash
uvicorn main:app --reload
```

Substitua `main:app` pelo caminho real para a sua instância da aplicação FastAPI, se for diferente. A flag `--reload` é útil para o desenvolvimento, pois reinicia o servidor automaticamente a cada alteração no código.

-----

## 🔗 Endpoints da API

Após iniciar a aplicação, você pode acessar a documentação interativa da API em:

  * **Swagger UI**: `http://127.0.0.1:8000/docs` 📚
  * **ReDoc**: `http://127.0.0.1:8000/redoc` 📖

Aqui estão os principais endpoints disponíveis:

### Produtos (`/products`)

  * **`POST /`**: ➕ **Criar um Novo Produto**.
      * **Corpo da Requisição**: Envie os detalhes do produto no formato `ProductIn`.
      * **Resposta**: Retorna os dados do produto criado (`ProductOut`).
      * **Tratamento de Erro**: Se houver um problema na inserção (ex: conexão com DB), uma exceção será levantada com um status HTTP 500.
  * **`GET /{id}`**: 🆔 **Obter Produto por ID**.
      * **Parâmetros**: `id` (UUID do produto).
      * **Resposta**: Retorna os detalhes do produto (`ProductOut`).
      * **Tratamento de Erro**: Retorna `404 Not Found` se o produto não for encontrado.
  * **`GET /`**: 📜 **Consultar Todos os Produtos com Filtro de Preço**.
      * **Parâmetros de Consulta (Opcionais)**:
          * `min_price` (float): Preço mínimo para o filtro (inclusive).
          * `max_price` (float): Preço máximo para o filtro (exclusivo).
      * **Exemplo de Uso**: `GET /products?min_price=5000&max_price=8000` (busca produtos com preço entre 5000 e 8000).
      * **Resposta**: Uma lista de produtos (`List[ProductOut]`).
  * **`PATCH /{id}`**: ✍️ **Atualizar Produto por ID**.
      * **Parâmetros**: `id` (UUID do produto).
      * **Corpo da Requisição**: Envie os campos a serem atualizados (`ProductUpdate`). O `updated_at` será definido automaticamente.
      * **Resposta**: Retorna os dados do produto atualizado (`ProductUpdateOut`).
      * **Tratamento de Erro**: Retorna `404 Not Found` se o produto não for encontrado.
  * **`DELETE /{id}`**: 🗑️ **Deletar Produto por ID**.
      * **Parâmetros**: `id` (UUID do produto).
      * **Resposta**: `204 No Content` em caso de sucesso.
      * **Tratamento de Erro**: Retorna `404 Not Found` se o produto não for encontrado.

-----

## 🤝 Contribuição

Sua contribuição é muito bem-vinda\! Se você encontrar bugs, tiver sugestões de melhoria ou quiser adicionar novas funcionalidades, sinta-se à vontade para:

1.  Abrir uma [Issue](https://www.google.com/search?q=https://github.com/seu-usuario/seu-repositorio/issues) 🐛
2.  Criar um [Pull Request](https://www.google.com/search?q=https://github.com/seu-usuario/seu-repositorio/pulls) 💡

-----

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](https://www.google.com/search?q=LICENSE).

-----
