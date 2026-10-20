Aquí tienes la planeación detallada.

### 1. Información General

* **Tema:** Espacios Vectoriales Reales y Subespacios
* **Duración:** 50 minutos
* **Dirigido a:** Finanzas, Administración, Comercio, Ingeniería, Contabilidad
* **Objetivo de la Sesión:** Comprender la estructura de los espacios vectoriales e identificar subespacios mediante la verificación de sus axiomas de cerradura, aplicándolo a restricciones de negocio e ingeniería.
* **Referencia Grossman:** Capítulo 4, Secciones 4.1 y 4.2.

### 2. Apertura (Motivación y Contexto Aplicado)

* **Reto / Pregunta Detonante:**
En la asignación de presupuestos, un departamento puede invertir su capital en campañas de Marketing (X) e Investigación (Y). Si se decreta que "el gasto en Investigación debe ser siempre el doble del gasto en Marketing", ¿qué sucede algebraicamente si dos gerentes presentan presupuestos válidos distintos y decidimos sumarlos? ¿El nuevo presupuesto total sigue cumpliendo la regla?
* **Conexión Interdisciplinar:**
* **Contabilidad y Finanzas:** Modelado de portafolios de inversión bajo restricciones estrictas de riesgo cero o balances contables homogéneos (activos = pasivos).
* **Administración y Comercio:** Definición de escenarios viables donde los recursos o inventarios deben mantener proporciones exactas independientemente de la escala de operación.
* **Ingeniería:** Control de sistemas estables donde la suma de dos estados de equilibrio garantice un nuevo estado de equilibrio (linealidad de sistemas).



### 3. Exploración (Intuición y Geometría)

* **Interpretación Visual/Geométrica:**
En $\mathbb{R}^2$ o $\mathbb{R}^3$, un espacio vectorial es como un universo infinito de movimientos. Un **subespacio** es un sub-universo cerrado (una línea o un plano) que **obligatoriamente debe pasar por el origen**. Si te sales del origen (por ejemplo, sumando una constante como $y = 2x + 5$), "rompes" el subespacio, porque al multiplicar por cero o sumar vectores, te sales de esa línea.
* **Demostración Rápida / Intuición:**
La "cerradura" significa que el conjunto se comporta como Las Vegas: lo que pasa en el conjunto (sumas o multiplicaciones escalares de sus elementos), se queda en el conjunto. Si mezclas dos soluciones válidas y el resultado es inválido, no es un subespacio.

### 4. Desarrollo Conceptual I (Rigor y Procedimiento)

* **Definiciones y Teoremas Clave:**
* **Espacio Vectorial Real ($V$):** Conjunto provisto de dos operaciones (suma y multiplicación por escalar) que satisface 10 axiomas fundamentales (conmutatividad, asociatividad, elemento neutro, inversos aditivos, distributividad, etc.).
* **Subespacio Vectorial ($H$):** Un subconjunto no vacío $H$ de $V$ es un subespacio si, y solo si, es cerrado bajo las dos operaciones de $V$:
1. **Cerradura bajo la suma:** Si $\mathbf{x} \in H$ y $\mathbf{y} \in H$, entonces $\mathbf{x} + \mathbf{y} \in H$.
2. **Cerradura bajo producto escalar:** Si $\mathbf{x} \in H$ y $\alpha$ es un escalar real, entonces $\alpha\mathbf{x} \in H$.
*(Nota: Todo subespacio debe contener al vector nulo $\mathbf{0}$).*




* **Algoritmo de Solución (Verificación de Subespacios):**
1. **Prueba del Elemento Neutro:** Verificar rápidamente si el vector $\mathbf{0}$ pertenece a $H$. Si no, $H$ no es subespacio (prueba de fuego).
2. **Prueba de Suma:** Tomar dos vectores genéricos $\mathbf{u}, \mathbf{v} \in H$ que cumplan la restricción. Sumarlos analíticamente y verificar si el vector resultante $(\mathbf{u}+\mathbf{v})$ también cumple la restricción de $H$.
3. **Prueba de Escalar:** Tomar un vector genérico $\mathbf{u} \in H$ y un escalar $\alpha$. Multiplicar y verificar si $\alpha\mathbf{u}$ cumple la restricción.


