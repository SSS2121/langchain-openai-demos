from langchain_community_tools import wikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime
# Create a function to save the output of the agent in a txt file. This can be useful for later use
# or for keeping a record of the research done by the agent.
def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}"
    if filename is None:
        filename = f"research_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(formatted_text)
    return f"Data successfully saved to {filename}"
# Create the save tool using the save_to_txt function:
save_tool = Tool(
    name = "save_to_txt",
    func = save_to_txt,
    description = "Save the output of the agent in a txt file"
)
# Create the search tool using the DuckDuckGoSearchRun class
search = DuckDuckGoSearchRun()
# Create tool instance for the search tool:
search_tool = Tool(
    name = "search",
    func = search.run,
    description = "Search the web for information"
)
# Create API wrapper for Wikipedia; this will be used in the Wikipedia tool:
wikipedia_api = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max = 100)
wiki_tool = wikipediaQueryRun(wikipedia_api)