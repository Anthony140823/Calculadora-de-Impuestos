'''
        EJERCICIO: CALCULADORA DE IMPUESTOS

Crear una función para calcular el total de un pago 
incluyedno un impuesto aplicado.

FORMULA: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
'''
# Función para calcular el pago total
def calcular_total_pago(pago_sin_impuesto:float, impuesto:float):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutamos la función
pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
impuesto = float(input("Proporcione el monto del impuesto: "))

pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto:.2f}')