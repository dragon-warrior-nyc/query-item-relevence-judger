from google.adk import Agent
from google.adk.tools import url_context
from . import prompt

item_info_extractor_agent = Agent(
    model="gemini-3-flash-preview",
    name="item_info_extractor_agent",
    description="An agent that takes both a product URL and a search query as input and extracts structured product information from the URL to support relevancy evaluation for the given search query.",
    instruction=prompt.ITEM_INFO_EXTRACTOR_PROMPT,
    tools=[url_context]
)

# root_agent = item_info_extractor_agent
