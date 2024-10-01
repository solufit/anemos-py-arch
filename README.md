# Anemos Python SDK

[![Lint Check](https://github.com/solufit/fastapi-template/actions/workflows/lint-python.yml/badge.svg)](https://github.com/solufit/fastapi-template/actions/workflows/lint-python.yml)
[![Python application test](https://github.com/solufit/fastapi-template/actions/workflows/test-python.yml/badge.svg)](https://github.com/solufit/fastapi-template/actions/workflows/test-python.yml)

## Configuring linting and type checking

### Ruff (Linting)

To modify ruff linting rules, edit the `pyproject.toml` file in the root directory. Adjust the `[tool.ruff]` section to customize ruff's behavior.

### Mypy (Type Checking)

To configure mypy type checking, add or modify the `[tool.mypy]` section in your `pyproject.toml` file.

You can adjust these settings based on how strict you want the type checking to be. For more options, refer to the [mypy configuration file documentation](https://mypy.readthedocs.io/en/stable/config_file.html).

Remember to run `mypy` and `ruff` regularly during development to catch type errors and style issues early.
If you use Visual Studio Code, you can install the Python extension to get real-time feedback on type errors and linting issues.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Python SDK Develper: Handa Kengo
Anemsos Developer: Solufit Anemos Developer Team
