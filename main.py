from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import OpenAI
from langchain_anthropic import Anthropic
from langchain_core.prompts import ChatPromoptTemplate
from langchain_core.output_parsers import pydantic0output_parser
from langchain.agents import create_tool_calling_agent, agentExecutor
from tools import search_tool, wiki_tool, save_tool

# Load environment variables from .env file
load_dotenv()


# Define a Pydantic model for the input data
class InputData(BaseModel):
    topic: str
    summary: str
    source: list[str]
    tools_used: list[str]


# Create an LLM instance using the OpenAI model
llm = OpenAI(model="gpt-3.5-turbo")
#llm2 = Anthropic(model="claude-2")

# Create variable for the output parser
parser = pydantic0output_parser(pydantic_object = ResearchResponse)

# Create a prompt template

prompt = ChatPromoptTemplate.from_messages([
    ("system", """You are a research assistant that will help generate a research paper.
    Answer the user query and use necessary tools.
    Wrap the output in this format and provide no other text\n{format_instructions}."""),
    ("placeholder","{chat_history}"),
    ("human", "{query}")
    ("placeholder", "{agent_scratchpad}"),
    
]
).partial(format_instructions = parser.get_format_instructions())

# Create the agent and the agent executor
tools = [search_tool,wiki_tool, save_tool] # add more tools to this list if you want to use more tools in the agent
agent = create_tool_calling_agent(
    llm=llm, 
    tools=tools, 
    prompt=prompt, 
    output_parser=parser
    )
agent_executor = agentExecutor(agent=agent, tools=tools, verbose = True)

# Example of how to call the agent executor
raw_response = agent_executor.invoke({"query": "What is the capital of France?", "name": "Santiago"})
print(raw_response)

#if you do like a input for you, you can do it like this:
# user_input = input("What do you want to research? ")
#and raw_response = agent_executor.invoke({"query": user_input, "name": "Santiago"})

# At the moment, the agent generates a response but it is not in the format of the Pydantic model.
# We need to parse the response to get the data in the format of the Pydantic model.

#Create a variable to store the parsed response
try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response.topic)
except Exception as e:
    print("Error parsing response:", e, "Raw response:", raw_response)
