# Calculator

A simple Python calculator with unit tests and an automated GitHub Actions workflow.

## Features

- Addition
- Subtraction
- Multiplication
- Division (raises `ValueError` when dividing by zero)

## Run the tests

Python 3.8 or newer is recommended. The tests use Python's built-in `unittest` framework, so no extra packages are required.

```bash
python -m unittest discover -s tests -v
```

## Continuous integration

GitHub Actions runs the unit tests automatically whenever code is pushed to the `main` or `master` branch.
