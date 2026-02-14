from pydantic import BaseModel, Field
from typing import List, Optional

class EmailAnalysis(BaseModel):
    intent: str = Field(description="The primary category: URGENT, SCHEDULING, INFORMATION, or SOCIAL")
    summary: str = Field(description="A concise 2-sentence summary of the email")
    action_items: List[str] = Field(description="List of specific tasks requested in the email")
    tone: str = Field(description="The emotional tone: Professional, Frustrated, Friendly, or Formal")