## Fase 1: Selección y Justificación del Modelo de IA

A continuación, se presenta la solución del caso de estudio de EcoMarket. Se propone un modelo Híbrido con Fine-Tuning y Orquestación Inteligente.

# Tipo de Modelo de IA Seleccionado:

Se propone una solución híbrida que combina un Modelo de Lenguaje Grande (LLM) especializado en conversación y sometido a un proceso de fine-tuning, con un sistema tradicional basado en reglas y llamadas directas a APIs para las consultas transaccionales.

# Arquitectura Propuesta:

La arquitectura se basa en un "Orquestador Inteligente" que actúa como el primer punto de contacto.

Orquestador/Clasificador de intención: al recibir una consulta, este componente inicial (un modelo de clasificación más pequeño y rápido) determina la intención del usuario.

Módulo transaccional (Reglas/API): si la intención es puramente informativa y requiere datos precisos (ej: "¿Dónde está mi pedido #12345?", "Quiero iniciar una devolución"), el orquestador dirige la consulta a un módulo que se conecta de forma segura a las bases de datos internas de EcoMarket (ERP, CRM) a través de APIs. Este módulo recupera la información exacta y la presenta al usuario.

Módulo conversacional (LLM con Fine-Tuning): si la consulta es abierta, compleja o requiere empatía (ej: "No estoy satisfecho con la calidad", "¿Qué producto me recomiendan para un regalo?", "Tengo una queja sobre un repartidor"), el orquestador la pasa al LLM ajustado.

Base de conocimiento (RAG): el LLM se apoya en una arquitectura de Generación Aumentada por Recuperación (RAG). Esto significa que antes de responder, busca en una base de datos vectorializada que contiene el catálogo de productos, las políticas de la empresa, FAQs y guías de sostenibilidad, para asegurar que sus respuestas sean siempre ajustadas a la realidad y basadas en la información de EcoMarket.

Proceso de fine-tuning: el modelo base será re-entrenado con un conjunto de datos curado de miles de interacciones de soporte pasadas de EcoMarket, previamente anonimizadas. Esto es crucial para que el LLM adopte el tono de voz, los valores y la empatía que definen a la marca.

## Justificación de la Elección:

Precisión y confiabilidad de la arquitectura híbrida: la principal ventaja es la eliminación del riesgo de "alucinaciones" para datos críticos. Para el 80% de las consultas repetitivas sobre pedidos o devoluciones, la precisión debe ser del 100%. Un LLM podría equivocarse en un número de seguimiento, pero una llamada directa a la API no. Este enfoque combina la precisión robótica para los datos y la inteligencia conversacional para el diálogo e interacción compleja con el cliente.

Costo-eficiencia: las llamadas a APIs internas son órdenes de magnitud más baratas que las inferencias de un LLM potente. Al desviar el 80% del tráfico al módulo transaccional, se logra una optimización de costos masiva, reservando el uso del LLM para cuando su capacidad generativa es realmente necesaria.

Calidad de la respuesta y alineación con la marca: el fine-tuning asegura que el LLM no solo responda correctamente, sino que lo haga como lo haría un agente de EcoMarket. Esto es fundamental para mantener la identidad de una marca centrada en valores como la sostenibilidad y la confianza.

Escalabilidad y seguridad: la arquitectura modular permite escalar cada componente de forma independiente. Además, limita el acceso del LLM a las bases de datos sensibles, mejorando la postura de seguridad al compartimentar el acceso a los datos.
