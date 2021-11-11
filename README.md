# TC2008B.1-Multiagentes
Este es el repositorio de código para el proyecto de autómatas para simular tráfico y optimizarlo.

### Conformación del equipo:

#### Integrantes del equipo:
* Eduardo Rodríguez Gil (A01274913)
* Michelle Aylin Calzada Montes (A01706202)
* Manolo Ramírez Pintor (A01706155)
<br>

#### Fortalezas y áreas de oportunidad:
Fortalezas:
* __Eduardo__ - Python, C#
* __Michelle__ - Python, C#
* __Manolo__ - Python, C#

Áreas de oportunidad:
* __Eduardo__ - Distraerme lo menos posible para ser más productivo.
* __Michelle__ - Mejorar el rendimiento de mi hardware.
* __Manolo__ - Procastinar menos para trabajar mejor.
<br>


#### Expectativas del bloque
Aprender a utilizar Unity sobre los sistemas multiagentes para poder usarlo en interligencia artificial para videojuegos. 
<br>

#### Compromisos para lograrlo
* Tener una buena organización.
* No dejar todo para la semana 5.
* Aprender a utilizar las herramientas.
* Acercarnos más con los profesores.
<br>

### Creación de herramientas de trabajo colaborativo:

#### Herramientas de trabajo colaborativo

* Este repositorio para el trabajo principal.
* Discord y WhatsApp para comunicación.
<br>

### Propuesta formal del reto:
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
    a. (Identificar de manera completa los agentes y las posibles relaciones entre los mismos)
    * Agentes reactivos simples:
        * Son agentes que toman desiciones de forma aleatoria sin tomar en cuenta el estado del entorno o en otras palabras no son conscientes del mundo y las causas de las acciones realizadas.<br><br>

    * Agentes basados en objetivos:
        * Son agentes que toman desiciones basadas en el estado del entorno, el cambio del mismo y las consecuencias de las acciones que se toman. Es decir que son conscientes del entorno y lo que sucede en él.<br><br>

    * Diagrama de clase presentando los distintos agentes involucrados.
        * Imagen
    * Diagrama de protocolos de interacción.
        * Imagen
    <br><br>

3. __Plan de trabajo y aprendizaje adquirido.__
    _Incluir el plan de trabajo actualizado y el aprendizaje adquirido como equipo_
    * Las actividades pendientes y el tiempo en el que se realizarán.
    * Para las actividades planeadas para la primera revisión, los responsables de llevarlas a cabo, la fecha en las que las realizarán y el intervalo de esfuerzo estimado.