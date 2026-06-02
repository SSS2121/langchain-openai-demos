# math_agent_demo (Lanchain_3.py)

Resumen

Demo que inicializa un agente de LangChain con la herramienta `llm-math` para resolver operaciones matemáticas.

Tecnologías

- Python
- langchain
- langchain-community (herramientas de agente)
- openai

Requisitos

- Python 3.9+
- Variable de entorno `OPENAI_API_KEY`

Instalación

```bash
python -m venv .env
.env\Scripts\activate
pip install -r requirements.txt
```

Uso

```bash
set OPENAI_API_KEY=tu_clave
python Lanchain_3.py
```

Notas

- El script usa `OPENAI_API_KEY` para inicializar el cliente.
- Puedes renombrar el archivo a `math_agent_demo.py` para mayor claridad en tu portafolio.
- Añade capturas de la ejecución para demostrar el flujo del agente.
