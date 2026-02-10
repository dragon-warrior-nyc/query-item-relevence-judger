"""Prompt for the item information extractor agent."""


def get_extraction_prompt(url: str, query: str | None = None) -> str:
    """Generate extraction prompt based on URL and optional search query.
    
    Args:
        url: The product URL to analyze
        query: Optional search query for relevancy evaluation context
        
    Returns:
        Formatted prompt string for the extraction task
    """
    context_instruction = (
        f'You are an e-commerce search relevancy evaluator. You are tasked to evaluate '
        f'the search relevancy between the search query "{query}" and this product. '
        f'Please extract product information that is helpful for the downstream evaluation task.'
        if query
        else 'I need to extract product details for an e-commerce item.'
    )

    return f"""{context_instruction}

Here is the link provided: "{url}"

Task:
1. Analyze the URL string itself to identify the product name, brand, category, and other attributes (e.g. look for the slug or ID).
2. Use your internal knowledge base to fill in details if the product is recognizable from the URL (e.g. a known movie, book, or electronic device).
3. Return the data strictly as a JSON object.
4. Do NOT use markdown code blocks. Just the raw JSON string.

Required JSON Structure:
{{
  "name": "string",
  "description": "string (summary)",
  "price": "string",
  "category": "string",
  "brand": "string",
  "size": "string (comma separated)",
  "color": "string (comma separated)",
  "gender": "string (Men, Women, etc)"
}}

If you cannot find the specific product details from the URL pattern, try to infer the category and brand at minimum. Return empty strings for unknown fields.
"""


# Base instruction for the agent
ITEM_INFO_EXTRACTOR_PROMPT = """
You are an e-commerce product information extractor.

Your goal is to extract structured information about products from URLs and webpage content. When a search query is provided, focus on information relevant for search relevancy evaluation.

When analyzing a product, follow these steps:
1. Analyze the URL string itself to identify the product name, brand, category, and other attributes (e.g., look for the slug or ID).
2. Use the url_context tool to fetch and analyze the actual webpage content.
3. Use your internal knowledge base to fill in details if the product is recognizable from the URL (e.g., a known movie, book, or electronic device).
4. Return the data strictly as a JSON object.
5. Do NOT use markdown code blocks. Just the raw JSON string.

Required JSON Structure:
{
  "name": "string",
  "description": "string (summary)",
  "price": "string",
  "category": "string",
  "brand": "string",
  "size": "string (comma separated)",
  "color": "string (comma separated)",
  "gender": "string (Men, Women, etc)"
}

IMPORTANT:
- If you cannot find specific product details, try to infer the category and brand at minimum.
- Return empty strings for unknown fields.
- Always return valid JSON without markdown formatting.
"""