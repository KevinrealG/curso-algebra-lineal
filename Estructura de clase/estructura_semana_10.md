
### Clase 1: Geometría de la Rotación y Áreas (Producto Cruz en $\mathbb{R}^3$)

**1. Información General**

### Plan de Clase (70 Minutos): El Producto Vectorial y sus Aplicaciones Transversales

---

#### 1. Información General

* **Tema:** El Producto Vectorial (Cruz), propiedades geométricas, dirección (regla de la mano derecha/tornillo) y aplicaciones en Ingeniería (Torque y Robótica) y Finanzas (Cobertura de Riesgos).
* **Modalidad y Duración:** Presencial, 70 minutos.
* **Competencia:** Aplicar el producto vectorial en $\mathbb{R}^3$ para calcular torques mecánicos, evaluar la independencia lineal de sistemas robóticos y diseñar instrumentos de cobertura financiera ortogonales.

---

#### 2. Apertura (10 min): El Reto del Torque y la Rotación

* **El Reto (Contexto Visual):** Proyecta la imagen de un mecánico industrial intentando aflojar un perno atascado con una llave de tuercas.
* **Preguntas Motivadoras:**
1. Si empujas el extremo de la llave con una fuerza determinada, ¿hacia dónde se orienta exactamente el resultado de ese esfuerzo y cómo sabe el perno si debe apretarse o aflojarse?
2. ¿Por qué si empujas la llave exactamente en la misma dirección en la que apunta el mango no logras ningún giro, sin importar cuánta fuerza apliques?
3. ¿Cómo podemos calcular matemáticamente tanto la **magnitud** de la fuerza de giro como su **dirección espacial exacta** en un entorno tridimensional?



---

#### 3. Exploración (5 min): Hipótesis de Orientación Física

* **Dinámica en Parejas:** Pide a los estudiantes que usen su antebrazo como el brazo de la llave ($\vec{r}$) y su mano como la fuerza aplicada ($\vec{F}$). Deben simular el empuje y debatir rápidamente hacia dónde "apunta" imaginariamente el eje de giro del perno antes de recibir la teoría formal.

---

#### 4. Desarrollo Conceptual I (15 min): Relación Física, Producto Vectorial y Propiedades

* **La Relación Física (Torque / Momento):**
* $\vec{r}$ (Vector de Posición): Va desde el pivote (centro del perno) hasta el punto de aplicación de la fuerza.
* $\vec{F}$ (Vector de Fuerza): La magnitud y dirección del empuje humano o mecánico.
* El producto cruz genera un nuevo vector llamado **Torque ($\vec{\tau}$)**: $\vec{\tau} = \vec{r} \times \vec{F}$. Este vector no se mueve a lo largo del plano, sino que representa el **eje de rotación**.


* **Definición y Dirección (El Tornillo y la Mano):**
* El producto cruz genera un vector estrictamente **perpendicular** al plano formado por $\vec{r}$ y $\vec{F}$.
* *Regla de la Mano Derecha / El Tornillo:* Si los dedos giran desde $\vec{r}$ hacia $\vec{F}$, el pulgar (o el avance del tornillo) indica la dirección del vector resultante (hacia adentro o hacia afuera del perno).


* **Magnitud y Propiedades:**
* Magnitud: $\Vert{}\vec{u} \times \vec{v}\Vert{} = \Vert{}\vec{u}\Vert{}\Vert{}\vec{v}\Vert{}\sin(\theta)$. Mide la eficacia máxima del giro (si $\theta = 0^\circ$, el seno es cero y no hay torque).
* *Propiedad Anticonmutativa:* $\vec{u} \times \vec{v} = -(\vec{v} \times \vec{u})$. Invertir el orden invierte el sentido de giro (aprieta en vez de aflojar).



---

#### 5. Actividad Guiada y Colaborativa (10 min): Cálculo Exacto de Torque

* **Práctica Deliberada:** Entrega un ejercicio estructurado a los grupos.
* *Escenario:* Un perno ubicado en el origen recibe un vector de posición $\vec{r} = (0.2, 0.4, 0)$ metros y una fuerza aplicada $\vec{F} = (0, 50, -10)$ Newtons.


* **Resolución:** Los estudiantes estructuran el determinante de $3 \times 3$ con los vectores unitarios $\hat{i}, \hat{j}, \hat{k}$:

$$\vec{\tau} = \vec{r} \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 0.2 & 0.4 & 0 \\ 0 & 50 & -10 \end{vmatrix}$$


* **Resultado:** Calculan los componentes y obtienen el vector de torque exacto y su norma para verificar si el perno resistirá la torsión.

---

#### 6. Desarrollo Conceptual y Aplicación II (10 min): Calibración y Control de un Dron

* **El Escenario:** Un dron necesita moverse en $\mathbb{R}^3$. Sus propulsores deben ser linealmente independientes para evitar quedar atrapados en un plano. La magnitud del producto cruz mide el área del paralelogramo, funcionando como un **indicador de independencia espacial**.
* **Caso 1 (Fallo del Sistema - Dependencia Lineal):**
* Propulsor 1: $\vec{A} = [2, 4, 0]$ (Noreste).
* Propulsor 2: $\vec{B} = [4, 8, 0]$ (Exactamente el doble, misma dirección).
* Cálculo: $\vec{A} \times \vec{B} = [0, 0, (2 \times 8) - (4 \times 4)] = [0, 0, 0]$.
* *Interpretación:* Magnitud cero. Los propulsores hacen exactamente lo mismo; el dron pierde control direccional.


