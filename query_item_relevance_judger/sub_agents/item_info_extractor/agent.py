from google.adk import Agent
from google.adk.tools import url_context
from . import prompt

item_info_extractor_agent = Agent(
    model="gemini-3-flash-preview",
    name="item_info_extractor_agent",
    description="An agent that extracts structured product information from a given product URL to support relevancy evaluation for a given search query.",
    instruction=prompt.ITEM_INFO_EXTRACTOR_PROMPT,
    tools=[url_context]
)

root_agent = item_info_extractor_agent
