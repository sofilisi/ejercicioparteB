'''
nombre: Sofia
apellido: Lisi Azaldegui
---
Enunciado:
Supongamos que le solicito a chatgpt una función para calcular valores de ventas de
productos con impuestos para una determinada empresa:
La respuesta de chatgpt es:
def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones
= 15):
resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
resultado_final = resultado_nacional + resultado_exportaciones
return resultado_final
¿Considera que cumple con los objetivos de una función?
Corrija la función dentro de un módulo, divida en distintas funciones de ser necesario,
documente y denomine correctamente.
'''
#> <


def calcular_ventas_nacionales (valor_ventas_nacionales: float, iva: float) -> float:

    '''
    calculo ventas nacionales con iva 

    ------

    retorna el valor de las ventas nacionales + iva
    '''

    resultado_ventas_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
    return resultado_ventas_nacional

def calcular_ventas_exportaciones (valor_ventas_exportaciones: float, retenciones: float) -> float:
    '''
    calculo las ventas por exportaciones 

    ------

    retorna el valor de exportaciones + retenciones
    '''
    
    resultado_exportaciones = valor_ventas_exportaciones*  (1 - (retenciones / 100))
    return resultado_exportaciones

def calcular_impuestos (resultado_ventas_nacional: float, resultado_exportaciones: float) -> float:
    '''
    calculo el resultado de  las ventas nacionales y el resultado de exportaciones

    ------

    retorna el total de ventas nacionales y exportaciones con sus impuestos
    '''
    resultado_final = resultado_ventas_nacional + resultado_exportaciones
    return resultado_final

