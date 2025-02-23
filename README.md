# AI Car Assistant

AI car-recommender chat assistant for a car retailing company using LLM. The assistant engages with users, asking relevant questions to comprehend their car preferences such as budget, car type, fuel type, brand, or specific features. Upon capturing these responses, the assistant will suggest the most suitable cars with their specifications.

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

## Provide .env file
Use env.example as a reference.

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
