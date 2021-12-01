# TC2008B.1-Multiagentes
Este es el repositorio de código para el proyecto de autómatas para simular tráfico y optimizarlo.

## Conformación del equipo:

### Integrantes del equipo:
* Eduardo Rodríguez Gil (A01274913)
* Michelle Aylin Calzada Montes (A01706202)
* Manolo Ramírez Pintor (A01706155)
<br>

### Fortalezas y áreas de oportunidad:
Fortalezas:
* __Eduardo__ - Python, C#
* __Michelle__ - Python, C#
* __Manolo__ - Python, C#

Áreas de oportunidad:
* __Eduardo__ - Distraerme lo menos posible para ser más productivo.
* __Michelle__ - Mejorar el rendimiento de mi hardware.
* __Manolo__ - Procastinar menos para trabajar mejor.
<br>


### Expectativas del bloque
Aprender a utilizar Unity sobre los sistemas multiagentes para poder usarlo en interligencia artificial para videojuegos. 
<br>

### Compromisos para lograrlo
* Tener una buena organización.
* No dejar todo para la semana 5.
* Aprender a utilizar las herramientas.
* Acercarnos más con los profesores.
<br>

## Creación de herramientas de trabajo colaborativo:

### Herramientas de trabajo colaborativo

* Este repositorio para el trabajo principal.
* Discord y WhatsApp para comunicación.
<br>

## Propuesta formal del reto:
1. __Descripción del reto a desarrollar.__<br>
    El crecimiento acelerado de las ciudades ha crecido mucho en los últimos años. El problema de esto es que se genera congestión y pérdidas de dinero porque se gasta más combustible durante la espera del tráfico.
    <br><br>
    Se han intentado utilizar estrategias para arreglar el problema del tráfico, por ejemplo el cobro de rutas de alta demanda. Pero provocó que ahora se congestionara tráfico en otras zonas.
    <br><br>
    Otra forma de solución que se intentó fue el "Hoy no circula", que no fue muy efectivo, ayudó poco en México.
    <br><br>
    El último recurso que queda para poder arreglar este problema es utilizar las Tecnologías de la Información y la Comunicación ya que ahora los avances tecnológicos que existen nos permiten la creación de sistemas de tráfico autónomos que pueden optimizarlo todo en base a las variables de tráfico actuales.
    <br><br>
    Para poner esto a prueba antes de sacarlo como tal a la vida real, se nos pide realizar una simulación en un entorno gráfico 3D utilizando Unity, donde los carros estarán controlados mediante autómatas y unos semáforos en una intersección de cuatro calles tomarán las mejores decisiones en base al tráfico actual.
    <br><br>
    __Las condiciones para esta prueba son las siguientes:__
    1. Las calles son de doble sentido
    2. La velocidad máxima es de 60km/h
    3. En cada camino los automóviles pueden ir derecho, girar a su izquierda o derecha
    4. Sólo un camino tendrá luz verde.
    5. Los semáforos están coordinados por una caja de control central.
    6. Los vehículos que transitan los caminos comunican a la caja de control sobre su destino. (derecho, izquierda, derecha) y tiempo aproximado de llegada.
    7. Si no hay vehículos, todos los semáforos deben ser rojos.
    
    &nbsp;
    El objetivo de la caja de control es minimizar el tiempo promedio de espera de los vehículos que cruzan la intersección.

    <br>

2. __Identificación de los agentes involucrados__
    a. (Identificar de manera completa los agentes y las posibles relaciones entre los mismos)<p>
    __Los tipos de agentes:__
    * Agentes reactivos simples:
        * Son agentes que toman desiciones de forma aleatoria sin tomar en cuenta el estado del entorno o en otras palabras no son conscientes del mundo y las causas de las acciones realizadas.<br><br>

    * Agentes basados en objetivos:
        * Son agentes que toman desiciones basadas en el estado del entorno, el cambio del mismo y las consecuencias de las acciones que se toman. Es decir que son conscientes del entorno y lo que sucede en él.<br><br>

    * __Diagrama de clase presentando los distintos agentes involucrados.__
        * Caja de control<br>
        ![Alt text](Diagramas/CajaContro.png?raw=true "Title")<br><br>
        * Carro<br>
        ![Alt text](Diagramas/Carro.png?raw=true "Title")<br><br>
        * Semáforo:<br>
        ![Alt text](Diagramas/Semaforo.png?raw=true "Title")<br><br>

    * __Diagrama de protocolos de interacción.__<br>
        ![Alt text](Diagramas/ProtocolosInteraccion.png?raw=true "Title")<br><br>

    __Agentes Involucrados:__
    * Carro:
        * Estos agentes determinarán el comportamiento de los semáforos a través de la comunicación con la caja de control. También los coches interactuarán entre ellos para evitar chocar<br><br>

    * Semáforo:
        * Son agentes que interactúan directamente con los carros y con la caja de control para recibir la información de los carros del entorno. Su función es cambiar de color e informar a los carros que pueden avanzar.<br><br>

    * Caja de control:
        * Es un agente que recibe la información de los carros para determinar qué semáforo se debe encender dependiendo de la prioridad que se deba establecer en cierta vialidad. <br><br>

3. __Plan de trabajo y aprendizaje adquirido.__<br>
    En este plan de trabajo asignamos las tareas a los integrantes del equipo en las áreas donde nos apasiona trabajar más y en donde sentimos que somos que tenemos un fuerte para hacer las cosas. Se puede ver cada tarea, el estatus, las fechas de inicio, entrega, la complejidad de la tarea y el estado (_No iniciado, En progreso y Completado_) para llevar un mejor control de cómo avanza nuestro proyecto.
    * Link del plan de trabajo: https://docs.google.com/spreadsheets/d/1SgBKHuhkFkiXe7oIPeWwVcgENM8nqlzAs02Dx2amhDM/edit#gid=0 <br><br>

4. __Despliegue de la aplicación__<br>
    La app se puede abrir desde Unity mientras el servidor de Python está corriendo en el servidor de IBM para recibir los datos generados y correr toda la simulación en el entorno gráfico 3D que hemos preparado.