* **Caso 2 (Navegación Correcta - Independencia Lineal):**
* Propulsor 1: $\vec{A} = [2, 0, 0]$ (Este).
* Propulsor 3: $\vec{C} = [0, 3, 0]$ (Norte).
* Cálculo: $\vec{A} \times \vec{C} = [0, 0, (2 \times 3) - (0 \times 0)] = [0, 0, 6]$.
* *Interpretación:* Magnitud de 6 (área no nula). Los vectores son linealmente independientes, permitiendo navegación tridimensional estable.



---

#### 7. Aplicación III (15 min): Cobertura de Riesgos en Finanzas

* **El Escenario:** Llevamos el producto cruz a un espacio de escenarios económicos ($x$: Crecimiento/Soleado, $y$: Estabilidad/Nublado, $z$: Crisis/Tormenta) para diseñar coberturas de portafolio.
* **Activos Base:**
* Activo Defensivo ($a$): $(0, 0, 2)$ — Refugio que duplica su valor en crisis.
* Activo Especulativo ($b$): $(3, 0, -2)$ — Gana con la bonanza, pierde en pánico.
* Índice de Mercado Tradicional ($c$): $(1, 1, 1)$ — Rendimiento constante y moderado.


* **El Reto de Cobertura ($w = b \times c$):**
* Tomamos el Activo Especulativo ($b$) y el Índice Tradicional ($c$ para hallar un nuevo activo sintético $w$ ortogonal a ambos).
* *Cálculo vectorial:*
* $x$ (Crecimiento): $(0)(1) - (-2)(1) = \mathbf{2}$
* $y$ (Estabilidad): $(-2)(1) - (3)(1) = \mathbf{-5}$
* $z$ (Crisis): $(3)(1) - (0)(1) = \mathbf{3}$


* *Vector Resultante de Cobertura:* $w = (2, -5, 3)$


* **Interpretación Financiera de los Valores ($x, y, z$):**
* **$x = 2$ (Crecimiento):** Apuesta en positivo con 2 unidades para mantener el equilibrio con las ganancias del mercado en tiempos buenos.
* **$y = -5$ (Estabilidad):** *¡El freno de mano!* Apuesta en negativo con 5 unidades (posición corta o *short*). Resta valor cuando el mercado está aburrido para neutralizar la inercia de los otros activos.
* **$z = 3$ (Crisis):** Apuesta en positivo con 3 unidades. Inyecta ganancias fuertes exactamente cuando el mercado se desploma, rescatando el capital total.



---

#### 8. Cierre y Reflexión (5 min)

* **Pregunta de Integración:** "¿Qué tienen en común un mecánico apretando un perno, un programador calibrando los propulsores de un dron y un gestor financiero cubriendo un fondo de inversión frente a una crisis?" (Respuesta: Todos utilizan la geometría del producto cruz para controlar direcciones perpendiculares, magnitudes y riesgos en espacios multidimensionales).
* **Actividad Final de Consolidación (Ticket de Salida):** Cada estudiante escribe en un papel una breve frase explicando cómo la magnitud del producto cruz distingue un sistema físico inútil (como vectores colineales) de un sistema de cobertura financiera exitoso. Se entrega al salir.

## Clase 2: Propiedades del Producto y el Triple Producto Escalar


### Plan de Clase (30 Minutos): El Volumen Oculto en los Cristales

**1. Información General**

* **Tema:** El Triple Producto Escalar y el cálculo de volúmenes espaciales.
* **Competencia:** Calcular el triple producto escalar para determinar el volumen de un paralelepípedo, aplicándolo a la viabilidad estructural de una celda cristalina en Ingeniería de Materiales.
* **Modalidad y Duración:** Presencial, 30 minutos (Cápsula intensiva).
* **Recursos:** Pizarra, calculadoras/smartphones, apuntes de la clase de producto cruz.

**2. Apertura (El Reto - 5 min)**

* **Reto:** Proyecta la imagen de un microscopio electrónico mostrando la estructura atómica de un nuevo material para baterías de iones de litio. Informa a los estudiantes que los átomos forman una "celda unitaria" definida por tres vectores: $u, v, w$.
* **Preguntas Motivadoras:**
1. Si estos tres vectores atómicos están aplastados en un solo plano, ¿cuánto espacio (volumen) tiene el litio para moverse dentro de la batería?
2. Ya sabemos que el producto cruz ($v \times w$) nos da un área bidimensional. ¿Qué operación matemática le "inyectaría" la tercera dimensión a esa área para convertirla en una caja 3D?
3. Si la operación matemática arroja un volumen negativo, ¿la materia se está destruyendo o qué significa físicamente?



**3. Exploración (3 min)**

