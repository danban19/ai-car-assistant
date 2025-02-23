# Installation Guide

## Install Poetry

For detailed instructions, visit the [Poetry Documentation](https://python-poetry.org/docs/).

## Activate Environment

```sh
poetry shell
```

## Install Dependencies

```sh
poetry lock --no-update
```

```sh
poetry install
```

## To run the app

```sh
chainlit run src/app.py -w
```

## Linting and formating

```sh
poetry run flake8 .
```

```sh
poetry run black .
```