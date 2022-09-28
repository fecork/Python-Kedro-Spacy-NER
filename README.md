# Spacy NER test with Kedro

_Descripción del Proyecto_

Pruebas de Spacy para un modelo de custom NER

# Estructura del Proyecto

Este proyecto tiene la estructura Kedro para aplicar buenas prácticas de software en pruebas
de modelos de IA y Ciencia de datos, y los datos están organizados en ocho capas de acuerdo al
Data Engineering Convention.

- conf: configuración de parámetros, catalogo de datos y credenciales.
- data: datos utilizados para las pruebsa y generados por el modelo
- logs: logs guardados
- notebooks: para análisis de datos utilizados o resultados del modelo
- src: código principal, configuración de pipelines y nodes.

# Pesos del modelo en

[Drive](https://drive.google.com/drive/folders/1r1qIzRU8dOtc7VNF7GNCN1cCDvNjsv7n?usp=sharing)

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.

```
git clone
```

### Pre-requisitos 📋

Instalar

```
pip install kedro
```

```
sudo apt install pipenv
```

```
pip install jupyter
```

### Instalación 🔧

Para ejecutar en local

instalamos los repositorios

```
pip install -r src/requirements.txt
```

o

```
pipenv install -r src/requirements.txt
```

Para crear o actualizar el archivo de requirements,

```
kedro build-reqs
```

iniciamos entorno virtual

```
pipenv shell
```

## Ejecutar

```
kedro run
```

## Ejecutando las pruebas unitarias ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

```
pipenv test
```

### Ejecutando las pruebas con Kedro para el flujo de trabajo 🔩

_Explica que verifican estas pruebas y por qué_

```
kedro test
```

revisar el archivo `src/tests/test_run.py` para ver las instruciones de cómo crear
pruebas para el flujo de trabajo, el coverage treshold está en el archivo `.coveragerc`

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Jupyter

Para presentar informes o analizar los datos de entrada y resultantes del modelo,
podemos usar notebooks

```
kedro jupyter notebook
```

## Visualizar Pipelines

```
kedro viz
```

## Generar Documentación

```
kedro build-docs
```

## Despliegue 📦

Para realizar el despliegue, cada node debe convertirse en una función

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

- [Kedro](https://pypi.org/project/kedro/)
- [data engineering convention](https://kedro.readthedocs.io/en/stable/faq/faq.html#what-is-data-engineering-convention)
- [Pipenv](https://github.com/microsoft/vscode-azurefunctions)

- [Azure Functions SDK](https://pypi.org/project/azure-functions/) - Microsoft
- [Spacy](https://spacy.io/api/data-formats) - Modelo GPT3

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en:

[Wiki](https://github.com/tu/proyecto/wiki)

[Kedro Paso a paso](https://www.notion.so/fecork/Kedro-paso-a-paso-71a3fa04d41c45409824db8cc27753b8)

[Estructura Kedro](https://www.notion.so/fecork/Estructura-Kedro-en-Python-6ced565ed4eb4a78888f6e7af57799c1)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

- **Wilberth Ferney Córdoba Canchala** - _Trabajo Inicial_ - [LinkenId](https://github.com/villanuevand)

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

- Comenta a otros sobre este proyecto 📢
- Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
- Da las gracias públicamente 🤓.
- etc.
