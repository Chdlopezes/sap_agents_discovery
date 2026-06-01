Hola. Necesito que trabajes como asistente de enriquecimiento de datos para un CSV exportado desde SAP Discovery Center llamado “AI Features Data.csv”.

El archivo contiene registros de AI Features & Agents con columnas como:

- Name
- AI Type
- Commercial Type
- Product
- Description
- Product Category
- Package
- Quick Filters
- Availability
- Identifier
- Detail Page

La tarea consiste en enriquecer el CSV y generar archivos Excel por lotes.

Debes seguir estrictamente las reglas indicadas abajo.

OBJETIVO DEL LOTE

Procesa únicamente el siguiente lote de registros:

- Registro inicial: [INDICAR_REGISTRO_INICIAL]
- Tamaño del lote: [INDICAR_TAMAÑO_DEL_LOTE, normalmente 10]

Importante:
- El registro 1 corresponde a la primera fila de datos del CSV, no al encabezado.
- Si el CSV termina antes de completar el lote, procesa solo los registros disponibles.
- No proceses registros anteriores ni posteriores al lote solicitado.

ARCHIVO DE SALIDA

Genera un archivo Excel `.xlsx` con exactamente 2 hojas:

1. AI Features & Agents
2. Pricing Premium

No agregues hojas adicionales.
No agregues columnas adicionales salvo que sean las definidas en este prompt.
No incluyas comentarios, notas técnicas, hojas de auditoría ni fuentes externas.

---

HOJA 1: “AI Features & Agents”

Para cada registro del lote, debes usar únicamente la información del enlace incluido en la columna:

- Detail Page

Reglas estrictas:

- Entra al link de “Detail Page”.
- No uses páginas alternativas de sap.com.
- No uses blogs.
- No uses documentación general.
- No uses SAP Notes, KBAs ni SAP Help Portal para llenar esta hoja.
- No uses conocimiento previo.
- No completes información por inferencia externa.
- Si la información no aparece en la página, escribe: “No disponible en la página Detail Page”.

Debes conservar las columnas originales relevantes del CSV y agregar las siguientes columnas enriquecidas:

- Overview
- Beneficios
- Business Value

El contenido debe estar en español, redactado de forma clara, ejecutiva y resumida.

Criterios de redacción:

Overview:
- Resume qué hace la funcionalidad o agente.
- Explica su propósito principal.
- No traduzcas literalmente si la página es extensa; sintetiza.

Beneficios:
- Resume los beneficios operativos o funcionales.
- Puedes usar frases separadas por punto y coma.
- No inventes beneficios no mencionados o no derivables directamente del Detail Page.

Business Value:
- Resume el valor de negocio.
- Enfócate en eficiencia, automatización, reducción de esfuerzo, mejor toma de decisiones, productividad, control, experiencia de usuario o calidad del proceso, solo si la página lo permite.
- No uses promesas exageradas.

---

HOJA 2: “Pricing Premium”

Esta hoja solo debe incluir registros cuyo campo:

- Commercial Type = Premium

Reglas estrictas:

- Si un registro no es Premium, no lo incluyas en esta hoja.
- Para los registros Premium, usa únicamente la sección “Pricing Details” de la misma página indicada en “Detail Page”.
- No uses ninguna otra fuente.
- No uses SAP Store, documentación externa, blogs, KBAs ni conocimiento previo.
- Si la página no tiene sección “Pricing Details”, escribe explícitamente: “No se encontró sección Pricing Details en la página Detail Page”.
- Si existe la sección pero no hay pricing concreto, escribe: “La sección Pricing Details no contiene información de pricing explícita”.
- Si no hay ningún registro Premium en el lote, la hoja debe existir de todas formas, pero solo con encabezados.

Columnas recomendadas para esta hoja:

- Name
- Product
- Commercial Type
- Package
- Identifier
- Detail Page
- Pricing Details

El campo “Pricing Details” debe estar en español, pero sin alterar el significado del texto original.

---

FORMATO DEL EXCEL

El archivo debe tener formato profesional y limpio:

- Encabezados en negrita.
- Ajuste de ancho de columnas.
- Texto ajustado en celdas largas.
- Congelar la primera fila si es posible.
- No usar colores excesivos.
- Mantener nombres exactos de las dos hojas:
  - AI Features & Agents
  - Pricing Premium

Nombre sugerido del archivo:

AI_Features_Data_lote_[INICIO]_[FIN]_enriquecido.xlsx

Ejemplo:

AI_Features_Data_lote_56_65_enriquecido.xlsx

---

CONTROL DE CALIDAD ANTES DE ENTREGAR

Antes de entregar el archivo, valida lo siguiente:

1. El Excel tiene exactamente 2 hojas.
2. No hay hojas adicionales.
3. La hoja “AI Features & Agents” tiene únicamente registros del lote solicitado.
4. La hoja “Pricing Premium” contiene solo registros con Commercial Type = Premium.
5. Si no hay Premium, la hoja “Pricing Premium” existe pero solo con encabezados.
6. No se usaron fuentes externas.
7. El archivo final es descargable en formato `.xlsx`.

---

RESPUESTA FINAL

Cuando termines, responde de forma breve indicando:

- Lote procesado.
- Número de registros procesados.
- Número de registros Premium incluidos en Pricing Premium.
- Link de descarga del archivo Excel.

No incluyas todo el contenido del Excel en el mensaje final; solo entrega el archivo.

Ejemplo de estructura esperada del Excel
Hoja 1: AI Features & Agents

| Name                   | AI Type         | Commercial Type | Product      | Description                  | Product Category | Package | Quick Filters | Availability   | Identifier | Detail Page   | Overview                                      | Beneficios                             | Business Value                                 |
| ---------------------- | --------------- | --------------- | ------------ | ---------------------------- | ---------------- | ------- | ------------- | -------------- | ---------- | ------------- | --------------------------------------------- | -------------------------------------- | ---------------------------------------------- |
| Nombre de la capacidad | Feature / Agent | Base / Premium  | Producto SAP | Descripción original del CSV | Categoría        | Paquete | Filtros       | Disponibilidad | ID         | Link original | Resumen en español basado solo en Detail Page | Beneficios resumidos desde Detail Page | Valor de negocio sintetizado desde Detail Page |


Hoja 2: Pricing Premium

| Name                        | Product      | Commercial Type | Package | Identifier | Detail Page   | Pricing Details                                                 |
| --------------------------- | ------------ | --------------- | ------- | ---------- | ------------- | --------------------------------------------------------------- |
| Nombre de capacidad Premium | Producto SAP | Premium         | Paquete | ID         | Link original | Información extraída únicamente de la sección “Pricing Details” |


Si el lote no tiene Premium:
| Name | Product | Commercial Type | Package | Identifier | Detail Page | Pricing Details |
| ---- | ------- | --------------- | ------- | ---------- | ----------- | --------------- |
