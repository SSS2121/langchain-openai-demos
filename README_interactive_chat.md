# interactive_chat (Langchain_2.py)

Resumen

Chat por línea de comandos que mantiene un historial de la conversación.

Tecnologías

- Python
- langchain
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
python Langchain_2.py
```

Comandos

- Escribe para enviar un mensaje; escribe `salir` para terminar.

Notas

- Verifica que tu paquete `langchain_openai` esté instalado y actualizado.
- Considera añadir límites de tokens y manejo de errores de red.
