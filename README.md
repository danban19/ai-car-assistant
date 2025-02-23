# AI Car Assistant 🚗
This project is an AI-powered car-recommender designed for a car retailing company. The assistant interacts with users by asking specific questions to understand car preferences like budget, type, fuel option, brand, and additional features. Based on the input, it suggests the best-matching cars along with their detailed specifications.

## Installation

### 1. Install Poetry
For installation instructions, refer to the [Poetry Documentation](https://python-poetry.org/docs/).

### 2. Activate the Environment
```sh
poetry shell
```

### 3. Install Dependencies
```sh
poetry lock --no-update
poetry install
```

### 4. Configure Environment Variables
Create your `.env` file based on the `env.example` provided.

### 5. Run the Application
```sh
chainlit run src/app.py -w
```

## Code Quality

### Linting
```sh
poetry run flake8 .
```

### Formatting
```sh
poetry run black .
```