* **Ejemplo Modelo Resuelto:**
Determinar si el conjunto $H = \{(x,y,z) \in \mathbb{R}^3 \mid 2x - y + z = 0\}$ es un subespacio vectorial.
1. *Vector Nulo:* Si $x=0, y=0, z=0 \implies 2(0) - (0) + 0 = 0$. Cumple.
2. *Cerradura bajo la Suma:*
Sean $\mathbf{u} = (x_1, y_1, z_1)$ y $\mathbf{v} = (x_2, y_2, z_2)$ elementos de $H$.
Sabemos que: $2x_1 - y_1 + z_1 = 0$ y $2x_2 - y_2 + z_2 = 0$.
Sumamos $\mathbf{u} + \mathbf{v} = (x_1+x_2, y_1+y_2, z_1+z_2)$.
Evaluamos en la restricción: $2(x_1+x_2) - (y_1+y_2) + (z_1+z_2)$.
Reagrupando: $(2x_1 - y_1 + z_1) + (2x_2 - y_2 + z_2) = 0 + 0 = 0$. Cumple.
3. *Cerradura bajo Escalar:*
Sea $\alpha \in \mathbb{R}$. Multiplicamos $\alpha\mathbf{u} = (\alpha x_1, \alpha y_1, \alpha z_1)$.
Evaluamos: $2(\alpha x_1) - (\alpha y_1) + (\alpha z_1) = \alpha(2x_1 - y_1 + z_1) = \alpha(0) = 0$. Cumple.
*Conclusión:* $H$ es un subespacio vectorial de $\mathbb{R}^3$.



### 5. Actividad Guiada y Colaborativa (Alta Dificultad)

**Instrucciones**
Formar equipos de 3 personas. Disponen de 20 minutos para analizar y resolver los dos problemas planteados, aplicando rigurosamente los axiomas de cerradura.

**Problema 1 (Enfoque Empresarial/Financiero/Contable)**
El comité de inversiones de un banco define un conjunto de portafolios aceptables $P$. Un portafolio es un vector $(x, y, z)$ donde $x$ es la inversión en bonos del tesoro, $y$ en acciones tecnológicas y $z$ en bienes raíces.
El conjunto permitido está dado por $P = \{(x,y,z) \in \mathbb{R}^3 \mid x + y + z = 100\}$.
(Es decir, todo portafolio debe sumar exactamente 100 millones).

1. Demuestre matemática y conceptualmente si el conjunto de portafolios $P$ es o no es un subespacio vectorial de $\mathbb{R}^3$.
2. Interprete qué significa el resultado en términos de la flexibilidad para combinar fondos o escalar inversiones.

**Problema 2 (Enfoque Técnico/Ingeniería/Análisis de Sistemas)**
En dinámica de fluidos, las velocidades de flujo en una intersección de tuberías están dadas por el vector $(v_1, v_2, v_3, v_4)$. Para que el sistema no acumule presión (equilibrio de masa), se define el conjunto $S = \{(v_1, v_2, v_3, v_4) \in \mathbb{R}^4 \mid v_1 = k v_2 \text{ y } v_3 - v_4 = k^2 - 4\}$.

1. Encuentre todos los valores del parámetro real $k$ que hagan que el sistema en equilibrio $S$ sea un subespacio vectorial válido.
2. Con el valor(es) de $k$ hallado(s), demuestre formalmente la cerradura bajo la suma.



**Solución Detallada y Pauta de Evaluación**

**Solución del Problema 1:**

1. **Prueba del vector nulo:** Para que sea subespacio, el vector nulo $\mathbf{0} = (0,0,0)$ debe pertenecer a $P$.
Evaluando: $0 + 0 + 0 = 0 \neq 100$.
Por lo tanto, el vector $\mathbf{0} \notin P$.
*Conclusión:* **No es un subespacio vectorial.** (Es una variedad afín / plano desplazado).
2. **Interpretación:** Al no ser un subespacio, carece de las propiedades de escalabilidad lineal. Si un gerente tiene un portafolio válido que suma 100, y decide triplicar su inversión (multiplicar por escalar $\alpha=3$), el nuevo total será 300, violando la regla del comité. Igualmente, si se fusionan (suman) dos portafolios válidos, el resultado sumará 200, quedando fuera de la restricción permitida.

**Solución del Problema 2:**

