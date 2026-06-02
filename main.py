from dotenv import load_dotenv
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.output_parsers import PydanticOutputParser
from langchain.chains import LLMChain
from tools import save_to_txt

# Load environment variables from .env file
load_dotenv()


# Define a Pydantic model for the structured output
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    source: list[str]
    tools_used: list[str]


# Create an LLM instance using OpenAI via LangChain
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Create variable for the output parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "You are a research assistant that will help generate a research paper.\n"
        "Answer the user query and use necessary tools if needed.\n"
        "Wrap the output in this format and provide no other text\n{format_instructions}."
    ),
    HumanMessagePromptTemplate.from_template("{query}"),
]).partial(format_instructions=parser.get_format_instructions())

# LLM chain to run the prompt
chain = LLMChain(llm=llm, prompt=prompt)

# Example run
raw_text = chain.run({"query": "What is the capital of France?"})
print("Raw model output:\n", raw_text)

# Parse into the Pydantic model
try:
    structured = parser.parse(raw_text)
    print("Parsed topic:", structured.topic)
    # Optionally save the result to a file
    save_to_txt(structured.json(), filename="research_output_example.txt")
except Exception as e:
    print("Error parsing response:", e)
