# IA Generativa para Atención al Cliente en EcoMarket


Este repositorio contiene una solución práctica que aplica técnicas de ingeniería de prompts para resolver el caso de estudio de EcoMarket. El objetivo es diseñar un asistente de IA capaz de gestionar consultas de clientes de manera eficiente y empática, utilizando un Modelo de Lenguaje Grande (LLM) ejecutado localmente.

El proyecto se basa en la arquitectura del curso de Ingeniería de Prompts Práctica, pero ha sido adaptado para funcionar sin necesidad de una API de pago, garantizando la reproducibilidad y eliminando los riesgos de seguridad asociados a las claves de API.

## Diseño de la Solución: Fases del Taller

El desarrollo de este proyecto siguió una metodología estructurada en tres fases, cubriendo desde la estrategia de alto nivel hasta la prueba de concepto técnica.

*   ### [FASE 1: Selección y Justificación del Modelo de IA](./DOCUMENTACION/FASE_1-SELECCION_DEL_MODELO.md)
    En esta fase se proponen y justifican dos arquitecturas de IA de nivel empresarial para resolver el problema de EcoMarket, considerando factores como costo, escalabilidad y precisión.

*   ### [FASE 2: Evaluación de Fortalezas, Limitaciones y Riesgos Éticos](./DOCUMENTACION/FASE_2-EVALUACION_DE_RIESGOS.md)
    Aquí se realiza un análisis crítico de las soluciones propuestas, evaluando sus implicaciones prácticas y, fundamentalmente, los riesgos éticos relacionados con la privacidad de los datos, los sesgos y el impacto laboral.

*   ### **FASE 3: Implementación del Prototipo (Este Código)**
    Esta fase consiste en la implementación de un prototipo funcional que valida los principios de la **Ingeniería de Prompts**. Se utiliza un modelo de lenguaje local (vía Ollama) para demostrar cómo guiar el comportamiento de la IA para resolver consultas de clientes de forma segura y coherente, aplicando las lecciones de las fases 1 y 2.

---

## Implementación del Prototipo


## Características Principales

Ejecución Local: Utiliza [Ollama](https://ollama.com/) para ejecutar modelos de lenguaje potentes (como Llama 3) de forma local, eliminando la dependencia de APIs externas y los costos asociados.

Enfoque en Prompt Engineering: La lógica central reside en el archivo settings.toml, que permite un desarrollo iterativo y claro de los prompts.

Caso de Estudio Aplicado: Los prompts y la lógica están diseñados específicamente para 
resolver los desafíos de EcoMarket: consulta de pedidos y gestión de devoluciones.

## Configuración del Entorno.

Para ejecutar este proyecto, no necesitas una clave de API de OpenAI. En su lugar, usaremos Ollama para servir el modelo localmente.

1. Instalar Ollama

Ve al sitio web oficial: https://ollama.com/
Descarga e instala la aplicación para tu sistema operativo (Windows, macOS o Linux).
Una vez instalado, asegúrate de que Ollama se esté ejecutando en segundo plano (deberías ver su icono en la barra de tareas o en la barra de menú).

2. Clonar el Repositorio y Preparar el Entorno

Abre tu Terminal y clona este proyecto:

```bash
git clone https://github.com/tu-usuario/tu-proyecto-ecomarket.git
cd tu-proyecto-ecomarket
```

Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar las Dependencias

Instala las librerías de Python necesarias desde requirements.txt:

```bash
pip install -r requirements.txt
```

4. Descargar el Modelo de Lenguaje

Abre una nueva Terminal (o Símbolo del sistema) y ejecuta el siguiente comando para que Ollama descargue el modelo llama3:

```bash
ollama pull llama3
```

Espera a que la descarga finalice. Este modelo ahora está disponible en tu máquina para ser utilizado por el script.

## Uso de la aplicación

El script app.py lee una consulta de cliente desde un archivo de texto, la procesa utilizando el LLM local y muestra la respuesta generada en la terminal.

Para ejecutar una consulta de estado de pedido:

```bash
python app.py prompts/consulta_pedido.txt
```

Para ejecutar una solicitud de devolución de producto:

```bash
python app.py prompts/solicitud_devolucionej1.txt
```
```bash
python app.py prompts/solicitud_devolucionej2.txt
``````
```bash
python app.py prompts/solicitud_devolucionej3.txt
``````
```bash
python app.py prompts/solicitud_devolucionej4.txt
```
## Estructura de Archivos

- app.py: La lógica principal de la aplicación. Lee los prompts, se comunica con el servidor de Ollama y muestra la respuesta.
- settings.toml: El corazón del proyecto. Aquí se definen los prompts, el rol del asistente y otros parámetros, permitiendo una   fácil iteración y mejora.
- requirements.txt: Contiene las dependencias de Python para asegurar un entorno reproducible.
- prompts/: Carpeta que contiene los archivos de texto con las consultas de los clientes para probar el sistema.
- consulta_pedido.txt: Ejemplo de un cliente preguntando por su pedido.
- solicitud_devolucion.txt: Ejemplo de un cliente queriendo devolver un producto.
- README.md: Instrucciones del uso de la aplcación.
-   `DOCUMENTACION/`: Carpeta que contiene el análisis estratégico del proyecto.
    -   `FASE_1-SELECCION_DEL_MODELO.md`
    -   `FASE_2-EVALUACION_DE_RIESGOS.md`


## Técnicas de Prompt Engineering Aplicadas

Este proyecto utiliza varias de las técnicas discutidas en el curso para asegurar respuestas precisas, coherentes y alineadas con la marca EcoMarket. Los prompts se configuran en settings.toml.

1. Role Prompting (Asignación de Rol)
Se le asigna una personalidad y un contexto claros al modelo para que sus respuestas sean consistentes con el tono de voz de EcoMarket. Esto se define en el role_prompt.

```Toml
[prompts]
role_prompt = """
Eres 'EcoAsistente', un agente de atención al cliente de EcoMarket. Tu tono es siempre amable, proactivo y empático, reflejando nuestros valores de sostenibilidad y confianza. Nunca inventas información.
"""
```

2. Context Injection (Inyección de Contexto)
En lugar de depender únicamente del conocimiento pre-entrenado del modelo, inyectamos datos específicos y en tiempo real en el prompt. Esto es crucial para evitar "alucinaciones" y responder con datos precisos. En app.py, el contenido del archivo de consulta del usuario se inserta en una plantilla más grande que incluye estos datos.

Ejemplo Conceptual:

Para una consulta de pedido, el sistema primero buscaría los detalles en una base de datos y luego los "inyectaría" en el prompt que se envía al LLM para que este formule una respuesta humana.

3. Instrucciones Paso a Paso (Chain-of-Thought)
Para tareas complejas como la gestión de una devolución, se le pide al modelo que siga una secuencia lógica de pasos. Esto descompone el problema y guía al modelo hacia la respuesta correcta, asegurando que se sigan las políticas de la empresa.

Ejemplo de Instrucción (settings.toml):

```Toml
[prompts]
instruction_prompt = """
El cliente quiere devolver un producto. Sigue estos pasos:
1. Analiza el producto que el cliente menciona.
2. Consulta la política de devoluciones proporcionada en el contexto para ver si el producto es elegible.
3. Si es elegible, informa al cliente y explícale los siguientes pasos.
4. Si NO es elegible, comunícalo con empatía y explica claramente el motivo basado en la política.
"""
```