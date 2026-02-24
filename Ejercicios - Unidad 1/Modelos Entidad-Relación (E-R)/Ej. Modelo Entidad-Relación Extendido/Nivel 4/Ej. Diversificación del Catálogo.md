#modelo-ER   #ejm   [[ER extendido con la notación de Chen -Ejm]]

Este es el salto al **Modelo Entidad-Relación Extendido (EER)**. En el **Nivel 4**, introducimos la **Herencia** (Especialización/Generalización).

En programación (Java, C#, etc.), tus alumnos de DAW ya estarán viendo el concepto de "Clase Padre" y "Clase Hija". Aquí vamos a aplicar exactamente lo mismo a los datos.

---
### Enunciado Nivel 4: "Diversificación del Catálogo"

**Contexto:**

"RetroPixel" ha decidido dejar de vender solo videojuegos. Ahora también venden **Merchandising** (figuras, tazas, pósters). Para gestionar esto de forma eficiente, el sistema debe tratar a ambos como "Productos", pero manteniendo sus diferencias.

**Reglas de negocio (Jerarquía ISA):**

1. Tanto los **Videojuegos** como el **Merchandising** se consideran **Productos**.
    
    - Todos los productos tienen un **Código de Barras** (PK), un **Nombre** y un **Precio Base**.
        
2. De los **Videojuegos** (específicamente), queremos seguir guardando el **Género** y la **Calificación PEGI** (edad recomendada).
    
3. Del **Merchandising**, nos interesa el **Tipo** (ej: figura, prenda, papelería) y el **Peso** (para gastos de envío).
    
4. **Restricción de la Jerarquía:**
    
    - Es **Total**: No puede haber un producto en la base de datos que no sea o videojuego o merchandising.
        
    - Es **Exclusiva (Disjunta)**: Un producto no puede ser simultáneamente un videojuego y merchandising.