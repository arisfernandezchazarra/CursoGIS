# UNIDAD 5 - ANÁLISIS DETALLADO DE LA DISTRIBUCIÓN DE BD

## 1. Formas de distribución.

Los sistemas de gestión de bases de datos (SGBD) pueden distribuirse de varias formas para gestionar datos en entornos distribuidos o con múltiples nodos. Estas formas de distribución incluyen:

1. **Réplicas:** Los datos se copian y almacenan en varios nodos o servidores. Cada réplica contiene una copia completa de los datos y se mantiene sincronizada para consultas y actualizaciones.
    
2. **Fragmentación:** Los datos se dividen en fragmentos más pequeños y se distribuyen entre diferentes nodos o servidores. Cada fragmento contiene una porción de los datos, lo que permite una distribución eficiente de la carga de trabajo y consultas paralelas.
    
3. **Particionamiento:** Los datos se dividen en particiones basadas en criterios específicos, como rangos de valores o funciones de hash. Cada partición se asigna a un nodo o servidor diferente para una mejor escalabilidad y distribución equilibrada de los datos.
    
4. **Sharding:** Los datos se distribuyen en múltiples servidores o clústeres, y cada servidor se encarga de un subconjunto de los datos. Esto permite una alta escalabilidad y rendimiento en entornos de gran escala.
    
5. **Federación:** Se combina múltiples bases de datos independientes en un sistema lógico único. Cada base de datos mantiene su autonomía y se puede acceder de forma independiente, mientras que un componente de federación coordina la comunicación y el acceso a las bases de datos federadas.
    
Estas formas de distribución de SGBD se utilizan según las necesidades específicas de la aplicación y el entorno. Cada enfoque tiene sus propias ventajas y desafíos en términos de escalabilidad, rendimiento y consistencia de los datos. La elección de la forma de distribución adecuada depende de factores como la carga de trabajo, la cantidad de datos y los requisitos de rendimiento de la aplicación.

<img src="https://images2.imgbox.com/bf/e4/nMEJoyh5_o.png" alt="image host" width="400" style="display: block; margin: 0 auto;" />
### Multiproceso y multihilo

Dependiendo del tipo de Gestión de los procesos, podemos clasificar los SGBD como:

#### Multiproceso

Un sistema de gestión de bases de datos (SGBD) multiproceso es aquel que tiene la capacidad de ejecutar múltiples procesos o subprocesos al mismo tiempo para realizar diversas tareas relacionadas con la administración de la base de datos. Estos SGBD están diseñados para optimizar el uso de los recursos de hardware y mejorar el rendimiento al permitir la ejecución paralela de operaciones.

Las características principales de los SGBD multiproceso son:

- **Ejecución concurrente:** Los SGBD multiproceso pueden llevar a cabo múltiples operaciones simultáneamente, lo que permite procesar consultas, actualizaciones y otras tareas de gestión de datos de manera paralela.
    
- **Control de concurrencia:** Estos sistemas se encargan de administrar la concurrencia y garantizar la consistencia de los datos mediante el uso de técnicas como el bloqueo de recursos, la serialización de transacciones y la resolución de conflictos.
    
- **Aprovechamiento de múltiples núcleos de CPU:** Los SGBD multiproceso están diseñados para hacer un uso eficiente de los múltiples núcleos de CPU presentes en los sistemas actuales, distribuyendo las tareas de procesamiento entre diferentes núcleos para mejorar el rendimiento.
    
- **Paralelismo en consultas:** Estos sistemas pueden descomponer una consulta compleja en subconsultas más pequeñas y procesarlas en paralelo utilizando hilos o procesos separados, lo que acelera la ejecución de consultas largas o que requieren un alto poder de cálculo.
    
- **Gestión de transacciones concurrentes:** Los SGBD multiproceso implementan mecanismos para administrar eficazmente las transacciones que se ejecutan de manera concurrente, asegurando la integridad de los datos y evitando problemas como lecturas sucias o conflictos de actualización.
    
