# explain_topic: genera una explicación breve sobre un tema usando LangChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

import os
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(api_key=api_key, model="gpt-4.0-mini", temperature=0.7 )

template = ChatPromptTemplate(
    input_variables=["question"],
    template="Explica de manera breve el siguiente tema {question}?"
)

def explicar_tema(tema):
    prompt = template.format(question=tema)
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    tema = "la inteligencia artificial"
    respuesta = explicar_tema(tema)
    print(respuesta)
