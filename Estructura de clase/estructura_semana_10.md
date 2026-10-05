
### Clase 1: Geometría de la Rotación y Áreas (Producto Cruz en $\mathbb{R}^3$)

**1. Información General**

* **Tema:** Transición del producto escalar al producto vectorial, cálculo analítico, dirección (mano y tornillo) y áreas.
* **Competencia:** Calcular el producto cruz para determinar vectores ortogonales y modelar áreas de superficies en el espacio tridimensional.
* **Recursos:** Modelos físicos (un tornillo y tuerca grandes), GeoGebra 3D.

**2. Apertura (10 min)**

* **Reto:** Proyecta la imagen de un panel solar inclinado en el espacio y una ráfaga de viento golpeándolo.
* **Preguntas Motivadoras:**
1. Hasta ahora, el producto punto nos entregaba un escalar (energía, costo). Si necesitamos calcular una nueva *dirección* perpendicular donde actúa la fuerza del viento, ¿nos sirve el producto punto?
2. ¿Por qué una herramienta geométrica que genera nuevas direcciones perpendiculares está limitada estrictamente a nuestro espacio tridimensional ($\mathbb{R}^3$)?
3. Si cambiamos el orden de los vectores que definen el panel, ¿el viento golpea por arriba o por abajo?



**3. Exploración (5 min)**

* Entrega un tornillo grande a cada grupo. Pídeles que simulen el giro de un vector $u$ hacia un vector $v$ (girando la cabeza del tornillo). Los estudiantes deben observar y anotar en qué dirección se desplaza el cuerpo del tornillo a medida que ocurre el giro.

**4. Desarrollo Conceptual (15 min)**

* **La Ecuación:** Introduce la fórmula matemática, enfatizando que genera un nuevo vector, no un escalar:

$$u \times v = (b_1c_2 - c_1b_2)i + (c_1a_2 - a_1c_2)j + (a_1b_2 - b_1a_2)k$$


* **Sentido y Dirección:** Explica la regla de orientación:
* *El Tornillo:* Rotar desde $u$ hacia $v$ define el avance (hacia arriba o hacia abajo).
* *La Mano:* Utiliza la mano izquierda/derecha como convención espacial; el pulgar indica el vector resultante perpendicular al plano formado por los dedos índice y medio.


* **Magnitud:** Define $\vert{}u \times v\vert{} = \vert{}u\vert{}\vert{}v\vert{} \sin(\omega)$. Demuestra geométricamente que esta magnitud equivale exactamente al **área del paralelogramo** que tiene como lados adyacentes a $u$ y $v$.

**5. Actividad Guiada y Colaborativa (15 min)**

* Asigna a cada grupo dos vectores $u$ y $v$ en $\mathbb{R}^3$ con coeficientes pequeños.
* *Roles:* Un estudiante calcula los componentes $i, j$, otro calcula el componente $k$ y verifica signos, y el tercero verifica la ortogonalidad calculando el producto punto $(u \times v) \cdot u = 0$.

**6. Aplicación (10 min)**

* **Reto de Ingeniería Civil:** Un toldo de tensión está definido por tres puntos de anclaje en el espacio. Los estudiantes deben convertir los puntos en dos vectores adyacentes y calcular el área exacta de lona necesaria utilizando la magnitud del producto cruz. Utilizan Colab (`np.cross` y `np.linalg.norm`) para acelerar el cálculo.

**7. Cierre y Reflexión (3 min)**

* ¿Qué significa físicamente para nuestra cubierta de lona si el ángulo $\omega$ entre los dos vectores de anclaje es cero o $180^\circ$ (colineales)?

**8. Actividad Final de Consolidación (2 min)**

* **Ticket de Salida Visual:** En una hoja, dibujan dos vectores en un plano y una flecha perpendicular. Deben indicar con una "T" hacia dónde avanza el tornillo si multiplican $v \times u$ en lugar de $u \times v$.

---

### Clase 2: Propiedades del Producto y el Triple Producto Escalar

**1. Información General**

* **Tema:** Anticonmutatividad, distributividad, el triple producto escalar y volúmenes.
* **Competencia:** Aplicar propiedades algebraicas para simplificar cálculos de productos vectoriales y modelar el volumen de sólidos geométricos.
* **Recursos:** Google Colab, cajas de cartón (paralelepípedos) deformables si es posible.

**2. Apertura (10 min)**

* **Reto:** Muestra el cálculo de rotación de un brazo robótico en una fábrica. El ingeniero programó $u \times v$ para mover la pieza a la cinta transportadora, pero por error digitó $v \times u$.
* **Preguntas Motivadoras:**
1. A diferencia de los números reales ($3 \times 4 = 4 \times 3$), ¿qué catástrofe física ocurrió en la fábrica con este error de código?
2. ¿Es posible multiplicar tres vectores combinando los dos mundos que conocemos (el punto y la cruz)?
3. ¿Qué representa la "caja" o sombra 3D proyectada por tres vectores diferentes que parten de un mismo origen?



