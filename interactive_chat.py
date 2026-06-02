import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Configura tu clave de API de OpenAI usando la variable de entorno
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(api_key=api_key, model="gpt-4.0-mini", temperature=0.7)

# Define un prompt para el modelo
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="Eres un asistente útil y preciso."),
    MessagesPlaceholder(variable_name="chat_history"),
    ( "human", "{input}" )
])

#crear cadena de conversación

chain = prompt | llm

def ejecutar_conversacion():
    print("Bienvenido al asistente de inteligencia artificial. Escribe 'salir' para terminar la conversación.")

    chat_history = []
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("¡Hasta luego!")
            break

        response = chain.invoke({
        "input": user_input, 
        "chat_history": chat_history
        })

        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=response.content))


        print(f"Asistente: {response.content}")

if __name__ == "__main__": 
    ejecutar_conversacion()