La utilización de un SGBD multiproceso puede mejorar significativamente el rendimiento y la capacidad de respuesta de una base de datos al permitir la ejecución simultánea de múltiples tareas. No obstante, es importante realizar una planificación adecuada de los recursos y gestionar la concurrencia de forma apropiada para evitar problemas como bloqueos o conflictos de acceso a los datos.

#### Multihilo

Un sistema de gestión de bases de datos (SGBD) multihilo es aquel que utiliza varios hilos de ejecución para realizar tareas relacionadas con la gestión de la base de datos de manera concurrente. Estos hilos permiten que diferentes operaciones se ejecuten al mismo tiempo, lo que mejora el rendimiento y la capacidad de respuesta del sistema.

Las características principales de un SGBD multihilo son:

- **Hilos de ejecución:** Los SGBD multihilo emplean hilos para llevar a cabo distintas tareas, como recibir consultas, procesar transacciones y gestionar bloqueos y concurrencia.
    
- **Paralelismo:** Al utilizar hilos de ejecución, el SGBD puede realizar múltiples operaciones de forma simultánea, aprovechando los recursos de hardware disponibles y acelerando el procesamiento de consultas y transacciones.
    
- **Gestión de concurrencia:** Los SGBD multihilo implementan mecanismos para controlar y gestionar la concurrencia, evitando conflictos y asegurando la coherencia de los datos. Esto incluye técnicas de bloqueo, serialización de transacciones y resolución de conflictos.
    
- **Mejora del rendimiento:** Al utilizar hilos de ejecución concurrentes, el SGBD puede aumentar el rendimiento al realizar múltiples tareas al mismo tiempo, reduciendo la latencia y mejorando el tiempo de respuesta.
    
- **Escalabilidad:** Los SGBD multihilo son escalables, lo que significa que pueden manejar una mayor carga de trabajo distribuyendo y ejecutando tareas en varios hilos, lo que permite un uso más eficiente de los recursos del sistema.
    
La utilización de un SGBD multihilo puede mejorar significativamente el rendimiento y la eficiencia de la gestión de bases de datos al permitir la ejecución concurrente de múltiples tareas. Sin embargo, es importante tener en cuenta aspectos como la sincronización y la gestión de la concurrencia para evitar problemas como bloqueos y condiciones de carrera.

<img src="https://images2.imgbox.com/7f/fc/267SUVGo_o.png" alt="image host" width="400" style="display: block; margin: 0 auto;" />

---

## 2. Arquitectura ANSI/X3/SPARC.

La arquitectura ANSI/X3/SPARC, también conocida como arquitectura de tres esquemas, es un modelo conceptual utilizado en el diseño de sistemas de gestión de bases de datos (SGBD). Esta arquitectura, desarrollada por el comité ANSI y el grupo X3/SPARC en los años 70, ha sido ampliamente adoptada en la industria de bases de datos.

La arquitectura ANSI/X3/SPARC se basa en tres niveles o esquemas:

<img src="https://images2.imgbox.com/3e/1a/JNvnEho4_o.png" alt="image host" width="400" style="display: block; margin: 0 auto;" />

1. **Nivel externo o de vistas:** Este nivel permite a los usuarios finales ver y acceder a los datos según sus necesidades individuales. Cada usuario puede tener su propia vista personalizada de los datos, independientemente de cómo se almacenen internamente.
    
2. **Nivel conceptual o lógico:** En este nivel se describe la estructura lógica de la base de datos sin considerar los detalles físicos de almacenamiento. Aquí se definen los esquemas conceptuales que representan las entidades, las relaciones y las restricciones de integridad de la base de datos.
    
3. **Nivel interno o físico:** Este nivel se encarga de la forma en que los datos se almacenan físicamente en los dispositivos de almacenamiento. Define las estructuras de almacenamiento, los índices y las técnicas de acceso utilizadas para la eficiente recuperación de datos.
    
La arquitectura ANSI/X3/SPARC se centra en la separación de preocupaciones, lo que permite que cada nivel se modifique de forma independiente sin afectar a los demás. Esto facilita la modularidad y el mantenimiento de los sistemas de bases de datos.

