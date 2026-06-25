'''
        EJERCICIO: CALCULADORA DE IMPUESTOS

Crear una función para calcular el total de un pago 
incluyedno un impuesto aplicado.

FORMULA: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
'''
pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
impuesto = float(input("Proporcione el monto del impuesto: "))

# Función para calcular el pago total
def total(pago_sin_impuesto:float, impuesto:float):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    print(f'Pago con impuesto: {pago_total:.2f}')

total(pago_sin_impuesto, impuesto)