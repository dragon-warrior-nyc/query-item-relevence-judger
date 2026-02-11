from google.adk import Agent
from . import prompt

query_intent_extractor_agent = Agent(
    model="gemini-3-flash-preview",
    name="query_intent_extractor_agent",
    description="Agent to extract the user intent behind e-commerce search queries.",
    instruction=prompt.QUERY_INTENT_EXTRACTOR_PROMPT
)

root_agent = query_intent_extractor_agent