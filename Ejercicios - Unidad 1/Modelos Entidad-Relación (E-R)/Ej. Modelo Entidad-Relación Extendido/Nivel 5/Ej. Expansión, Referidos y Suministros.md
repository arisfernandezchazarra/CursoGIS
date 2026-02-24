#modelo-ER   #ejm   [[ER extendido con la notación de Chen -Ejm]]

Llegamos al **Nivel 5**, el "Boss Final". Este nivel separa a los alumnos que simplemente "dibujan" de los que realmente entienden la **lógica de negocio compleja**. Aquí es donde el diseño se vuelve una herramienta de ingeniería.

---
### Enunciado Nivel 5: "Expansión, Referidos y Suministros"

 **Contexto:**

  "RetroPixel" ya no es una tienda de barrio; es una franquicia nacional. El sistema debe ahora gestionar relaciones internas de los clientes y una cadena de suministro compleja entre proveedores y sus diferentes sedes físicas.

**Reglas de negocio:**

1. **Relación Reflexiva (Sistema de Referidos):** Para ganar clientes, han lanzado un plan de "Amigos".

    - Un cliente veterano puede **recomendar** a nuevos clientes.

    - Un cliente nuevo solo puede ser recomendado por **un único** veterano.

    - Un veterano puede haber recomendado a **muchos** clientes nuevos.

    - Interesa saber la **Bonificación** (descuento) que se le aplicó al veterano por cada recomendación realizada.

2. **Relación Ternaria (Gestión de Suministros):** La empresa tiene varias **Sedes** (tiendas físicas en distintas ciudades).

    - Necesitamos saber qué **Proveedor** suministra qué **Producto** a qué **Sede**.

    - Un proveedor puede suministrar el mismo producto a varias sedes.

    - Una sede puede recibir el mismo producto de diferentes proveedores.

    - Es fundamental registrar la **Cantidad** de producto que se entrega en cada operación de suministro.

3. **Entidad Sede:** De cada sede guardamos un ID de sede, la ciudad y el nombre del gerente.
