# Learning Python

The development ecosystem is evolving and in order to remain competitive is important to continue adapting and learning new things.

This time I'm in the journey of learning Python.

- Dependency managers
- Publishing packages and libraries  # clarify what is the difference between a package and a library
- Tooling
- Testing

## Just

"Commands, called recipes, are stored in a file called justfile with syntax inspired by make"

Just es parecido a `make`, pero aparentemente mas moderno y con muchas useful features e improvements over `make`.

- it loads .env files making easy to populate environment variables

- command line completition scripts

- recipes can be written in arbitrary languages like Python or NodeJS

- Just a command runner, not a build system, so it avoid many of the problems que tiene `make`.

### Getting started

En Mac se puede instalar con `brew`

```bash
brew install just
```

To learn more about the installation check https://github.com/casey/just?tab=readme-ov-file#packages

## Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.

### Getting started

```bash
poetry new package_name
```

The official link is https://python-poetry.org/docs/basic-usage/#project-setup

Entonces ya teniendo mi estructura con `Poetry` es importante entender que un paquete o library de python se hace de cierta forma.

Tenemos modules

Module es un file simplemente. El modulo es el file name.

## Publishing a library

We need to build and package the library.

Since we need Poetry, we need:

https://github.com/marketplace/actions/install-poetry-action

And here I can learn how to build and test python projects:

https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

More information here

https://packaging.python.org/en/latest/tutorials/packaging-projects/

### Modules

Que es un `module` en python?

Pues un file y el nombre del module es el nombre del file.

Y luego tenemos los `packages`.

### Packages

Los paquetes son una forma de structurar el codigo de Python. Por ejemplo:

sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

El `__init__.py` es una forma de inicializar el package y hasta puedes configurar los modulos y como se hacen las importaciones.

Por ejemplo Bittensor tiene algo asi en el`__init__.py`.

```python
from .utils.balance import Balance as Balance
```

Lo que significa es que en lugar de hacer 

```python
from mypackage.utils.balance import Balance
```

Solo podria hacer

```python
from mypackage import Balance
```

Y ya se facilita mucho los imports y lo hago disponible directamente en el root de mi paquete digamos.

Aqui esta como lo tiene Bittensor

https://github.com/opentensor/bittensor/blob/master/bittensor/__init__.py#L209C1-L242C37

<!-- References -->

