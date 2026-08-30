Problema 1: Planta de Producción de Bebidas
Contexto

Una empresa de bebidas produce tres tipos de productos:

Refresco (R)
Jugo (J)
Agua saborizada (A)

Durante una jornada de producción intervienen tres áreas:

Mezclado (M)
Embotellado (E)
Empaque (P)

Al finalizar el día se registró el tiempo total utilizado en cada área:

Mezclado: 52 horas
Embotellado: 43 horas
Empaque: 35 horas

Las horas requeridas por lote producido son:

Proceso	Refresco	Jugo	Agua saborizadaMezclado	4 h	2 h	3 h
Embotellado	3 h	3 h	2 h
Empaque	2 h	1 h	3 h
Parte 1: Sistemas de ecuaciones lineales

a) Plantee el sistema de ecuaciones lineales que modela la situación.

b) Identifique la matriz de coeficientes AA y el vector de términos independientes bb.

c) Encuentre la inversa de AA.

d) Utilice el método matricial para determinar cuántos lotes de cada bebida se produjeron.

import sympy as sp

A = sp.Matrix([
    [4, 2, 3],
    [3, 3, 2],
    [2, 1, 3]
])

b = sp.Matrix([52, 43, 35])

A_inv = A.inv()

x = A_inv * b

print("Matriz inversa:")
sp.pprint(A_inv)

print("\nSolución:")
sp.pprint(x)

Parte 2: Multiplicación de matrices y análisis

Los costos por hora de operación son:

Proceso	Turno Regular ($/h)	Turno Nocturno ($/h)Mezclado	50.000	75.000
Embotellado	65.000	98.000
Empaque	40.000	60.000

Sea

V=[500007500065000980004000060000]V= \begin{bmatrix} 50000 & 75000\\ 65000 & 98000\\ 40000 & 60000 \end{bmatrix}

a) Calcule P=A⋅VP=A\cdot V.

b) Interprete el significado de cada fila y cada columna de la matriz resultante.

c) ¿Cuál de las bebidas resulta más costosa de producir en turno regular?

d) ¿Cuál experimenta el mayor incremento de costo al pasar de turno regular a nocturno?

import numpy as np

A = np.array([
    [4,2,3],
    [3,3,2],
    [2,1,3]
])

V = np.array([
    [50000,75000],
    [65000,98000],
    [40000,60000]
])

P = A @ V

print(P)

Problema 2: Empresa de Desarrollo de Software
Contexto

Una compañía tecnológica desarrolla tres tipos de proyectos:

Aplicaciones Web (W)
Aplicaciones Móviles (M)
Sistemas Empresariales (S)

Cada proyecto requiere horas de trabajo en tres departamentos:

Diseño (D)
Programación (PR)
Pruebas (T)

Durante un mes se emplearon:

75 horas en Diseño
122 horas en Programación
58 horas en Pruebas

Las horas necesarias por proyecto son:

Departamento	Web	Móvil	EmpresarialDiseño	3	2	4
Programación	5	4	6
Pruebas	2	1	3
Parte 1: Sistema de ecuaciones lineales

a) Formule el sistema de ecuaciones lineales correspondiente.

b) Construya la matriz de coeficientes AA y el vector bb.

c) Determine A−1A^{-1}.

d) Calcule el número de proyectos de cada tipo desarrollados durante el mes.

import sympy as sp

A = sp.Matrix([
    [3,2,4],
    [5,4,6],
    [2,1,3]
])

b = sp.Matrix([
    75,
    122,
    58
])

A_inv = A.inv()

x = A_inv*b

print(x)

Parte 2: Multiplicación de matrices y análisis

Los costos por hora en cada departamento son:

Departamento	Personal Junior ($/h)	Personal Senior ($/h)Diseño	90.000	130.000
Programación	120.000	180.000
Pruebas	80.000	115.000

Sea:

V=[9000013000012000018000080000115000]V= \begin{bmatrix} 90000 & 130000\\ 120000 & 180000\\ 80000 & 115000 \end{bmatrix}

a) Calcule P=A⋅VP=A\cdot V.

b) Interprete el significado de la matriz obtenida.

c) ¿Cuál tipo de proyecto genera el mayor costo con personal junior?

d) ¿Cuál proyecto presenta el mayor aumento de costos cuando se utilizan equipos senior?

import numpy as np

A = np.array([
    [3,2,4],
    [5,4,6],
    [2,1,3]
])

V = np.array([
    [90000,130000],
    [120000,180000],
    [80000,115000]
])

P = A @ V

print(P)


Estos dos problemas permiten evaluar simultáneamente:

Planteamiento de sistemas de ecuaciones lineales.
Interpretación de matrices.
Inversa de matrices.
Solución matricial X=A−1bX=A^{-1}b.
Multiplicación de matrices.
Interpretación contextual de productos matriciales.
Análisis y toma de decisiones a partir de resultados.