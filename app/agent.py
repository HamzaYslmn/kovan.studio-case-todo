import os
from typing import Union, Type, Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

load_dotenv(".env")

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY")).aio

async def response_chat(
    message: str,
    instructions: str = "",
    model: str = "gemini-flash-lite-latest",
    struct: Union[Type[BaseModel], None] = None,
):
    contents = [types.Content(role="user", parts=[types.Part.from_text(text=message)])]
    
    schema = struct.model_json_schema() if struct else None
    
    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=-1),
        system_instruction=[types.Part.from_text(text=instructions)] if instructions else None,
        response_mime_type="application/json" if struct else None,
        response_schema=schema,
    )

    async with client:
        response = await client.models.generate_content(
            model=model,
            contents=contents,
            config=config,
        )
        yield response.text, None


class Agent(BaseModel):
    score: int = Field(..., ge=0, le=100, description="The candidate's score")
    strong_points: str = Field(..., description="Candidate's strong points")
    risks: str = Field(..., description="Candidate's risks")
    summary_of_reason: str = Field(..., description="Summarize why the candidate was chosen or not")
    suggestion: Literal["evet", "hayir", "belki"] = Field(..., description="Suggestion to hire or not")


INSTRUCTIONS = "You are an expert career advisor. Analyze the candidate's profile:\n{job_details}"

async def analyze_cv(cv_content: str) -> str:
    with open("ilan.md", encoding="utf-8") as f:
        job_details = f.read()
    
    instructions = INSTRUCTIONS.format(job_details=job_details)
    result = ""
    async for text, _ in response_chat(cv_content, instructions, struct=Agent):
        result += text
    return result


if __name__ == "__main__":
    import asyncio

    async def test():
        with open("cv.md", encoding="utf-8") as f:
            cv = f.read()
        print(await analyze_cv(cv))

    asyncio.run(test())