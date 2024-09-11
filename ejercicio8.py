'''
nombre: Sofia
apellido: Lisi Azaldegui
---
Enunciado:
Genere un segundo módulo en el cual existan las funciones necesarias para la gestión del
equipo de recursos humanos de la empresa.
En el mismo debe existir una primera función que calcule el valor del salario de cada
empleado. El valor del mismo es la cantidad de horas trabajadas multiplicadas por 10 y un
incremento del 3% por cada año de antigüedad.
También debe haber una segunda función que calcule la productividad del empleado. La
misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de
horas de trabajo.
En tercer lugar debe haber una función que reporte toda la información del empleado
incluyendo la calculada en las dos funciones anteriores, nombre y edad.

'''
#> <
#{ }

def calculo_salario (cant_horas_trabajadas: float, años_de_antiguedad: int) -> float:
    '''
    calculo salario + cantidad de horas trabajadas y años de antiguedad

    ------

    retorna el salario total
    '''

    salario_total = cant_horas_trabajadas * 10 * (1 + (años_de_antiguedad * 3 / 100))
    return salario_total

def calculo_productividad (cantidad_artefactos: int, cant_horas_trabajadas: float) -> float:
    '''
    calculo productividad + cantidad de artefactos producidos y cantidad de horas trabajadas

    ------

    retorna la productividad del empleado
    '''
    productividad_total = cantidad_artefactos / cant_horas_trabajadas
    return productividad_total

def mostrar_datos (nombre_empleado: str, edad_empleado: int , salario_total: float , productividad_total: float) -> float:
    
    ''' 
    muestro datos del empleado por pantalla 
    nombre del empleado, edad empleado, salario total y productividad 
    ''' 

    print(f"nombre: {nombre_empleado}")
    print(f"edad: {edad_empleado}")
    print(f"salario: {salario_total}")
    print(f"salario: {productividad_total}")


