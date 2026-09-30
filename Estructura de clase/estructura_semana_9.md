### Propuesta de Recurso Digital: "Scouting AI: El Ángulo de Similitud"

Para conectar el álgebra lineal con los intereses de estudiantes de ingeniería y economía, desarrollaremos conceptualmente (y en código para Google Colab/Streamlit) una aplicación de *Scouting* deportivo o corporativo.

* **En $\mathbb{R}^2$:** Analizamos dos métricas (ej. Velocidad vs. Fuerza). Los estudiantes visualizan los vectores en un plano.
* **En $\mathbb{R}^3$:** Añadimos una tercera métrica (ej. Resistencia). Se visualiza en un gráfico 3D interactivo con Plotly.
* **En $\mathbb{R}^n$:** Un jugador de fútbol real (o un perfil de riesgo financiero) tiene decenas de métricas (Pases, Tiros, Intercepciones, etc.). Aunque no podemos graficarlo espacialmente, la aplicación utiliza la **Similitud del Coseno** (el ángulo entre dos vectores en $\mathbb{R}^n$) para responder a la pregunta: *"¿Qué jugador es matemáticamente más similar a Lionel Messi o a un perfil de empleado ideal?"*.

---

### Clase 1: De la Geometría a los Datos (Vectores en $\mathbb{R}^3$ y $\mathbb{R}^n$)

**1. Información General**

* **Tema:** Vectores en el espacio tridimensional y n-dimensional.
* **Competencia:** Modelar entidades complejas del mundo real mediante arreglos vectoriales en $n$-dimensiones, superando la restricción visual geométrica.
* **Recursos:** Pizarras, App "Scouting AI" (fase visual $\mathbb{R}^2$ y $\mathbb{R}^3$).

**2. Apertura (10 min)**

* **Reto:** Proyecta un gráfico radar (telaraña) de un jugador de fútbol famoso o un análisis de riesgo de una acción bursátil con 8 variables distintas. https://kevinrealg.github.io/curso-algebra-lineal/Dispositivas%20Clase/app.html 
* **Preguntas Motivadoras:**
1. Si en un plano cartesiano ($\mathbb{R}^2$) necesitamos 2 coordenadas para ubicar un punto, ¿cuántas coordenadas necesitamos para definir matemáticamente a este producto?
2. ¿Es posible dibujar un espacio de 5 dimensiones?
3. Si no podemos dibujarlo, ¿significa que sus propiedades matemáticas (como la suma de habilidades) dejan de existir?



**3. Exploración (5 min)**

* En grupos de 3, los estudiantes deben inventar un "jugador" o "producto" asignándole valores del 1 al 10 en cinco categorías diferentes, escribiéndolo con el formato $v = (x_1, x_2, x_3, x_4, x_5)$.

**4. Desarrollo Conceptual (10 min)**

* Formaliza la definición matemática de un vector en $\mathbb{R}^n$ como una n-tupla ordenada.
* Establece la conexión: Un vector ya no es solo "una flecha en el espacio", es una **estructura de datos** o un registro en una base de datos.
* **Verificación:** ¿Qué significaría en la vida real multiplicar el vector de nuestro jugador por un escalar $k = 1.5$?

**5. Actividad Guiada y Colaborativa (15 min)**

* Los equipos suman sus vectores de $\mathbb{R}^5$ (simulando la creación de un "equipo" o "portafolio" combinado).
* Se introduce la representación geométrica estricta de $\mathbb{R}^3$ en la pizarra (ejes $x, y, z$). Los estudiantes grafican un vector de 3 componentes.

**6. Aplicación (10 min)**

* Proyecta la App "Scouting AI" en modo $\mathbb{R}^3$. Los estudiantes introducen 3 métricas de sus jugadores y giran el gráfico 3D para entender cómo la magnitud de cada variable cambia la dirección espacial del perfil.

**7. Cierre y Reflexión (5 min)**

* ¿Cuál es la limitación humana principal al trabajar con vectores en Data Science, Finanzas o Ingeniería, y por qué el álgebra es nuestra única forma de "ver" en la oscuridad de $\mathbb{R}^n$?

**8. Actividad Final de Consolidación (5 min)**

* **One-Minute Paper:** Define con tus propias palabras la diferencia conceptual entre un vector geométrico en $\mathbb{R}^3$ y un vector de datos en $\mathbb{R}^{10}$.

---

### Clase 2: Midiendo Diferencias (Norma, Distancia y Ortogonalidad en $\mathbb{R}^n$)

**1. Información General**

* **Tema:** Producto punto básico, Norma (magnitud), Distancia Euclidiana y Ortogonalidad.
* **Competencia:** Calcular métricas de magnitud y distancia para evaluar el rendimiento general y la divergencia entre dos modelos.
* **Recursos:** Calculadoras, matrices de datos de la sesión anterior.

**2. Apertura (10 min)**

* **Reto:** Muestra dos vectores de $\mathbb{R}^4$: Jugador A = $(9, 2, 8, 1)$ y Jugador B = $(5, 5, 5, 5)$.
* **Preguntas Motivadoras:**
1. A simple vista, ¿quién es el jugador más "completo" o con mayor volumen de juego total?
2. ¿Cómo medimos la "distancia" en habilidades entre el Jugador A y el Jugador B?
3. Si un jugador solo ataca y otro solo defiende, ¿cómo se relacionan sus vectores en el espacio?