Esta arquitectura ha sido fundamental en el desarrollo de los SGBD modernos y ha influido en la estandarización de lenguajes de consulta como SQL. Además, ha sentado las bases para otros modelos de bases de datos, como el modelo relacional.

<img src="https://images2.imgbox.com/ec/c7/hPNv3ZSJ_o.png" alt="image host" width="400" style="display: block; margin: 0 auto;" />

---

## 3. Transacciones distribuidas.

Las transacciones distribuidas en los sistemas de gestión de bases de datos (SGBD) son operaciones que involucran múltiples bases de datos ubicadas en diferentes sistemas o sitios interconectados en una red. Estas transacciones se realizan de manera coordinada para asegurar la integridad y consistencia de los datos en todos los sitios involucrados.

Las características clave de las transacciones distribuidas en SGBD son:

1. **Atomicidad:** Las transacciones distribuidas se consideran como una unidad atómica, lo que significa que se ejecutan por completo o se deshacen en caso de fallo. Si una parte de la transacción falla en algún sitio, se revierten todas las operaciones realizadas en todos los sitios para mantener la consistencia de los datos.
    
2. **Coordinación:** Para garantizar la consistencia, las transacciones distribuidas requieren de un coordinador central o de un protocolo de coordinación distribuido. El coordinador supervisa y coordina las operaciones en los sitios participantes, asegurando que se cumplan las propiedades ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad) de las transacciones.
    
3. **Protocolos de commit:** Los protocolos de commit se utilizan para garantizar que las transacciones distribuidas se confirmen o deshagan de manera coherente. Estos protocolos aseguran que todos los sitios participantes estén de acuerdo en confirmar o deshacer la transacción, evitando incoherencias en los datos.
    
4. **Concurrencia y aislamiento:** Las transacciones distribuidas deben manejar la concurrencia y el aislamiento entre transacciones concurrentes en diferentes sitios. Se utilizan técnicas de bloqueo y control de concurrencia para asegurar que las transacciones se ejecuten de forma aislada y sin interferencias.
    
5. **Tolerancia a fallos:** Dado que las transacciones distribuidas involucran múltiples sitios, es importante considerar la tolerancia a fallos. Los SGBD distribuidos implementan mecanismos para manejar fallos en los sitios participantes, como la recuperación de errores y la replicación de datos.
    
Estas transacciones aseguran la consistencia de los datos a través de la coordinación, cumplimiento de protocolos y manejo de la concurrencia y los fallos.

<img src="https://images2.imgbox.com/b9/10/C75TjUha_o.png" alt="image host" width="400" style="display: block; margin: 0 auto;" />

---

## 4. Mecanismos de distribución de datos.

Existen varios mecanismos utilizados en sistemas de gestión de bases de datos distribuidas (SGBDD) para distribuir y administrar eficientemente los datos. Estos mecanismos incluyen:

1. **Fragmentación:** Se divide una tabla o conjunto de datos en fragmentos más pequeños que se distribuyen en diferentes sitios. Esto permite un almacenamiento y acceso eficiente a los datos distribuidos.
    
2. **Replicación:** Se crean copias idénticas de los datos en múltiples sitios. Esto mejora la disponibilidad y el rendimiento al permitir el acceso local a los datos en cada sitio.
    
3. **Distribución basada en particionamiento:** Se divide una tabla en particiones basadas en algún criterio, como la clave primaria. Cada partición se asigna a un sitio diferente, lo que facilita la distribución y el procesamiento paralelo de las consultas.
    
4. **Indexación distribuida:** Se crean índices distribuidos que contienen información sobre la ubicación de los datos en diferentes sitios. Esto permite un acceso rápido y eficiente a los datos distribuidos.
    
5. **Optimización de consultas distribuidas:** Se utilizan técnicas de optimización para mejorar el rendimiento de las consultas distribuidas, considerando la ubicación de los datos y los costos de comunicación entre sitios.
    
Estos mecanismos permiten que los SGBDD almacenen y gestionen grandes volúmenes de datos de forma distribuida, aprovechando la capacidad de procesamiento y almacenamiento de múltiples sitios. Esto mejora el rendimiento, la disponibilidad y la escalabilidad de los sistemas de bases de datos distribuidas.