1. Para que $S$ sea subespacio, debe contener el origen $(0,0,0,0)$.
Si $(v_1, v_2, v_3, v_4) = (0,0,0,0)$, la segunda restricción exige que:
$0 - 0 = k^2 - 4 \implies k^2 = 4 \implies \mathbf{k = 2} \text{ o } \mathbf{k = -2}$.
*(Nota: Con estos valores, la restricción de masa se vuelve homogénea: $v_3 - v_4 = 0$ o $v_3 = v_4$, y la primera restricción es $v_1 = 2v_2$ o $v_1 = -2v_2$. Ambas son lineales).*
2. Demostración de cerradura bajo la suma (usando $k=2$):
El conjunto es $S = \{(v_1, v_2, v_3, v_4) \mid v_1 = 2v_2 \text{ y } v_3 = v_4\}$.
Sean $\mathbf{u} = (u_1, u_2, u_3, u_4)$ y $\mathbf{w} = (w_1, w_2, w_3, w_4)$ vectores en $S$.
Sabemos que:
$u_1 = 2u_2 \quad \text{y} \quad u_3 = u_4$
$w_1 = 2w_2 \quad \text{y} \quad w_3 = w_4$
Sumamos: $\mathbf{u} + \mathbf{w} = (u_1+w_1, u_2+w_2, u_3+w_3, u_4+w_4)$.
Comprobamos la primera condición en la suma:
$u_1+w_1 = (2u_2) + (2w_2) = 2(u_2+w_2)$. (Cumple la proporción de $k=2$).
Comprobamos la segunda condición en la suma:
$u_3+w_3 = (u_4) + (w_4) = u_4+w_4$. (Cumple la igualdad $v_3 = v_4$).
El vector suma pertenece a $S$. (Se podría hacer lo mismo de forma análoga para $k=-2$).
## Ejemplo 1
El mejor ejemplo de cómo se usan los espacios vectoriales para detectar y corregir errores son los **Códigos de Bloque Lineal** (como el Código de Hamming).

En la transmisión digital, los datos se manejan en un espacio vectorial sobre un "campo finito" llamado GF(2), donde los únicos escalares posibles son `0` y `1`, y la suma es la operación XOR ($1+1=0$).

### La matemática detrás de la corrección

1. **El Subespacio Válido:** Si tienes un mensaje de 4 bits, existe en un espacio de $\mathbb{R}^4$. Usando una **Matriz Generadora ($G$)**, transformas ese vector a un espacio más grande, digamos $\mathbb{R}^7$. Los mensajes válidos ahora son un *subespacio* muy específico de $\mathbb{R}^7$.
2. **El Espacio Nulo (Núcleo):** Creas una **Matriz de Comprobación de Paridad ($H$)**. Esta matriz está diseñada de tal forma que su "espacio nulo" contiene exactamente a todos los vectores válidos. Es decir, si multiplicas cualquier vector válido por $H$, el resultado debe ser el vector cero.
3. **El Síndrome:** Cuando recibes un vector, lo multiplicas por $H$. Si el resultado es distinto de cero (a este resultado se le llama *síndrome*), el vector "salió" del subespacio válido debido a un error de transmisión. El síndrome te indica exactamente qué dimensión (bit) tiene el error.

### Código en Python (Código de Hamming 7,4)

Este código simula cómo tu computadora o tu módem Wi-Fi usa operaciones de álgebra lineal matricial para asegurar que la información no se corrompa.

```python
import numpy as np

def simular_transmision():
    # 1. Definición de los Espacios Vectoriales
    # Matriz Generadora G (Mapea un vector de dimensión 4 a uno de dimensión 7)
    G = np.array([
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ])

    # Matriz de Paridad H (Define el subespacio válido. Multiplicar por H debe dar 0)
    H = np.array([
        [1, 1, 0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1]
    ])

    # 2. El Emisor codifica el mensaje
    mensaje_original = np.array([1, 0, 1, 1])
    
    # Producto punto de matrices (módulo 2 para trabajar en GF(2))
    vector_transmitido = np.dot(mensaje_original, G) % 2
    print(f"Vector original a enviar:   {vector_transmitido}")

    # 3. Interferencia en el canal (se voltea un bit durante la transmisión)
    vector_recibido = vector_transmitido.copy()
    error_index = 2 # Simulamos que el ruido electromagnético cambió el tercer bit
    vector_recibido[error_index] = (vector_recibido[error_index] + 1) % 2
    print(f"Vector recibido con error:  {vector_recibido}")

    # 4. El Receptor verifica si el vector pertenece al subespacio válido
    # Calculamos el síndrome: S = H * R^T (módulo 2)
    sindrome = np.dot(H, vector_recibido) % 2
    print(f"Síndrome calculado:         {sindrome}")

    # 5. Corrección basada en álgebra lineal
    if np.sum(sindrome) == 0:
        print("El vector está en el subespacio nulo. No hay errores.")
    else:
        # Buscamos qué columna de la matriz H es igual al síndrome
        # Esto nos indica qué coordenada del vector causó que saliera del subespacio
        for i in range(H.shape[1]):
            if np.array_equal(H[:, i], sindrome):
                print(f"\n¡Error detectado en el bit {i}! Corrigiendo...")
                vector_recibido[i] = (vector_recibido[i] + 1) % 2
                break
        
        print(f"Vector corregido:           {vector_recibido}")

simular_transmision()

```

