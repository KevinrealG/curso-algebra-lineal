

# Clase 1

Aquí tienes el plan detallado para la **Clase 1A**, organizado fuera de la tabla para que sea más fácil de leer y seguir:

### Clase 1A: Matrices Elementales (Fundamentos)

**Información General**

* **Meta:** Dominar visual y algebraicamente las operaciones elementales de fila.
* **Modalidad:** Presencial.

---

**Apertura (10 min)**

* **Reto:** Proyecta una deformación en tu app web.
* **Preguntas para la clase:**
1. ¿Qué pasó con las coordenadas originales?
2. ¿Qué operación matricial provocó esto?
3. ¿Cómo revertimos este cambio al estado original?



**Exploración (5 min)**

* Trabajo en parejas formulando hipótesis sobre qué matriz exacta generó la deformación visual.

**Desarrollo Conceptual (10 min)**

* **Instrucción mínima:** Definición de las tres matrices elementales y su equivalencia con operaciones de fila.

**Actividad Guiada (15 min)**

* **Práctica deliberada:** Los grupos aplican matrices elementales secuenciales a un modelo $2 \times 2$ en pizarra.

**Aplicación (10 min)**

* Representar un cambio de escala o rotación simple para un nodo de ingeniería estructural.

**Cierre y Reflexión (5 min)**

* **Debate:** ¿Toda transformación de filas es geométricamente reversible?

**Actividad Final (5 min)**

* Quiz rápido de emparejamiento visual (operación vs. matriz resultante).
Generating slides ...



Your slide deck on Matrices Elementales e Inversa (Semana 3) is ready! Feel free to take a look and let me know if you'd like to make any edits.

Aquí tienes la **Planeación Detallada de las Sesiones** bajo la metodología de aprendizaje activo solicitada:

# 3 **Clase 1: Miércoles (2 Horas)**

**1. Información General**

* **Temas:** Matrices elementales y algoritmo de Gauss-Jordan para la inversa.
* **Resultados de Aprendizaje:** Comprender la conexión geométrica y algebraica de las matrices elementales y aplicar el método de Gauss-Jordan a casos aplicados.
* **Competencias:** Abstracción, modelado matemático y trabajo colaborativo.

**2. Recursos Previos (Flipped Classroom)**

* **En SAVIO:** Asignar un video corto (5-7 min) interactivo sobre "La idea intuitiva de deshacer una transformación" y un artículo corto sobre el Modelo de Leontief.

**3. Plan de Clase**

* **Apertura (20 min):** Inicia proyectando la *Slide 3 (Modelo Insumo-Producto)* o la *Slide 4 (Nodos en Ingeniería)*. Plantea un sistema $3 \times 3$ con interdependencias económicas. **Reto:** Pregunta a los estudiantes: *"Si la demanda externa cambia mañana, ¿tenemos que volver a calcular todo el sistema 3x3 por sustitución de cero?"* No des la respuesta aún, fomenta la duda cognitiva.
* **Exploración (15 min):** Pide que debatan en grupos de 3 cómo crearían un "atajo matemático" que, al multiplicarlo por el nuevo vector de demanda, les dé la producción automáticamente.
* **Desarrollo Conceptual (30 min):** Usando las diapositivas 5 a 8, introduce formalmente las **3 Matrices Elementales**. Explica que operar filas es multiplicar por matrices. Luego, formaliza el algoritmo de Gauss-Jordan $[A\vert{}I] \to [I\vert{}A^{-1}]$ (*Slide 8*).
* **Actividad Guiada y Colaborativa (35 min):** Asigna a cada grupo una matriz $3 \times 3$ (un grupo la matriz económica de Leontief, otro la matriz de rigidez estructural). Deben aplicar operaciones elementales en pizarra o papel para hallar la matriz inversa de forma colaborativa. El docente actúa estrictamente como facilitador y validador.
* **Aplicación (10 min):** Una vez hallada la inversa, dales un "vector de carga externa" o "vector de demanda". Deben multiplicar $A^{-1} \times b$ para hallar la solución final, evidenciando la utilidad del concepto en el mundo real.
* **Cierre y Reflexión (10 min):** Proyecta la *Slide 7* y cierra con la pregunta: *"¿Qué significa en la economía o en el puente que el Determinante sea cero y no podamos hallar la Inversa?"*.

---

# Clase 2
Aquí tienes el plan detallado para la **Clase 1B**, siguiendo exactamente el mismo formato:

### Clase 1B: Gauss-Jordan e Inversa (Aplicación)

**Información General**

* **Meta:** Aplicar el algoritmo de Gauss-Jordan para invertir matrices en contextos reales.
* **Modalidad:** Presencial.

---

**Apertura (10 min)**

* **Reto:** Plantea un modelo de interdependencia económica.
* **Preguntas para la clase:**
1. Si la demanda cambia a diario, ¿debemos recalcular todo?
2. ¿Existe un "botón deshacer" matricial?
3. ¿Cómo construiríamos esa matriz?



**Exploración (5 min)**

* Estudiantes intentan idear un método para aislar las variables del sistema económico sin usar sustitución.

**Desarrollo Conceptual (10 min)**

* **Instrucción mínima:** Estructura del algoritmo de Gauss-Jordan empleando la matriz aumentada $[A\vert{}I] \to [I\vert{}A^{-1}]$.

**Actividad Guiada (15 min)**

* **Cálculo colaborativo:** Los grupos resuelven una matriz $3 \times 3$, asumiendo roles para verificar cada paso de fila.

**Aplicación (10 min)**

* Multiplicar la matriz inversa calculada por un vector de nueva demanda para resolver el modelo económico.

**Cierre y Reflexión (5 min)**

* **Debate:** ¿Qué significa físicamente o financieramente que un sistema no tenga matriz inversa?

**Actividad Final (5 min)**

* Elaboración de un diagrama de flujo rápido que resuma el proceso de inversión.

# Clase 3

**1. Información General**

* **Tema:** Examen 1 (Matrices y operaciones con matrices).
* **Valoración:** 25%.

**2. Recursos Previos**

* **En SAVIO:** Simulación de cuestionario formativo (Quiz auto-evaluable sin nota) para que practiquen autorregulación antes de la prueba.

**3. Plan de Clase**

* **Apertura (10 min):** Proyecta la *Slide 10* y establece el encuadre. Lee en voz alta un problema aplicado del examen para asegurar que no existan ambigüedades en la redacción y aclarar el contexto de ingeniería o finanzas.
* **Ejecución (40 min):** Desarrollo del examen de forma individual. El docente recorre el aula monitoreando el comportamiento ético y resolviendo dudas exclusivamente de redacción.
* **Cierre y Reflexión (10 min):** Recolección del examen. Realiza un sondeo a mano alzada muy rápido (*"¿Qué punto consideraron que requirió más análisis computacional/abstracto?"*) para validar el nivel de dificultad percibido y bajar la ansiedad de los estudiantes antes de finalizar la semana.