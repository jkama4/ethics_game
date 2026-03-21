from pydantic import BaseModel
from typing import List, Dict

class ChartData(BaseModel):
    title: str
    chart_type: str
    data: Dict
    y_label: str = ""

class Scorecard(BaseModel):
    issue_descriptions: List[str]

class Scenario(BaseModel):
    setting: str
    system_prompt: str
    scorecard: Scorecard
    charts: List[ChartData] = []