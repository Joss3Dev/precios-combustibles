# Instalacion y puesta en marcha
Este proyecto se desarrollo utilizando Python v3.9 y MongoDB v5.0.8.<br/>
Inicialmente se debe ingresar al fichero donde se encuentra el proyecto y crear un entorno virtual en Python 3.9:<br/>
```
cd /path/a/proyecto/precios-combustibles
python3 -m venv
```
Luego se debe activar el entorno virtual e instalar las correspondientes dependencias:
```
. ./venv/bin/activate
pip install -r requirements.txt
```
Una vez configurado e instalado las dependencias se debe levantar MongoDB localmente en el puerto 27017.<br/>
Al ya estar en ejecucion MongoDB el paso final es ejecutar el archivo python scrapper.py
```
python scrapper.py
```