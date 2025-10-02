# 02. VS Code y Conda - Configuración del Entorno

## 🔧 Extensiones VS Code Necesarias

- **Python** (ms-python.python) - Soporte completo para Python
- **Pylance** (ms-python.vscode-pylance) - Language server avanzado  
- **Python Debugger** (ms-python.debugpy) - Debugging integrado
- **Jupyter** (ms-toolsai.jupyter) - Notebooks y celdas interactivas

## 🎯 Objetivos

- Instalar y configurar Miniconda
- Crear y gestionar entornos virtuales con conda
- Integrar conda con VS Code

## 📋 Paso 1: Instalar Miniconda

```bash
# Descargar Miniconda para Linux
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Hacer ejecutable
chmod +x Miniconda3-latest-Linux-x86_64.sh

# Ejecutar instalador (seguir instrucciones en pantalla)
./Miniconda3-latest-Linux-x86_64.sh
```

### Durante la instalación

1. Presionar **ENTER** para continuar leyendo la licencia
2. Escribir **yes** para aceptar los términos
3. Presionar **ENTER** para instalar en la ubicación por defecto (`~/miniconda3`)
4. Escribir **yes** cuando pregunte si quiere inicializar conda

### Configurar PATH y reiniciar terminal

```bash
# El instalador debería añadir conda al PATH automáticamente
# Si no lo hizo, añadirlo manualmente:
echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bashrc

# Recargar configuración del shell
source ~/.bashrc

# O alternativamente: cerrar y abrir nueva terminal
```

## 📋 Paso 2: Verificar Instalación

```bash
# Verificar que conda está disponible
conda --version
# Debería mostrar algo como: conda 23.x.x

# Obtener información del sistema conda
conda info
# Muestra configuración completa

# Ver entornos disponibles (inicialmente solo 'base') - comando principal
conda env list

# Ver entornos disponibles (forma alternativa)
conda info --envs
```

**Si `conda` no se reconoce:**

```bash
# Verificar si miniconda está instalado
ls -la ~/miniconda3/bin/conda

# Si existe, añadir al PATH manualmente
export PATH="$HOME/miniconda3/bin:$PATH"
conda --version
```

## 📋 Paso 3: Crear Entorno para el Curso

```bash
# Crear entorno llamado "sea_curso" con Python 3.11
conda create -n sea_curso python=3.11

# Verificar que el entorno se creó correctamente
conda env list
# Ahora deberías ver: base y sea_curso

# También puedes usar la forma alternativa
conda info --envs

# Activar el entorno
conda activate sea_curso

# Verificar que estamos en el entorno correcto
which python
python --version

# IMPORTANTE: Apuntar la ruta completa para VS Code
which python
# Ejemplo de salida: /home/usuario/miniconda3/envs/sea_curso/bin/python
```

**⚠️ Importante:** Apunta la ruta completa que muestra `which python`, la necesitarás para configurar VS Code.

## 📋 Paso 4: Instalar Paquetes Esenciales

```bash
# Con el entorno sea_curso activado
conda install numpy

# Verificar instalación
conda list numpy
```

## 📋 Paso 5: Demostrar Aislamiento de Entornos

Una de las ventajas principales de los entornos virtuales es que cada uno puede tener diferentes versiones de paquetes sin conflictos.

### Instalar diferentes versiones de numpy

```bash
# Activar entorno sea_curso (si no está activo)
conda activate sea_curso

# Instalar numpy 1.24 en sea_curso (versión más antigua)
conda install numpy=1.24

# Verificar versión en sea_curso
python -c "import numpy; print(f'sea_curso: numpy {numpy.__version__}')"

# Cambiar al entorno base
conda deactivate

# Instalar numpy última versión en base
conda install numpy

# Verificar versión en base (debería ser más reciente)
python -c "import numpy; print(f'Base: numpy {numpy.__version__}')"
```

### Comparar los dos entornos

```bash
# En sea_curso (activo)
python -c "import sys; print(f'Python: {sys.executable}')"
python -c "import numpy; print(f'NumPy: {numpy.__version__}')"

# Cambiar a base
conda deactivate
python -c "import sys; print(f'Python: {sys.executable}')"
python -c "import numpy; print(f'NumPy: {numpy.__version__}')"
```

**Resultado esperado:** Verás que cada entorno tiene su propia versión de numpy y su propio intérprete de Python, completamente aislados.

## 📋 Paso 6: Limpiar - Eliminar Entorno de Prueba

Una vez que hayas comprobado cómo funcionan los entornos virtuales, puedes eliminar el entorno de prueba:

```bash
# Asegurarse de no estar en el entorno que vamos a borrar
conda deactivate

# Verificar qué entornos tenemos
conda env list

# Eliminar el entorno sea_curso
conda env remove -n sea_curso

# Confirmar que se eliminó
conda env list
# Ahora solo debería aparecer 'base'
```

**Nota:** Al eliminar un entorno se borran todos sus paquetes y configuraciones. Es una operación irreversible, pero no afecta a otros entornos.

## 💡 Comandos Útiles de Conda

### Gestión de entornos

```bash
conda env list                  # Listar entornos (forma principal)
conda info --envs              # Listar entornos (forma alternativa)
conda activate nombre_entorno   # Activar entorno
conda deactivate               # Desactivar entorno actual
conda env remove -n nombre     # Eliminar entorno
```

### Gestión de paquetes

```bash
conda install paquete          # Instalar paquete
conda update paquete           # Actualizar paquete
conda list                     # Listar paquetes instalados
conda search paquete           # Buscar paquetes disponibles
```

### Exportar/Importar entornos

```bash
conda env export > environment.yml    # Exportar configuración
conda env create -f environment.yml   # Crear desde archivo
```

## 📚 Recursos

- [Conda Documentation](https://docs.conda.io/)
- [Miniconda Download](https://docs.conda.io/en/latest/miniconda.html)
- [VS Code Python Extension](https://code.visualstudio.com/docs/python/python-tutorial)

---

## ➡️ Siguiente

**[03. Conceptos Básicos](../03_conceptos_basicos/README_03.md)**
