from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
import os

# Usa la variable de entorno OPENAI_API_KEY en lugar de hardcodear la clave
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(
    api_key=api_key,
    model="gpt-3.5-turbo",
    temperature=0.7
)
# Carga las herramientas necesarias para el agente, en este caso, la herramienta de matemáticas
tools = load_tools(["llm-math"], llm=llm)

# Inicializa el agente con los tipos de herramientas y el modelo de lenguaje
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True #muestra las desiciones del agente en la consola
    )
# Ejecuta el agente con una pregunta matemática
respuesta = agent.run("¿Cuánto es 25 por 4?")
print(respuesta)
