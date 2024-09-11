'''
nombre: Sofia
apellido: Lisi Azaldegui
---
Enunciado:
importacion de funciones 
'''

from paquete import funciones as fn  # Importamos el módulo con todas las funciones

valor_ventas_nacionales = fn.solicitarventasnacionales(resultado_ventas_nacional)  #Solicitar ventas nacionales 

valor_ventas_exportaciones = fn.solicitarexportaciones(resultado_exportaciones) # solicitar exportaciones 

calcular_impuestos = fn.calcularimpuestos(resultado_final)  # calcular y mostrar el resultado

print(f"\nEl valor total con impuestos incluidos es: {resultado_final}")

'''
-------------
'''
from Paquete import funciones as fn

salario_total = fn.solicitarsalariototal(salario_total)  #Solicitar salario total

productividad_total = fn.solicitarproductividad(productividad_total) # solicitar productividad del empleado 

mostrar_datos = fn.solicitardatos(mostrar_datos)  # mostrar los datos del empleado

print(f"datos del empleado:, {nombre_empleado}, {edad_empleado}, {salario_total},{productividad_total} ")
