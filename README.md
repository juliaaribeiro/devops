# Exercício Prático — Docker, GitHub Actions e Container Registry

Este projeto implementa uma aplicação simples em Python com FastAPI, com endpoint `GET /hello`.

## Versões

- Versão 1.0: `Hello World`
- Versão 2.0: `Hello World 2`

A aplicação usa a variável de ambiente `APP_MESSAGE` para alternar o texto da resposta do endpoint.

## Estrutura do projeto

- `app/main.py`: aplicação FastAPI
- `Dockerfile`: imagem da aplicação
- `.github/workflows/docker.yml`: pipeline do GitHub Actions
- `requirements.txt`: dependências da aplicação

## Executar localmente

### Build da versão 1.0

```bash
docker build -t minha-aplicacao:1.0 --build-arg APP_MESSAGE="Hello World" .
docker run -d --rm -p 8080:8080 --name app-v1 minha-aplicacao:1.0
curl http://localhost:8080/hello
```

Resultado esperado:

```text
Hello World
```

### Build da versão 2.0

```bash
docker build -t minha-aplicacao:2.0 --build-arg APP_MESSAGE="Hello World 2" .
docker run -d --rm -p 8080:8080 --name app-v2 minha-aplicacao:2.0
curl http://localhost:8080/hello
```

Resultado esperado:

```text
Hello World 2
```

## Pipeline GitHub Actions

A pipeline automatiza:

1. checkout do repositório;
2. build da imagem Docker;
3. validação do endpoint `/hello`;
4. autenticação no GHCR;
5. publicação das imagens no GitHub Container Registry.

## Observações

- A imagem padrão do Dockerfile usa `Hello World`.
- O valor pode ser sobrescrito com `--build-arg APP_MESSAGE="Hello World 2"` para gerar outra versão.
- Para publicar no GHCR, configure o repositório e o token do GitHub Actions conforme as permissões do pacote.