**3. Exploración (5 min)**

* Sin dar fórmulas, pide a las parejas que inventen una manera matemática de resumir los 4 números del Jugador A en un solo número que represente su "tamaño total".

**4. Desarrollo Conceptual (15 min)**

* Define el **Producto Punto** ($u \cdot v = \sum u_i v_i$).
* Deriva la **Norma** $\vert{}\vert{}v\vert{}\vert{} = \sqrt{v \cdot v}$ (como extensión del Teorema de Pitágoras).
* Deriva la **Distancia Euclidiana** $d(u,v) = \vert{}\vert{}u - v\vert{}\vert{}$.
* Define la **Ortogonalidad:** Si $u \cdot v = 0$, los vectores son perpendiculares (no comparten ninguna "sombra" de habilidades).

**5. Actividad Guiada y Colaborativa (15 min)**

* **Práctica Deliberada:** Cada grupo recibe perfiles de $\mathbb{R}^5$ de tres entidades diferentes.
* Deben calcular la Norma de cada uno para hacer un ranking de "magnitud".
* Deben calcular el producto punto entre ellos para identificar si existen perfiles ortogonales.

**6. Aplicación (5 min)**

* En ingeniería o economía, si las variables de inflación y desempleo fueran un vector ortogonal al vector de crecimiento, ¿qué implicaría esto sobre la relación entre esos fenómenos económicos? (Son linealmente independientes/no correlacionados).

**7. Cierre y Reflexión (3 min)**

* Si la distancia Euclidiana entre dos competidores es muy cercana a cero, ¿qué decisión gerencial o estratégica tomarían respecto a ellos?

**8. Actividad Final de Consolidación (2 min)**

* **Quiz Rápido de Mano Alzada:** Proyecta tres pares de vectores simples ($2 \times 2$). Los estudiantes deben indicar visualmente si su producto punto es 0 (pulgar abajo) o distinto de 0 (pulgar arriba).

---

### Clase 3: Ángulos de Similitud y Proyecciones

**1. Información General**

* **Tema:** Producto punto avanzado, ángulos entre vectores y proyecciones ortogonales.
* **Competencia:** Aplicar la similitud del coseno y la proyección vectorial para diseñar motores de recomendación y extraer componentes útiles de un conjunto de datos.
* **Recursos:** Google Colab con script de Similitud del Coseno, aplicación "Scouting AI".

**2. Apertura (10 min)**

* **Reto:** En Spotify, si te gusta una banda de Rock (Vector A), el algoritmo te recomienda otra banda (Vector B) que tiene un "volumen de reproducciones" mucho menor, pero un "estilo" idéntico.
* **Preguntas Motivadoras:**
1. Si el Jugador A tiene stats $(2, 2, 2)$ y el Jugador B tiene $(10, 10, 10)$, la distancia euclidiana entre ellos es enorme. Sin embargo, ¿sus perfiles de juego apuntan hacia el mismo lado?
2. ¿Cómo medimos matemáticamente que dos cosas son "proporcionalmente iguales" sin importar su tamaño?



**3. Exploración (5 min)**

* Los grupos dibujan en $\mathbb{R}^2$ los vectores $u = (1, 2)$ y $v = (3, 6)$. Deben debatir qué ángulo forman entre sí y cómo calcularlo sin usar un transportador.

**4. Desarrollo Conceptual (10 min)**

* Fórmula del ángulo: $\cos(\theta) = \frac{u \cdot v}{\vert{}\vert{}u\vert{}\vert{} \vert{}\vert{}v\vert{}\vert{}}$ (La base de la *Similitud del Coseno* en Machine Learning).
* Explicación de la **Proyección** $\text{proy}_v u = \left(\frac{u \cdot v}{\vert{}\vert{}v\vert{}\vert{}^2}\right) v$: "Cuánto de las habilidades del jugador A se pueden proyectar sobre el rol táctico del jugador B".

**5. Actividad Guiada y Colaborativa (15 min)**

* Los estudiantes ejecutan el cálculo del ángulo $\theta$ (usando la función inversa $\arccos$) para dos vectores de $\mathbb{R}^4$.
* Calculan la proyección vectorial de un vector sobre otro, interpretando físicamente los componentes de la ecuación.

**6. Aplicación (10 min)**

* **Simulación de la App (Colab):** Los estudiantes ingresan el perfil de un "Jugador Objetivo" en $\mathbb{R}^{10}$. Usan un bloque de código (que automatiza la fórmula del ángulo) para iterar sobre una base de datos de 5 jugadores.
* Identifican qué jugador tiene el ángulo más pequeño (mayor *Cosine Similarity*) respecto al objetivo, encontrando el "fichaje ideal" o "inversión recomendada".

**7. Cierre y Reflexión (5 min)**

* ¿Por qué empresas como Netflix, Amazon o agencias de *Scouting* prefieren usar el ángulo entre vectores (similitud del coseno) en lugar de la distancia euclidiana para recomendar productos o personas?

**8. Actividad Final de Consolidación (5 min)**

* **Mini-proyecto (Diagrama):** En un papelógarafo, cada grupo esquematiza un motor de recomendación sencillo para una industria de su elección, explicando explícitamente cómo usarían el producto punto, la norma y la fórmula del ángulo para conectar clientes con productos.