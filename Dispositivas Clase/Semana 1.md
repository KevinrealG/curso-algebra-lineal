Aquí tienes el diseño instruccional estructurado bajo metodologías de aprendizaje activo. He ajustado el enfoque para conectar la abstracción matemática con los perfiles de ingeniería y economía, optimizando el uso de tu propia herramienta web.

### Sesión 1: Miércoles (2 Horas) - Modelado, Solución Gráfica y Sustitución

**Información General**

* **Tema:** Introducción a sistemas de ecuaciones (Modelado, método gráfico y sustitución).
* **Objetivo:** Modelar un problema contextualizado en un sistema 2x2, resolverlo por sustitución y validar visualmente.
* **Recursos:** Pizarras blancas (o papelógrafo) por grupos, tu herramienta web propia.

**1. Apertura (Reto Inicial - 20 min)**

* **Reto:** Proyecta un problema integrado (Ej: Una planta produce dos tipos de aleaciones/productos financieros. El producto A requiere 2 horas de máquina y $5 de materia prima; el B requiere 3 horas y $2. Disponemos de 100 horas y $120. ¿Cuántos productos de cada tipo se pueden hacer?).
* **Preguntas motivadoras:**
1. ¿Cuáles son las variables desconocidas aquí?
2. ¿Qué restricciones nos impone la realidad del problema?
3. Si adivinaran una respuesta, ¿cómo comprobarían si es correcta sin usar matemáticas avanzadas?


* *Nota:* No expliques cómo resolverlo aún.

**2. Exploración (15 min)**

* En grupos de 3, los estudiantes intentan plantear las ecuaciones y proponer una solución intuitiva.
* El docente circula por el aula escuchando las hipótesis y anotando enfoques interesantes.

**3. Desarrollo Conceptual (15 min)**

* Formalización breve (Instrucción por pares): Pide a un grupo que comparta sus ecuaciones.
* Define formalmente qué es un sistema lineal y qué significa "solución" (el punto donde las verdades de ambas ecuaciones se cruzan).
* Muestra, en máximo 5 minutos, la solución en tu herramienta web. Destaca la intersección de las rectas.

**4. Actividad Guiada y Colaborativa (30 min)**

* Presenta el método de **sustitución** como una forma analítica de hallar ese punto de corte.
* Los grupos resuelven el sistema inicial planteado usando este método.
* Si un grupo termina rápido, pídeles que alteren un coeficiente en el problema original para ver qué sucede.

**5. Aplicación (20 min)**

* Entrega a cada grupo un nuevo escenario (uno orientado a ingeniería civil/sistemas y otro a finanzas).
* Deben plantear el sistema, resolverlo por sustitución e ingresar a tu herramienta web desde sus celulares/laptops para validar gráficamente que su cálculo manual coincide con la gráfica.

**6. Cierre y Reflexión (10 min)**

* Preguntas de cierre: ¿Qué pasaría físicamente (en la fábrica o en la bolsa) si las dos líneas en la aplicación web fueran paralelas? ¿Y si fueran la misma línea?

**7. Actividad Final de Consolidación (10 min)**

* **Ticket de salida (One-Minute Paper):** Cada estudiante escribe en un papel: 1) El concepto más claro de hoy. 2) La duda más grande que aún tienen sobre los sistemas de ecuaciones. (Esto te servirá de insumo para el viernes).

---

### Sesión 2: Viernes (1 Hora) - Eliminación e Igualación

**Información General**

* **Tema:** Métodos de Eliminación (Reducción) e Igualación.
* **Objetivo:** Resolver sistemas lineales identificando el método algebraico más eficiente (eliminación o igualación) según la estructura del problema.
* **Recursos:** Notas del "Ticket de salida" del miércoles, pizarra.

**1. Apertura (Reto Inicial - 10 min)**

* **Reto:** Proyecta un sistema donde la sustitución sea matemáticamente engorrosa (ej. con fracciones complejas: $17x - 13y = 4$ y $17x + 13y = 30$).
* **Preguntas motivadoras:**
1. Si usamos sustitución aquí, ¿qué problema enfrentaremos?
2. ¿Habrá alguna manera de "sumar" estas verdades para desaparecer un problema?



**2. Exploración (10 min)**

* Pide a los estudiantes que discutan en parejas durante 3 minutos cómo podrían resolverlo sin despejar una variable primero.

**3. Desarrollo Conceptual (10 min)**

* Aclara dudas del "Ticket de salida" anterior.
* Teoría mínima: Explica el principio de equivalencia (si $A=B$ y $C=D$, entonces $A+C=B+D$).
* Muestra cómo esto fundamenta el método de **eliminación** y cómo la transitividad ($A=B$ y $A=C \implies B=C$) fundamenta la **igualación**.

**4. Actividad Guiada y Colaborativa (15 min)**

* Divide la clase en dos. A la mitad asígnale resolver un nuevo problema de balance de masa (ingeniería) o equilibrio de mercado (economía) usando Eliminación. A la otra mitad, Igualación.

**5. Aplicación (10 min)**

* Una pareja de cada lado se reúne (formando grupos de 4) y comparan resultados. Deben debatir qué método fue más rápido para los coeficientes dados y por qué.

**6. Cierre y Reflexión (5 min)**

* Pregunta abierta: Sabiendo que los lunes usaremos Python (NumPy/SciPy) para matrices gigantes, ¿por qué creen que los computadores prefieren usar variantes de la eliminación (como veremos más adelante en Gauss-Jordan) en lugar de la sustitución?

**7. Actividad Final de Consolidación (5 min)**

* **Votación rápida (Mano alzada o Mentimeter):** Proyecta 3 sistemas de ecuaciones diferentes. Para cada uno, los estudiantes deben votar rápidamente qué método usarían (Gráfico en tu app, Sustitución, Igualación o Eliminación) basándose únicamente en la "forma" de la ecuación, justificando su instinto.

Esta estructura te garantiza que los estudiantes construyan el concepto matemático antes de mecanizarlo, preparándolos perfectamente para el laboratorio de Python del lunes. ¿Deseas hacer algún ajuste en los tiempos o en los casos de estudio sugeridos?