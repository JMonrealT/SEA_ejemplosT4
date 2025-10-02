# 03. Conceptos Básicos - Demos Interactivas

## 🎯 Objetivos

Demostrar 7 conceptos fundamentales de Python mediante scripts ejecutables

## 📋 Demos Disponibles

### 1. Indentación

### 2. Comentarios

### 3. Importar otros módulos

### 3b. if __name__ == '__main__'

### 4. Variables

### 5. Tipos de datos

### 6. Scopes (Ámbitos)

### 7. Clases y herencia

## 📂 Scripts de Demo

### Archivos Disponibles

- `demo_01_indentacion.py` - Indentación y estructura de código
- `demo_02_comentarios.py` - Tipos de comentarios y documentación
- `demo_03_importar_modulos.py` - Diferentes formas de importar
- `demo_03b_name_main.py` - Concepto `if __name__ == '__main__'`
- `demo_03b_importacion_test.py` - Archivo de prueba para importación
- `demo_04_variables.py` - Declaración y convenciones de variables
- `demo_05_tipos_datos.py` - Tipos básicos y conversiones
- `demo_06_scopes.py` - Ámbitos y regla LEGB
- `demo_07_clases_herencia.py` - POO básica con ejemplos prácticos

## 🏃‍♂️ Orden de Ejecución Recomendado

1. **Indentación** - Base estructural de Python
2. **Comentarios** - Documentación y buenas prácticas
3. **Variables** - Declaración y convenciones
4. **Tipos de datos** - Fundamentos de datos
5. **Importar módulos** - Organización de código
6. **Scopes** - Ámbitos y visibilidad
7. **Clases y herencia** - Programación orientada a objetos

## 💡 Cómo usar estas demos

```bash
# Ejecutar cada script individual
python3 demo_01_indentacion.py
python3 demo_02_comentarios.py
python3 demo_03_importar_modulos.py
python3 demo_03b_name_main.py        # Ver funcionamiento directo
python3 demo_03b_importacion_test.py  # Ver comportamiento al importar
python3 demo_04_variables.py
# ...y así sucesivamente
```

### 🔍 Demo Especial: `if __name__ == '__main__'`

El `demo_03b` incluye dos archivos para demostrar este concepto crucial:

- **`demo_03b_name_main.py`** - Ejecutar directamente para ver todo el código
- **`demo_03b_importacion_test.py`** - Ejecutar para ver cómo se comporta al importar

**Diferencia clave:**
- Ejecutar directamente: `__name__ == '__main__'` ✅ (se ejecuta todo)
- Importar como módulo: `__name__ == 'nombre_archivo'` ❌ (solo se importan funciones)

---

## ➡️ Siguiente

**[04. Alternativa a BASH](../04_alternativa_a_bash/README_04.md)**
