# sw-projection-storage

[![Test & lint](https://github.com/AvenirHealth-org/sw-projection-storage/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/AvenirHealth-org/sw-projection-storage/actions/workflows/test.yml)
[![Build Docker Image](https://github.com/AvenirHealth-org/sw-projection-storage/actions/workflows/docker.yml/badge.svg)](https://github.com/AvenirHealth-org/sw-projection-storage/actions/workflows/docker.yml)

Projection data storage for Spectrum Web.

# Development

sw-projection-storage uses [uv](https://docs.astral.sh/uv/) as a package and project manager. To install `uv` go to [installation instructions](https://docs.astral.sh/uv/getting-started/installation/). `uv` will automatically manage installing the correct Python version, updating dependencies and the virtual environment.


## Run app

```
uv run uvicorn app.main:app --port 8000
```

with reloading

```
uv run uvicorn app.main:app --port 8000 --reload
```

## Tests

We use [pytest](https://docs.pytest.org/en/stable/) for testing, to run the tests run

```
uv run pytest
```

## Lint & formatting

We use [ruff](https://docs.astral.sh/ruff/) for linting and formatting, to run lint and format checks

```
uvx ruff check
```

To run autoformatter

```
uvx ruff format
```

## Type checking

We use [basedpyright](https://docs.basedpyright.com/latest/) for type checking. We recommend installing the VSCode extension to get type checking integrated with your IDE. Can also run the checks with

```
uv run basedpyright
```

# Docker

You can either build it locally, or use the image from [GitHub package registry](https://github.com/AvenirHealth-org/sw-projection-storage/pkgs/container/sw-projection-storage)

Build the docker image

```
docker build -t avenirhealth-org/sw-projection-storage -f docker/Dockerfile .
```

Run the docker image

```
docker run -p 8000:8000 avenirhealth-org/sw-projection-storage
```

Run using package registry

```
docker run -p 8000:8000 ghcr.io/avenirhealth-org/sw-projection-storage:main
```
