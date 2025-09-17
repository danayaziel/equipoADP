## Diferencias entre Conda, venv y pip

**Conda**:
Conda es un gestor de paquetes y entornos de código abierto que funciona en múltiples lenguajes (no solo Python) y puede instalar dependencias no solo de Python sino también de otros lenguajes (como bibliotecas de C). 

**Pip**:
Pip es el gestor de paquetes oficial de Python, enfocado en instalar bibliotecas de Python desde el PyPI. 

**Venv**:
Venv es la herramienta nativa de Python para crear y gestionar entornos virtuales aislados, y se usa en conjunto con pip para instalar y aislar paquetes de Python en un proyecto. 

### Pasos para recrear el entorno en otra computadora.
**Conda**
```bash
# crear entorno con la misma versión de Python
conda create --name mi_proyecto python=3.11 -y
conda activate mi_proyecto
# instalar paquetes listados en requirements.txt usando pip
pip install -r requirements.txt
```
**Pip y Venv**
```bash
python -m venv mi_en
.\mi_en\Scripts\activate
pip install -r requirements.txt
``` 