### ¿Dónde se usa esto en la vida real?

* **Memorias RAM ECC (Error-Correcting Code):** Los servidores de bases de datos utilizan esta misma multiplicación de matrices en tiempo real por hardware para evitar que la radiación cósmica cambie un bit en la memoria y colapse el sistema.
* **Comunicaciones Espaciales:** Las sondas como Voyager envían datos con potencias de señal minúsculas. Los códigos Reed-Solomon (una versión avanzada basada en polinomios sobre espacios vectoriales) permiten reconstruir las imágenes a pesar del ruido del espacio profundo.
* **Códigos QR:** Si tapas una esquina de un código QR, tu cámara aún puede leerlo gracias a que los datos están proyectados en un espacio vectorial redundante.
## Ejemplo 2
Los *embeddings* en Deep Learning (como Word2Vec) transforman conceptos discretos, como palabras o imágenes, en coordenadas de números reales dentro de un espacio vectorial multidimensional continuo (por ejemplo, en $\mathbb{R}^{300}$).

En este espacio vectorial, las operaciones algebraicas básicas (suma y multiplicación por escalares) capturan relaciones semánticas reales:

* **Suma y resta de vectores:** El ejemplo clásico es la aritmética vectorial que permite resolver analogías lógicas:
$\text{Vector(Rey)} - \text{Vector(Hombre)} + \text{Vector(Mujer)} \approx \text{Vector(Reina)}$
* **Magnitud y dirección (Similitud del coseno):** La geometría del espacio refleja el significado. Los vectores de "Perro" y "Gato" tendrán un ángulo muy estrecho entre sí (están cerca en el espacio vectorial), mientras que el vector de "Termodinámica" apuntará en una dirección completamente distinta.

El modelo de red neuronal "aprende" a asignar las coordenadas correctas para que la estructura de ese espacio vectorial mapee perfectamente las reglas y relaciones lógicas del lenguaje.

# clase 2

### 1. Información General

* **Tema:** Combinación Lineal y Conjuntos Generadores (Espacio Generado / *Span*).
* **Duración:** 50 minutos.
* **Dirigido a:** Finanzas, Administración, Comercio, Ingeniería, Contabilidad.
* **Objetivo de la Sesión:** Formular combinaciones lineales de vectores mediante sistemas de ecuaciones y evaluar si un conjunto de vectores es capaz de generar todo un espacio vectorial o solo un subespacio, aplicándolo a la creación de mezclas, portafolios sintéticos y asignación de recursos.
* **Referencia Grossman:** Capítulo 4, Sección 4.3.

### 2. Apertura (Motivación y Contexto Aplicado)

* **Reto / Pregunta Detonante:**
Eres el gerente de operaciones de una empresa química. En tus almacenes tienes tres mezclas base (fluidos con diferentes concentraciones de 3 químicos). Si un cliente te pide un pedido especial con una concentración exacta $(a, b, c)$, ¿es químicamente posible satisfacer su pedido simplemente mezclando proporciones de lo que ya tienes en el almacén? ¿Existen pedidos que son imposibles de fabricar con tus inventarios actuales?
* **Conexión Interdisciplinar:**
* **Finanzas:** Un banco crea un "activo sintético" (combinación lineal) sumando proporciones de diferentes bonos y acciones existentes para replicar el rendimiento de un índice de mercado.
* **Administración/Comercio:** La capacidad de satisfacer cualquier demanda logística en una red usando un conjunto finito de rutas base.



### 3. Exploración (Intuición y Geometría)

