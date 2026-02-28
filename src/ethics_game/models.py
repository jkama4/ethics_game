from pydantic import BaseModel

from typing import List

class Scorecard(BaseModel):
    issue_descriptions: List[str]


class Scenario(BaseModel):
    setting: str
    system_prompt: str
    scorecard: Scorecard
