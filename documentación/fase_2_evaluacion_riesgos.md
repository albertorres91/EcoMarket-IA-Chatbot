## Fase 2: Evaluación de Fortalezas, Limitaciones y Riesgos Éticos

# Análisis de la Solución: Modelo Híbrido con Fine-Tuning y Orquestación Inteligente

# Fortalezas:

Máxima precisión en datos críticos: al utilizar llamadas directas a APIs para el 80% de las consultas transaccionales (estado del pedido, devoluciones), se elimina casi por completo el riesgo de errores o "alucinaciones" en la información más sensible para el cliente.

Disponibilidad 24/7: la solución puede resolver la gran mayoría de las consultas de forma instantánea y a cualquier hora, reduciendo el tiempo de respuesta promedio de 24 horas a segundos.

Identidad de marca coherente: el proceso de fine-tuning permite que el LLM aprenda y adopte el tono de voz, la empatía y los valores de sostenibilidad de EcoMarket, ofreciendo una experiencia de marca consistente que un modelo genérico no podría replicar.

Optimización de costos: reservar el uso del LLM más costoso solo para el 20% de las consultas complejas y usar llamadas a API (mucho más económicas) para el 80% restante, genera un ahorro operativo significativo a escala.

# Limitaciones:

Complejidad en la implementación: esta arquitectura tiene más componentes (clasificador, módulo de reglas, LLM) que deben ser desarrollados, integrados y mantenidos, lo que incrementa el tiempo y el coste inicial del proyecto.

Rigidez del clasificador: el orquestador inicial es un punto potencial de fallo. Si clasifica incorrectamente una consulta compleja como "transaccional", podría generar una respuesta insatisfactoria y frustrar al cliente.

Dependencia de datos de calidad: la efectividad del fine-tuning depende directamente de la calidad y cantidad de los datos históricos. Si los datos son escasos, inconsistentes o contienen sesgos, el modelo los heredará.

Menor flexibilidad ante consultas mixtas: le costaría más gestionar de forma fluida una consulta que combine una pregunta transaccional con una abierta (ej: "¿Dónde está mi pedido y por qué su empaque no parecía muy ecológico?").

# Riesgos Éticos:

Privacidad de datos en el entrenamientoe el riesgo principal, reside en el uso de conversaciones pasadas para el fine-tuning. Es necesario aplicar técnicas de anonimización de datos extremadamente robustas para eliminar toda la Información de identificación personal. Un fallo en este proceso podría "incrustar" datos privados de clientes en el modelo, creando una brecha de seguridad muy grave.

Sesgo inherente y amplificado: el modelo aprenderá de los agentes humanos. Si en el pasado existieron sesgos (conscientes o inconscientes) en la forma de tratar a ciertos clientes, el modelo los aprenderá y los aplicará a escala, perpetuando un trato desigual.

Alucinaciones en casos complejos: aunque mitigado para datos de pedidos, el LLM aún puede "alucinar" al gestionar el 20% restante de los casos por ser complejos, inventando políticas de la empresa o detalles de productos que no existen si la información no se encuentra en su base de conocimiento.

Impacto laboral y deshumanización: el objetivo debe ser claro: empoderar a los agentes, no reemplazarlos. Se debe gestionar el cambio cultural para que los agentes vean la IA como una herramienta que les libera de tareas monótonas para convertirse en especialistas en resolución de problemas complejos. Si no se maneja bien, puede generar miedo, desmotivación y la percepción de que el servicio se está deshumanizando.