* **Interpretación Visual/Geométrica:**
Imagina que estás en el origen $(0,0,0)$ de una habitación vacía. Si te doy un vector (una dirección fija), solo puedes caminar hacia adelante y hacia atrás sobre esa línea; ese es el espacio que "generas". Si te doy un segundo vector que no apunte en la misma línea, ahora combinando pasos en ambas direcciones puedes caminar por todo un plano bidimensional. Si te doy un tercer vector (que no esté en ese plano), ahora puedes alcanzar *cualquier punto* de la habitación 3D.
* **Demostración Rápida / Intuición:**
Una combinación lineal es simplemente una "receta de cocina". Los vectores son los ingredientes crudos y los escalares (los números por los que multiplicas) son las cantidades o tazas de cada ingrediente. Generar el espacio completo significa responder "Sí" a la pregunta: *¿Puedo cocinar cualquier plato imaginable del menú utilizando exclusivamente los ingredientes de esta despensa?*

### 4. Desarrollo Conceptual I (Rigor y Procedimiento)

* **Definiciones y Teoremas Clave:**
* **Combinación Lineal:** Un vector $\mathbf{v}$ en un espacio vectorial $V$ se denomina *combinación lineal* de los vectores $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k$ si existen escalares $c_1, c_2, \dots, c_k$ tales que:

$$\mathbf{v} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_k\mathbf{v}_k$$


* **Conjunto Generador (Span):** Se dice que los vectores $\mathbf{v}_1, \dots, \mathbf{v}_k$ *generan* a $V$ si todo vector en $V$ se puede escribir como una combinación lineal de ellos. Es decir, $\text{gen}\{\mathbf{v}_1, \dots, \mathbf{v}_k\} = V$.


* **Algoritmo de Solución:**
1. Para probar si $\mathbf{v}$ es C.L. de otros vectores, plantear la ecuación vectorial y traducirla a un sistema de ecuaciones lineales $A\mathbf{c} = \mathbf{v}$, donde las columnas de $A$ son los vectores dados.
2. Resolver la matriz aumentada mediante Gauss-Jordan.
3. Si el sistema es **consistente** (tiene 1 o infinitas soluciones), SÍ es combinación lineal. Si es **inconsistente**, NO lo es.
4. Para probar si *generan* todo el espacio $\mathbb{R}^n$, igualar la combinación a un vector genérico $(x, y, z)$ o usar el cálculo del determinante (si la matriz es cuadrada $n \times n$ y su determinante es $\neq 0$, generan $\mathbb{R}^n$).


* **Ejemplo Modelo Resuelto:**
¿Es el vector de recursos $\mathbf{b} = (2, -1, 3)$ una combinación lineal de los inventarios $\mathbf{v}_1=(1, 0, 1)$, $\mathbf{v}_2=(-1, 1, 0)$, $\mathbf{v}_3=(0, 1, 1)$?
Planteamos el sistema:
$c_1(1,0,1) + c_2(-1,1,0) + c_3(0,1,1) = (2,-1,3)$
Matriz Aumentada:

$$\begin{pmatrix} 1 & -1 & 0 & \vert & 2 \\ 0 & 1 & 1 & \vert & -1 \\ 1 & 0 & 1 & \vert & 3 \end{pmatrix}$$


Operación $R_3 \rightarrow R_3 - R_1$:

$$\begin{pmatrix} 1 & -1 & 0 & \vert & 2 \\ 0 & 1 & 1 & \vert & -1 \\ 0 & 1 & 1 & \vert & 1 \end{pmatrix}$$


Operación $R_3 \rightarrow R_3 - R_2$:

$$\begin{pmatrix} 1 & -1 & 0 & \vert & 2 \\ 0 & 1 & 1 & \vert & -1 \\ 0 & 0 & 0 & \vert & 2 \end{pmatrix}$$


La última fila indica $0c_1 + 0c_2 + 0c_3 = 2$, lo cual es matemáticamente imposible. El sistema es inconsistente.
*Conclusión:* NO es combinación lineal. No hay forma de mezclar esos 3 inventarios para obtener exactamente el requerimiento $\mathbf{b}$.

### 5. Actividad Guiada y Colaborativa (Alta Dificultad)

**Instrucciones:**
Formen equipos de 3 personas. Disponen de 15-20 minutos. Cada equipo debe plantear matricialmente la solución, aplicar los conceptos de consistencia de sistemas y brindar la interpretación gerencial y técnica correspondiente.

