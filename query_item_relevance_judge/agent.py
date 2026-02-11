from google.adk.agents import Agent
from google.adk.tools import AgentTool
from google.genai.types import GenerateContentConfig
from . import prompt

from .sub_agents.item_info_extractor import item_info_extractor_agent
from .sub_agents.query_intent_extractor import query_intent_extractor_agent 

query_item_relevance_judge_agent = Agent(
    model="gemini-3-pro-preview",
    name="query_item_relevance_judger_agent",
    description="Judges relevance between search query and product with reasoning",
    instruction=prompt.QUERY_ITEM_RELEVANCE_JUDGE_PROMPT,
    # generate_content_config=GenerateContentConfig(thinking_config={"thinking_level": "high"}),
    tools=[
        AgentTool(agent=query_intent_extractor_agent),
        AgentTool(agent=item_info_extractor_agent)
    ]
)

root_agent = query_item_relevance_judge_agent

