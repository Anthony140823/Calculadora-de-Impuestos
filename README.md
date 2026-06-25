# 💰 Calculadora de Impuestos en Python

Proyecto desarrollado en Python para calcular el monto total de un pago después de aplicar un porcentaje de impuesto definido por el usuario.

Este ejercicio forma parte de una serie de proyectos prácticos enfocados en fortalecer los fundamentos de programación y el uso de funciones en Python.

---

# 📌 Descripción

La aplicación solicita al usuario un monto base y un porcentaje de impuesto. Posteriormente calcula el valor final utilizando una función dedicada a realizar la operación matemática y muestra el resultado en pantalla.

La fórmula utilizada es:

```text
pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
```

---

# 🎯 Objetivos del Proyecto

* Practicar la creación de funciones.
* Utilizar parámetros y valores de retorno.
* Aplicar fórmulas matemáticas mediante programación.
* Implementar entrada y salida de datos por consola.
* Introducir el uso de anotaciones de tipos (Type Hints).

---

# 🚀 Características

✅ Solicita el monto base del pago.

✅ Solicita el porcentaje de impuesto.

✅ Calcula automáticamente el total a pagar.

✅ Utiliza una función para encapsular la lógica del cálculo.

✅ Devuelve el resultado mediante un valor de retorno.

✅ Muestra el resultado con formato decimal.

---

# 🛠️ Tecnologías Utilizadas

* Python 3
* Funciones
* Parámetros
* Valores de retorno
* Type Hints
* Entrada y salida de datos por consola

---

# 📂 Estructura del Proyecto

```text
calculadora-impuestos/
│
├── main.py
└── README.md
```

---

# ⚙️ Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/Anthony140823/Calculadora-de-Impuestos.git
```

## 2. Acceder al directorio

```bash
cd RETO-CALCULADORA DE IMPUESTOS
```

## 3. Ejecutar el programa

```bash
python main.py
```

---

# ▶️ Uso

Al ejecutar el programa se solicitarán los siguientes datos:

```text
Proporcione el pago sin impuesto:
Proporcione el monto del impuesto:
```

### Ejemplo

```text
Proporcione el pago sin impuesto: 100
Proporcione el monto del impuesto: 18

Pago con impuesto: 118.00
```

---

# 🔍 Explicación de la Lógica

La función principal recibe dos parámetros:

* `pago_sin_impuesto`: monto base del producto o servicio.
* `impuesto`: porcentaje de impuesto a aplicar.

```python
def calcular_total_pago(pago_sin_impuesto: float, impuesto: float):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total
```

Posteriormente, el resultado calculado es mostrado al usuario con dos decimales.

---

# 🧠 Conceptos Aplicados

Durante el desarrollo de este proyecto se practicaron los siguientes conceptos:

* Definición de funciones.
* Parámetros de entrada.
* Valores de retorno.
* Operaciones matemáticas.
* Variables locales.
* Captura de datos mediante `input()`.
* Conversión de tipos con `float()`.
* Formateo de cadenas utilizando f-strings.
* Anotaciones de tipos (`type hints`).

---

# 📈 Aprendizajes Obtenidos

Este proyecto permitió comprender cómo encapsular lógica de negocio dentro de funciones reutilizables y cómo utilizar parámetros para realizar cálculos dinámicos según los datos ingresados por el usuario.

También reforzó el uso de valores de retorno para separar el procesamiento de datos de la presentación de resultados.

---

# 🔮 Mejoras Futuras

Algunas mejoras que podrían implementarse en futuras versiones:

* Validar que los valores ingresados sean numéricos.
* Manejar errores mediante `try-except`.
* Permitir calcular múltiples operaciones sin reiniciar el programa.
* Agregar soporte para diferentes tipos de impuestos.
* Crear una interfaz gráfica utilizando Tkinter.
* Implementar pruebas unitarias para verificar los cálculos.

---

# 👨‍💻 Autor

**Anthony JeanPaul Reyes Risco**

Desarrollador de software en formación enfocado en fortalecer sus habilidades mediante proyectos prácticos y la construcción de un portafolio sólido en Python.

---

# 📄 Licencia

Proyecto desarrollado con fines educativos y de aprendizaje.