**Ejercicios de Alta Dificultad / Desafío Aplicado:**

* **Problema 1 (Enfoque Empresarial/Financiero/Contable):**
Un fondo de inversión tiene a su disposición tres tipos de portafolios indexados, cuya composición (en porcentaje de Renta Fija, Renta Variable y Materias Primas) viene dada por los vectores: $\mathbf{p}_1 = (1, 1, 0)$, $\mathbf{p}_2 = (0, 1, 1)$ y $\mathbf{p}_3 = (1, 2, 1)$.
Un cliente ultra-rico exige estructurar un fondo a la medida con la proporción exacta $\mathbf{p}_{obj} = (2, 3, 1)$.
1. ¿Es posible replicar este fondo exigido combinando proporciones de $\mathbf{p}_1, \mathbf{p}_2, \mathbf{p}_3$? (Halle los valores).
2. ¿Pueden los analistas del fondo asegurar que con esos 3 portafolios básicos podrán generar *cualquier* perfil de riesgo $(x,y,z)$ que exija el mercado en el futuro? Justifique algebraicamente.


* **Problema 2 (Enfoque Técnico/Ingeniería/Análisis de Sistemas):**
En un simulador aerodinámico, las fuerzas de empuje de tres propulsores vectoriales dependen de un parámetro de calibración estructural $\alpha$. Los propulsores ejercen vectores de fuerza direccional: $\mathbf{f}_1=(1, \alpha, 0)$, $\mathbf{f}_2=(0, 1, -1)$ y $\mathbf{f}_3=(\alpha, 0, 1)$.
Para que la nave tenga un control de traslación total y maniobrabilidad 3D absoluta, los propulsores deben poder generar todo el espacio $\mathbb{R}^3$.
Halle qué valores críticos (puntos de falla) del parámetro $\alpha$ provocarán que la nave pierda un grado de libertad (es decir, que los vectores *no* generen $\mathbb{R}^3$).

**Solución Detallada y Pauta de Evaluación:**

* **Solución del Problema 1:**
1. Planteamos $\mathbf{p}_{obj}$ como combinación lineal: $c_1(1,1,0) + c_2(0,1,1) + c_3(1,2,1) = (2,3,1)$.
La matriz aumentada es:

$$\begin{pmatrix} 1 & 0 & 1 & \vert & 2 \\ 1 & 1 & 2 & \vert & 3 \\ 0 & 1 & 1 & \vert & 1 \end{pmatrix}$$



Operamos $R_2 \rightarrow R_2 - R_1$:

$$\begin{pmatrix} 1 & 0 & 1 & \vert & 2 \\ 0 & 1 & 1 & \vert & 1 \\ 0 & 1 & 1 & \vert & 1 \end{pmatrix}$$



Operamos $R_3 \rightarrow R_3 - R_2$:

$$\begin{pmatrix} 1 & 0 & 1 & \vert & 2 \\ 0 & 1 & 1 & \vert & 1 \\ 0 & 0 & 0 & \vert & 0 \end{pmatrix}$$



El sistema es consistente (infinitas soluciones). Sí es posible. Una solución es hacer $c_3=0$, por ende $c_2=1$ y $c_1=2$. (El cliente compra 2 unidades de $\mathbf{p}_1$, 1 de $\mathbf{p}_2$ y nada de $\mathbf{p}_3$).
2. ¿Generan $\mathbb{R}^3$? Calculamos el determinante de la matriz de portafolios $A$:
$\det(A) = 1(1\cdot 1 - 1\cdot 2) - 0 + 1(1\cdot 1 - 0\cdot 1) = -1 + 1 = 0$.
Como el determinante es 0, los vectores **no generan** $\mathbb{R}^3$ (solo generan un plano). Esto significa que habrá clientes con perfiles de riesgo que el fondo será incapaz de satisfacer. (Pauta: el analista que note que $\mathbf{p}_3 = \mathbf{p}_1 + \mathbf{p}_2$ gana puntos por inspección, descubriendo la dependencia prematura).


