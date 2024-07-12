# CLI Calculator

This simple calculator CLI app shows the use of poetry to configura and manage a python project and its dependencies.

### 1. Install poetry

```bash
pip install poetry
```
or

```bash
pipx install poetry
```

Note that python and its tools need to be installed.

### 2. Configure poetry virtual environments locations (optional)

By default, poetry saves a project virtual environment in as specific folder in the system (not in the project folder). In this case, we are going to change that setting to save the virtual environment folder in the project's folder.

```bash
poetry config virtualenvs.in-project true
```

### 3. Create project folder and package

```bash
poetry new <my-folder> --name <package>
```

### 4. Add project dependencies

Once inside the project folder

```bash
poetry add <dependency>
```

To add dependencies that are going to be used only during development

```bash
poetry add <dependency> -G dev
```

### 5. Run the app
Once app has been developed, you can run the app with poetry

In the `pyproject.toml` file, add 

```bash
[tool.poetry.scripts]
<script-name> = "<package>.<module>:<function>"
```

The script can be executed in two ways

```bash
poetry run <script-name> <command> <argument> ...
```

or the virtual environment can be activated as an interactive shell

```bash
poetry shell
```

Then, to install your app locally in editable mode (change are reflected immediatly), simply run

```bash
pip install --editable .
```

Then, execute the app

```bash
<script-name> <command> <argument> ...
```