**3. Exploración (5 min)**

* Sin darles la regla, pide a los grupos que calculen rápidamente $i \times j$ y luego $j \times i$ usando la fórmula del determinante de la clase pasada. Deben formular una hipótesis sobre el comportamiento del signo.

**4. Desarrollo Conceptual (15 min)**

* **Propiedades:** Formaliza la **propiedad anticonmutativa** ($u \times v = -(v \times u)$) y la **propiedad distributiva** ($u \times (v + w) = (u \times v) + (u \times w)$).
* **El Triple Producto Escalar:** Presenta la operación híbrida $u \cdot (v \times w)$.
* **Interpretación Geométrica:** Explica que el escalar absoluto derivado de $u \cdot (v \times w)$ representa el **volumen del paralelepípedo** determinado por los vectores $u, v, w$.

**5. Actividad Guiada y Colaborativa (15 min)**

* Los equipos reciben tres vectores que representan las aristas de una celda cristalina (Ciencia de Materiales).
* Paso 1: Calculan el área de la base ($v \times w$).
* Paso 2: Calculan el producto punto del resultado con $u$ para hallar el volumen total.

**6. Aplicación (10 min)**

* **Validación Computacional:** Los estudiantes implementan en Python las propiedades. Deben programar una celda que arroje un valor `True` al verificar que `np.cross(u, v)` es igual a `-np.cross(v, u)` y luego calcular el volumen de un sistema de embalaje logístico de 3 variables.

**7. Cierre y Reflexión (3 min)**

* Si programamos un modelo en 3D de tres vectores y el triple producto escalar nos da un volumen exactamente igual a $0$, ¿qué nos dice esto sobre la ubicación de los tres vectores en el espacio real? (Están aplastados en un solo plano / son coplanarios).

**8. Actividad Final de Consolidación (2 min)**

* **Quiz Rápido:** Proyecta tres matrices (una de $u \times v$, otra demostrando la anticonmutatividad y una de volumen). Los estudiantes votan con señales manuales si la operación arrojará un *Vector* o un *Escalar*.
### Clase 1: Cobertura de Riesgos y Activos No Correlacionados (Producto Cruz en $\mathbb{R}^3$)

**1. Información General**

* **Tema:** Cálculo del producto cruz y su aplicación para encontrar vectores ortogonales (activos no correlacionados).
* **Competencia:** Utilizar el producto vectorial en $\mathbb{R}^3$ para diseñar instrumentos financieros sintéticos que sirvan como cobertura perfecta de riesgo ante otros dos activos.
* **Nivel:** Ciencias Económicas, Finanzas y Negocios. Modalidad Presencial (1 hora).
* **Recursos:** Google Colab (Python) o Microsoft Excel, Pizarras.

**2. Apertura (El Reto - 10 min)**

* **Reto:** Proyecta la pantalla de una terminal de Bloomberg simulada. Tu fondo de inversión ya tiene dos grandes paquetes de acciones (Vector $u$ y Vector $v$) cuyos rendimientos proyectados en 3 escenarios económicos (Optimista, Neutro, Pesimista) están definidos en $\mathbb{R}^3$. El CEO exige incorporar un tercer activo que sirva de "cobertura perfecta": debe tener **cero correlación** (ser ortogonal) con $u$ y con $v$ simultáneamente.
* **Preguntas Motivadoras:**
1. Usando el producto punto, podemos saber si dos activos están correlacionados, pero ¿cómo "fabricamos" o descubrimos desde cero un tercer activo que no tenga relación con los otros dos?
2. Si imaginamos los rendimientos de nuestros dos fondos actuales como un plano, ¿hacia dónde debe apuntar nuestro nuevo fondo para no chocar con ellos?
3. ¿Qué pasaría con el riesgo de nuestro portafolio si logramos encontrar este activo matemáticamente "perpendicular"?



**3. Exploración (5 min)**

* En parejas, los estudiantes formulan hipótesis: Si el Fondo $u = (1, 1, 0)$ y el Fondo $v = (0, 1, 1)$, ¿qué números intuitivamente le pondrían al Fondo $w$ para que su producto punto con $u$ y con $v$ sea exactamente cero?

**4. Desarrollo Conceptual (15 min)**

* **La Ecuación (El Creador de Activos):** Introduce la fórmula del producto cruz $u \times v$. Explica que este es un "motor" matemático que toma dos vectores y escupe un tercer vector 100% ortogonal a ambos.
* **Interpretación Financiera:**
* *La dirección:* El nuevo vector resultante indica las ponderaciones (pesos) de un portafolio sintético de cobertura.
* *La magnitud (Área):* $\vert{}u \times v\vert{}$ representa la "prima de diversificación" o el grado de independencia entre los dos activos originales.


* **Verificación:** ¿Qué significaría para nuestro portafolio de negocios si al calcular $u \times v$ el resultado es el vector nulo $(0,0,0)$? (Respuesta esperada: Los activos $u$ y $v$ son colineales, se comportan igual; no hay diversificación).