* **Solución del Problema 2:**
Para que los 3 propulsores generen todo $\mathbb{R}^3$, la matriz formada por sus vectores columna debe ser invertible (su determinante debe ser diferente de 0).
Los puntos de falla crítica ocurren cuando el determinante es igual a 0.
Sea $A = \begin{pmatrix} 1 & 0 & \alpha \\ \alpha & 1 & 0 \\ 0 & -1 & 1 \end{pmatrix}$.
Calculamos $\det(A)$ desarrollando por la primera fila:
$\det(A) = 1 [ (1)(1) - (-1)(0) ] - 0 [ \dots ] + \alpha [ (\alpha)(-1) - (0)(1) ]$
$\det(A) = 1(1) + \alpha(-\alpha) = 1 - \alpha^2$.
Igualamos a cero para encontrar las fallas de maniobrabilidad:
$1 - \alpha^2 = 0 \implies \alpha^2 = 1 \implies \mathbf{\alpha = 1} \text{ o } \mathbf{\alpha = -1}$.
*Conclusión técnica:* Si el diseño aerodinámico arroja un valor estructural de calibración de 1 o -1, los vectores de fuerza se coplanan y la nave pierde la capacidad de trasladarse libremente en las tres dimensiones del espacio, limitando su movimiento a un plano bidimensional en caso de $\alpha = 1$ o $\alpha = -1$.

# Clase 3
### 1. Información General

* **Tema:** Independencia Lineal, Conjuntos Generadores, Bases y Dimensión.
* **Duración:** 50 minutos.
* **Dirigido a:** Finanzas, Administración, Comercio, Ingeniería, Contabilidad.
* **Objetivo de la Sesión:** Identificar vectores redundantes en un sistema, extraer el conjunto mínimo indispensable (base) y calcular los verdaderos grados de libertad (dimensión) en modelos de negocios e ingeniería.
* **Referencia Grossman:** Capítulo 4, Secciones 4.4 y 4.5.

### 2. Apertura (Motivación y Contexto Aplicado)

* **Reto / Pregunta Detonante:** Un gerente monitorea 10 KPIs (Indicadores Clave) distintos en su panel de control. Si resulta que 7 de ellos son matemáticamente solo promedios ponderados de los otros 3, ¿el gerente realmente gestiona 10 variables o su "dimensión" operativa es solo 3? ¿Cómo identificamos cuáles 3 indicadores son el verdadero motor del negocio y cuáles son ruido?
* **Conexión Interdisciplinar:**
* **Finanzas:** Identificación de factores de riesgo subyacentes. Un portafolio de 50 acciones puede tener una dimensión real de riesgo de solo 3 (tasas, inflación, PIB).
* **Ingeniería:** Grados de libertad en un brazo robótico o sistema estructural.
* **Comercio:** Reducción de dimensionalidad en grandes bases de datos logísticos para evitar multicolinealidad estadística.



### 3. Exploración (Intuición y Geometría)

* **Interpretación Visual/Geométrica:** Vectores dependientes son los que "colapsan" o se superponen sobre líneas o planos ya creados por otros vectores; no aportan una "nueva dirección" al espacio. La **base** es el esqueleto estructural mínimo y perfecto: no le sobra ningún hueso (independientes) y sostiene todo el cuerpo (genera). La **dimensión** es simplemente contar cuántos huesos tiene ese esqueleto.
* **Demostración Rápida / Intuición:** Si una ecuación de costos puede escribirse como combinación de otras dos, es redundante. Eliminarla no quita información.

### 4. Desarrollo Conceptual I (Rigor y Procedimiento)

* **Definiciones y Teoremas Clave:**
* **Independencia Lineal:** El conjunto de vectores $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n$ es linealmente independiente (L.I.) si la ecuación $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_n\mathbf{v}_n = \mathbf{0}$ tiene *únicamente* la solución trivial $c_1 = c_2 = \dots = c_n = 0$.
* **Base:** Un conjunto de vectores forma una base para el espacio vectorial $V$ si: 1) Generan a $V$, y 2) Son linealmente independientes.
* **Dimensión:** Es el número exacto de vectores que conforman una base para $V$.


* **Algoritmo de Solución:**
1. Construir una matriz donde las columnas (o filas) sean los vectores del conjunto.
2. Aplicar eliminación de Gauss-Jordan para llevarla a forma escalonada.
3. Si quedan filas de ceros (o hay columnas sin pivote principal), los vectores son linealmente dependientes.
4. Las columnas (o filas) pivote de la matriz original forman una **base**. El número de pivotes es la **dimensión**.


