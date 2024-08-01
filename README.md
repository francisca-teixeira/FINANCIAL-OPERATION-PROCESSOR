# Financial Operation Processor

FOP is a **business critical application**, which processes and authorizes debit
operations on a bank account by using a set of rules.

Check the [contributing](./CONTRIBUTING.md) document for information about how
to contribute to this project.

Check the [challenge](./documentation/CHALLENGE.md) document for information about the summer
camp challenge.

## Contents

- [Setup the Tools](#setup-the-tools)
- [Setup the Development Environment](#setup-the-development-environment)

## [Setup the Tools](#contents)

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads)
- [Pipenv](https://pipenv.pypa.io/en/latest/installation.html)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Visual Studio Code Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Visual Studio Code Pylance extension](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Visual Studio Code Flake8 extension](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)
- [Visual Studio Code Isort extension](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
- [Visual Studio Code Robot Framework extension](https://marketplace.visualstudio.com/items?itemName=robocorp.robotframework-lsp)
- [Visual Studio Code Markdownlint extension](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
- [Visual Studio Code YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
- [Visual Studio Code Postman extension](https://marketplace.visualstudio.com/items?itemName=Postman.postman-for-vscode)

### Docker Community on Windows

Install Docker using WSL2 to run Ubuntu Linux 22.04.2 LTS. Run from a terminal:

```console
wsl --install -d Ubuntu-22.04
wsl --set-default-version 2
```

After finished, follow the steps to install using `apt` from the [Official Website](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository).

### Docker Community on Linux

Follow the steps from the [Official Website](https://docs.docker.com/engine/install/)
according to your Linux distribution.

### Testing Docker

From a terminal on the parent folder, build the image:

```console
$ docker build --tag fop -f ./infrastructure/docker/application/Dockerfile .

[+] Building 5.8s (9/9) FINISHED
...
=> exporting to image
=> => exporting layers
=> => writing image
=> => naming to docker.io/library/fop
```

From a terminal on the parent folder, run the container:

```console
$ docker run --env TEST_MODE=False -v ./data:/fop/data:ro -v ./output:/fop/output:rw --name fop --rm fop

Financial operation processor: Hello
```

Finally, access the running container:

```console
docker exec -it fop bash
```

## [Setup the Development Environment](#contents)

From a terminal on the application folder, run:

```console
pipenv shell
pip install --upgrade pip
pipenv install --skip-lock --system
```
