#!/bin/bash

# Iniciar cross-anvil en el fondo
cross-anvil &

# Esperar a que cross-anvil esté listo (ajusta según sea necesario)
sleep 5

cd /app/contracts

# Desplegar contratos locales
just deploy_local_contracts

cd /app

# Ejecutar pruebas (esto mantiene el contenedor en ejecución)
poetry run pytest