* **Ejemplo Modelo Resuelto:**
Determine si $\mathbf{v}_1=(1,2)$ y $\mathbf{v}_2=(2,4)$ son independientes, halle una base y su dimensión.
* Ecuación: $c_1(1,2) + c_2(2,4) = (0,0)$.
* Matriz: $\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$.
* Gauss ($R_2 - 2R_1$): $\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$.
* La segunda fila es de ceros. El sistema tiene variables libres, luego son **Linealmente Dependientes**.
* **Base:** $\{\mathbf{v}_1\} = \{(1,2)\}$. **Dimensión:** 1 (es solo una línea en el plano).



### 5. Actividad Guiada y Colaborativa (Alta Dificultad)

**Instrucciones:**
Trabajo en parejas (20 minutos). Traducir el problema práctico a vectores, plantear la matriz y aplicar reducción para concluir estratégicamente.

**Ejercicios de Alta Dificultad / Desafío Aplicado:**

* **Problema 1 (Enfoque Empresarial/Administración):**
Una consultora evalúa tres estrategias de marketing $\mathbf{E}_1, \mathbf{E}_2, \mathbf{E}_3$. Los vectores de impacto esperado en (Retorno, Visibilidad, Costo) son:
$\mathbf{E}_1 = (1, 1, 2)$
$\mathbf{E}_2 = (0, 1, -1)$
$\mathbf{E}_3 = (2, 3, 3)$
1. Determine si las tres estrategias son linealmente independientes.
2. Si hay estrategias redundantes, identifique cuáles forman la **base** de toma de decisiones del gerente y cuál es la **dimensión** real del plan de marketing. Justifique operativamente qué significa que una sea dependiente.


* **Problema 2 (Enfoque Técnico/Ingeniería):**
Un ingeniero ajusta los actuadores de un mecanismo. Sus vectores de calibración son $\mathbf{u} = (1, \beta)$ y $\mathbf{v} = (\beta, 4)$.
1. Encuentre los valores del parámetro de calibración $\beta$ para los cuales el mecanismo "colapsa" perdiendo un grado de libertad (es decir, la dimensión se reduce y no forman base para $\mathbb{R}^2$).



**Solución Detallada y Pauta de Evaluación:**

* **Solución del Problema 1:**
1. Se ubican los vectores en las columnas de una matriz $A$ y se reduce:
$A = \begin{bmatrix} 1 & 0 & 2 \\ 1 & 1 & 3 \\ 2 & -1 & 3 \end{bmatrix}$
$R_2 \rightarrow R_2 - R_1$ y $R_3 \rightarrow R_3 - 2R_1$:
$\begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 0 & -1 & -1 \end{bmatrix}$
$R_3 \rightarrow R_3 + R_2$:
$\begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}$
Al existir una fila de ceros, hay una variable libre. Las columnas **no** son linealmente independientes (son L.D.).
2. La columna 1 y 2 tienen pivotes. La **Base** es $\{\mathbf{E}_1, \mathbf{E}_2\}$. La **Dimensión** operativa es 2.
*Interpretación:* La estrategia $\mathbf{E}_3$ es redundante. Matemáticamente, de la RREF deducimos que $\mathbf{E}_3 = 2\mathbf{E}_1 + \mathbf{E}_2$. El gerente no necesita implementar las 3 estrategias; combinando la 1 y la 2 puede generar exactamente los mismos impactos en retorno y visibilidad que ofrece la estrategia 3.


* **Solución del Problema 2:**
Para que $\mathbf{u}$ y $\mathbf{v}$ sean base en $\mathbb{R}^2$, deben ser linealmente independientes, lo que implica que el determinante de la matriz que forman debe ser diferente de cero.
$A = \begin{bmatrix} 1 & \beta \\ \beta & 4 \end{bmatrix}$
El colapso dimensional (no forman base) ocurre si $\det(A) = 0$.
$\det(A) = (1)(4) - (\beta)(\beta) = 4 - \beta^2$.
$4 - \beta^2 = 0 \implies \beta^2 = 4 \implies \mathbf{\beta = 2} \text{ o } \mathbf{\beta = -2}$.
*Conclusión técnica:* Si el actuador se calibra en 2 o -2, los vectores se vuelven paralelos $\mathbf{v} = 2\mathbf{u}$ o $\mathbf{v} = -2\mathbf{u}$, la dimensión se colapsa de 2 a 1, y el mecanismo no podrá moverse en todo el plano $\mathbb{R}^2$.