* **Hipótesis Rápida (Think-Pair-Share):** Pide a los estudiantes que miren a su compañero de al lado durante 60 segundos y debatan: *Si el área de la base de nuestra celda de cristal es el vector resultante de $v \times w$ (que apunta hacia arriba), ¿cómo podemos usar el producto escalar (punto) con el tercer vector $u$ para encontrar la altura exacta de la caja?*

**4. Desarrollo Conceptual (5 min)**

* **La Ecuación Híbrida:** Escribe en la pizarra la fórmula del **Triple Producto Escalar**: $u \cdot (v \times w)$.
* **Decodificación Geométrica:**
* **Paso 1:** $v \times w$ calcula el *área de la base* (un paralelogramo) y genera un vector perpendicular.
* **Paso 2:** Al hacer el producto punto con $u$, estamos multiplicando esa área base por la "sombra" (proyección) de $u$ sobre el eje vertical, lo cual es exactamente la *altura*.
* **Conclusión:** El valor absoluto $\vert{}u \cdot (v \times w)\vert{}$ es el **volumen del paralelepípedo**. ¡Área de la base por la altura!



**5. Actividad Guiada y Colaborativa (10 min)**

* **El Laboratorio Exprés:** Cada trío de estudiantes asume el rol de Ingenieros de Materiales.
* **Los Datos:** La celda cristalina del material propuesto está definida por los vectores:
* $u = (1, 0, 2)$
* $v = (0, 2, 0)$
* $w = (1, 1, 0)$


* **La Misión:**
1. Un estudiante calcula rápido la base: $v \times w$.
2. Otro estudiante realiza el producto punto del resultado con $u$.
3. El tercero audita los cálculos y aplica el valor absoluto para obtener el volumen en nanómetros cúbicos.



**6. Aplicación (2 min)**

* **Toma de Decisión:** Si el fabricante asiático les envía una propuesta de material barato cuyos vectores base arrojan un triple producto escalar exactamente igual a $0$, ¿aprueban la compra para fabricar baterías 3D o la rechazan de inmediato? (Respuesta: Se rechaza; volumen 0 significa vectores coplanarios, es un material 2D).

**7. Cierre y Reflexión (3 min)**

* **Debate Plenario:** ¿Por qué el triple producto escalar es el "detector de fraudes" definitivo en sistemas de coordenadas de 3 dimensiones? (Descubre dependencias lineales).

**8. Actividad Final de Consolidación (2 min)**

* **Ticket de Salida (Fast-Sketch):** En un trozo de papel, cada estudiante debe dibujar una caja inclinada, etiquetar $u, v, w$, sombrear la base indicando que es $v \times w$, y entregar el papel al salir del aula.

---

### Estructura de las Diapositivas (Apoyo Visual)

Dado que solo tienes 30 minutos, la presentación debe ser ágil y muy visual. No uses viñetas largas.

**Slide 1: Apertura (El Reto del Material)**

* **Visual:** Fotografía en alta resolución (microscopio) de una celda cristalina y una batería de litio moderna.
* **Texto:** El Reto de Materiales: Tres vectores atómicos. ¿Material revolucionario o fraude geométrico?
* **Uso:** Mantén esta diapositiva mientras lanzas las 3 preguntas motivadoras.

**Slide 2: Exploración (La Caja Inclinada)**

* **Visual:** Un modelo 3D simple de un paralelepípedo formado por flechas $u, v, w$. La base formada por $v, w$ está resaltada en un color brillante.
* **Texto:** *Think-Pair-Share* (60 segundos).
* **Uso:** Sirve como cronómetro visual para que los estudiantes discutan cómo calcular la altura.

**Slide 3: Desarrollo Conceptual (La Ecuación del Volumen)**

* **Visual:** La ecuación en fuente muy grande: **$\vert{}u \cdot (v \times w)\vert{} = \text{Volumen}$**.
* Una flecha señala a $(v \times w)$ indicando "Área de la base".
* Otra flecha señala al producto $\cdot$ indicando "Proyección de la Altura".


* **Uso:** Explicación magistral mínima (5 minutos). El enfoque visual evita escribir texto explicativo.

**Slide 4: Actividad Guiada (Cálculo de la Celda Cristalina)**

* **Visual:** Los tres vectores atómicos $u = (1, 0, 2)$, $v = (0, 2, 0)$, $w = (1, 1, 0)$ en formato de matriz de $3 \times 3$ (para que visualicen que el triple producto escalar equivale al determinante).
* **Texto:** ¡Misión de Auditoría! Calculen el volumen en nanómetros cúbicos ($nm^3$).
* **Uso:** Queda proyectada durante los 10 minutos de trabajo colaborativo.

**Slide 5: Cierre y Ticket de Salida**

* **Visual:** Icono de advertencia o "Sello de Rechazado" sobre un cálculo que da $= 0$.
* **Texto:**
* Reflexión: Volumen $0$ = Vectores Coplanarios = Material Bidimensional.
* **Ticket de Salida:** Dibuja la celda, etiqueta la base y la altura. ¡Entrégalo al salir!


* **Uso:** Consolida el aprendizaje y dirige la actividad de cierre antes de que los estudiantes recojan sus pertenencias.