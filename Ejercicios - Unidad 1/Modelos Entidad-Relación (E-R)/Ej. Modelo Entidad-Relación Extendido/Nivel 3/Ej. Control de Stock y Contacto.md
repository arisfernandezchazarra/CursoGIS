### Enunciado Nivel 3: "Control de Stock y Contacto"

**Contexto:**

La tienda "RetroPixel" está creciendo. Ahora no les basta con saber que tienen el juego "Zelda", necesitan controlar cada **copia física** (ejemplar) que tienen en la estantería para saber su estado. Además, quieren mejorar la comunicación con los clientes.

**Nuevas Reglas de negocio:**

1. **Entidad Débil (Ejemplar):** De cada `Videojuego` existen varios `Ejemplares` físicos.
    
    - Cada ejemplar se identifica por un **Número de Serie local** (ej. copia 1, copia 2, copia 3...). Este número solo es único para ese juego concreto (puede haber una "copia 1" de Zelda y una "copia 1" de Mario).
        
    - De cada ejemplar queremos saber su **Estado de conservación** (Nuevo, Semi-nuevo, Dañado).
        
    - _Regla clave:_ Si un videojuego se elimina del catálogo, sus ejemplares desaparecen automáticamente.
        
2. **Atributo Multivaluado:** Los `Clientes` ahora pueden facilitar **varios números de teléfono** (móvil, casa, trabajo) para que la tienda les avise de ofertas.
      
3. **Atributo Compuesto:** De la **Dirección** del cliente queremos guardar de forma desglosada la Calle, el Número y el Código Postal.