**5. Actividad Guiada y Colaborativa (15 min)**

* Los grupos reciben dos vectores de $\mathbb{R}^3$ que representan flujos de caja de dos proyectos de inversión en tres años distintos.
* Calculan manualmente el producto cruz para encontrar el "Proyecto C", cuya estructura de flujo de caja proteja a la empresa (sea ortogonal) de las fluctuaciones de los Proyectos A y B.
* Comprueban la ortogonalidad calculando que $(A \times B) \cdot A = 0$.

**6. Aplicación (10 min)**

* **Reto en Colab/Excel:** Los estudiantes reciben un dataset de 3 escenarios de mercado. Usando `np.cross()` en Python, deben hallar el vector de inversión ortogonal para dos criptomonedas altamente volátiles.

**7. Cierre y Reflexión (3 min)**

* Si el producto cruz nos entrega un activo con pesos negativos en ciertos escenarios, ¿qué acción financiera real representa un "peso negativo" en los mercados? (Posiciones en corto o *short selling*).

**8. Actividad Final de Consolidación (2 min)**

* **One-Minute Paper:** Escribe en un párrafo por qué el producto cruz es una herramienta para la gestión de riesgos y no solo para calcular áreas geométricas.

---

### Clase 2: Auditoría de Portafolios y Activos Redundantes (Triple Producto Escalar)

**1. Información General**

* **Tema:** Propiedades del producto cruz, el triple producto escalar y su interpretación analítica.
* **Competencia:** Evaluar la dependencia lineal y la diversificación de un portafolio de tres activos mediante el cálculo del "volumen" financiero (triple producto escalar).
* **Nivel:** Ciencias Económicas, Finanzas y Negocios. Modalidad Presencial (1 hora).
* **Recursos:** Pizarras, Google Colab.

**2. Apertura (El Reto - 10 min)**

* **Reto:** Un banco de inversión te ofrece venderte tres estrategias comerciales diferentes ($u, v, w$) para operar en 3 mercados (Divisas, Bonos, Acciones). Te cobran una comisión altísima argumentando que te ofrecen "cobertura tridimensional total".
* **Preguntas Motivadoras:**
1. ¿Cómo podemos auditar matemáticamente si realmente nos están vendiendo 3 estrategias independientes, o si la tercera es solo una mezcla (combinación lineal) de las dos primeras disfrazada con otro nombre?
2. Si graficáramos estos tres activos y el "volumen" de la figura que forman fuera cero, ¿estamos siendo estafados?
3. Si el orden de las estrategias cambia, ¿cambia el nivel de diversificación total?



**3. Exploración (5 min)**

* Se presentan tres vectores a los grupos. Dos son evidentes ($u=(1,0,0)$ y $v=(0,1,0)$), y el tercero es $w=(2,3,0)$. Se les pide debatir si el vector $w$ aporta alguna información nueva al mercado que no pudieran replicar comprando $u$ y $v$.

**4. Desarrollo Conceptual (15 min)**

* **Propiedades Analíticas:** Formaliza rápidamente la anticonmutatividad y la distributividad, traduciéndolas a operaciones de portafolio (invertir el orden invierte la posición de largo a corto).
* **El Triple Producto Escalar:** Define $u \cdot (v \times w)$.
* **El "Volumen" Financiero:** Explica que este cálculo equivale al determinante de la matriz $3 \times 3$. En negocios, si este volumen es distinto de cero, el portafolio "abarca todo el mercado" (es una base completa). Si el volumen es $0$, los activos son coplanarios: uno de ellos es **redundante**.

**5. Actividad Guiada y Colaborativa (15 min)**

* Los equipos actúan como auditores financieros. Reciben la estructura de los 3 paquetes de inversión del Reto inicial.
* Paso 1: Calculan el "área base" hallando el producto cruz de $v$ y $w$.
* Paso 2: Realizan el producto punto con $u$.
* Paso 3: Diagnostican. Si da $0$, deben redactar un memo alertando que hay un "activo redundante" (oportunidad de arbitraje o cobro indebido de comisiones).

**6. Aplicación (10 min)**

* **Modelado Computacional:** Abren Google Colab y programan una función llamada `auditor_arbitraje(u, v, w)` que retorne `"Portafolio Sólido"` si el valor absoluto del triple producto escalar es mayor a un umbral, o `"Alerta: Activos Redundantes"` si es cero. Validan la función con datos proporcionados por el docente.

**7. Cierre y Reflexión (3 min)**

* En contabilidad corporativa y finanzas, ¿por qué encontrar un "volumen cero" en un sistema de ecuaciones de precios de mercado es el sueño de los analistas cuantitativos que buscan "arbitraje" (ganancias sin riesgo)?

**8. Actividad Final de Consolidación (2 min)**

* **Diagrama Lógico:** En la pizarra o cuaderno, construyen un pequeño árbol de decisiones de 3 pasos que un bot de trading usaría, aplicando el triple producto escalar para decidir si comprar un paquete de tres acciones o rechazarlo por redundancia.