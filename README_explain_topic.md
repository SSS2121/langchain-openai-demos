# explain_topic (Explain_topic.py)

Resumen

Script sencillo que usa LangChain + un LLM de OpenAI para generar una explicación breve sobre un tema.

Tecnologías

- Python
- langchain
- openai

Requisitos

- Python 3.9+
- Variable de entorno `OPENAI_API_KEY` con tu clave de OpenAI

Instalación

```bash
python -m venv .env
.env\Scripts\activate
pip install -r requirements.txt
```

Uso

```bash
set OPENAI_API_KEY=tu_clave
python Explain_topic.py
```

Ejemplo de salida

- Entrada: "la inteligencia artificial"
- Salida: breve párrafo explicando el tema

Mejoras posibles

- Añadir argumentos CLI para pasar el tema desde la línea de comandos
- Guardar respuestas en un archivo JSON
