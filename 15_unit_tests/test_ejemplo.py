"""
test_ejemplo.py
Ejemplos reales de tests con pytest

Este archivo contiene tests que pueden ser ejecutados con:
    pytest test_ejemplo.py
    pytest test_ejemplo.py -v
    pytest test_ejemplo.py -vs
"""

import pytest
import os


# ============================================================================
# 1️⃣ FUNCIONES A PROBAR
# ============================================================================

def sumar(a, b):
    """Suma dos números"""
    return a + b


def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b


def dividir(a, b):
    """Divide a entre b, lanza excepción si b es 0"""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def potencia(a, b):
    """Calcula a elevado a la potencia b (NO PROBADO - Sin cobertura)"""
    if b < 0:
        return 1 / (a ** (-b))
    return a ** b


# ============================================================================
# 2️⃣ TESTS BÁSICOS
# ============================================================================

class TestSuma:
    """Tests para la función sumar"""
    
    def test_sumar_positivos(self):
        """Test: sumar números positivos"""
        assert sumar(2, 3) == 5
        assert sumar(10, 20) == 30
    
    def test_sumar_negativos(self):
        """Test: sumar números negativos"""
        assert sumar(-1, -1) == -2
        assert sumar(-5, 3) == -2
    
    def test_sumar_cero(self):
        """Test: sumar con cero"""
        assert sumar(5, 0) == 5
        assert sumar(0, 0) == 0


class TestMultiplicacion:
    """Tests para la función multiplicar"""
    
    def test_multiplicar_positivos(self):
        """Test: multiplicar números positivos"""
        assert multiplicar(3, 4) == 12
        assert multiplicar(5, 0) == 0
    
    def test_multiplicar_negativos(self):
        """Test: multiplicar números negativos"""
        assert multiplicar(-2, -3) == 6
        assert multiplicar(-4, 2) == -8


# ============================================================================
# 3️⃣ TESTS CON FIXTURES
# ============================================================================

@pytest.fixture
def datos_usuario():
    """Fixture: Datos de usuario para tests"""
    return {"nombre": "Juan", "rol": "admin", "edad": 30}


@pytest.fixture
def numeros():
    """Fixture: Lista de números para tests"""
    return [1, 2, 3, 4, 5]


def test_usuario_rol(datos_usuario):
    """Test: Verificar rol del usuario"""
    assert datos_usuario["rol"] == "admin"


def test_usuario_edad(datos_usuario):
    """Test: Verificar que el usuario es mayor de edad"""
    assert datos_usuario["edad"] >= 18


def test_numeros_contenido(numeros):
    """Test: Verificar contenido de la lista"""
    assert 3 in numeros
    assert len(numeros) == 5
    assert sum(numeros) == 15


# ============================================================================
# 4️⃣ TESTS DE EXCEPCIONES
# ============================================================================

def test_dividir_correctamente():
    """Test: División correcta"""
    assert dividir(10, 2) == 5.0
    assert dividir(100, 4) == 25.0


def test_dividir_por_cero_lanza_excepcion():
    """Test: Verifica que lanza ValueError al dividir entre cero"""
    with pytest.raises(ValueError) as excinfo:
        dividir(10, 0)
    
    # Verificar el mensaje de la excepción
    assert "cero" in str(excinfo.value).lower()


def test_dividir_por_cero_mensaje_especifico():
    """Test: Verifica el mensaje exacto de la excepción"""
    with pytest.raises(ValueError) as excinfo:
        dividir(100, 0)
    
    # El mensaje debe contener "cero"
    assert str(excinfo.value) == "No se puede dividir entre cero"


def test_dividir_normal_no_lanza_excepcion():
    """Test: Verifica que NO lanza excepción en división normal"""
    # Esto no debe lanzar excepciones
    resultado1 = dividir(15, 3)
    resultado2 = dividir(7, 1)
    
    assert resultado1 == 5.0
    assert resultado2 == 7.0


# ============================================================================
# 5️⃣ FIXTURES AVANZADAS: LEER DESDE ARCHIVOS
# ============================================================================

@pytest.fixture
def usuarios_validos():
    """Fixture: Carga usuarios desde archivo txt existente"""
    config_path = "usuarios.txt"
    
    # Leer y procesar el archivo (ya existe en la carpeta)
    usuarios = []
    with open(config_path, "r") as f:
        for linea in f:
            nombre, contraseña = linea.strip().split(":")
            usuarios.append({"nombre": nombre, "contraseña": contraseña})
    
    yield usuarios  # Proporciona datos al test


def test_cantidad_usuarios(usuarios_validos):
    """Test: Verifica que hay 3 usuarios"""
    assert len(usuarios_validos) == 3


def test_primer_usuario_es_admin(usuarios_validos):
    """Test: El primer usuario es admin"""
    assert usuarios_validos[0]["nombre"] == "admin"


def test_todos_usuarios_tienen_contraseña(usuarios_validos):
    """Test: Todos los usuarios tienen contraseña"""
    for usuario in usuarios_validos:
        assert "contraseña" in usuario
        assert len(usuario["contraseña"]) > 0


# ============================================================================
# 6️⃣ TESTS CON PARAMETRIZACIÓN
# ============================================================================

@pytest.mark.parametrize("a,b,resultado", [
    (2, 3, 5),
    (10, 20, 30),
    (-1, 1, 0),
    (0, 0, 0),
    (-5, -3, -8),
])
def test_sumar_parametrizado(a, b, resultado):
    """Test parametrizado: prueba múltiples valores para sumar"""
    assert sumar(a, b) == resultado


@pytest.mark.parametrize("a,b,resultado", [
    (2, 3, 6),
    (4, 5, 20),
    (-2, -3, 6),
    (5, 0, 0),
    (10, 1, 10),
])
def test_multiplicar_parametrizado(a, b, resultado):
    """Test parametrizado: prueba múltiples valores para multiplicar"""
    assert multiplicar(a, b) == resultado


@pytest.mark.parametrize("dividendo,divisor,resultado", [
    (10, 2, 5.0),
    (15, 3, 5.0),
    (100, 4, 25.0),
    (7, 1, 7.0),
    (20, 5, 4.0),
])
def test_dividir_parametrizado(dividendo, divisor, resultado):
    """Test parametrizado: prueba múltiples divisiones correctas"""
    assert dividir(dividendo, divisor) == resultado


@pytest.mark.parametrize("dividendo,divisor", [
    (10, 0),
    (100, 0),
    (-5, 0),
    (0, 0),
])
def test_dividir_por_cero_parametrizado(dividendo, divisor):
    """Test parametrizado: verifica excepciones con múltiples valores"""
    with pytest.raises(ValueError):
        dividir(dividendo, divisor)


# ============================================================================
# RESUMEN
# ============================================================================
"""
🎯 Cómo ejecutar estos tests desde terminal:

    # Ejecutar todos los tests
    pytest test_ejemplo.py
    
    # Con output detallado
    pytest test_ejemplo.py -v
    
    # Con prints visibles
    pytest test_ejemplo.py -vs
    
    # Ejecutar solo una clase de tests
    pytest test_ejemplo.py::TestSuma
    
    # Ejecutar solo un test
    pytest test_ejemplo.py::TestSuma::test_sumar_positivos
    
    # Mostrar el resumen de cobertura
    pytest test_ejemplo.py --cov
"""
