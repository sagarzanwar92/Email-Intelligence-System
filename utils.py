from pydantic import BaseModel, Field
from typing import List, Optional

class EmailAnalysis(BaseModel):
    # Keep Intent and Summary mandatory (the core)
    intent: str = Field(description="URGENT, SCHEDULING, or CAN IGNORE")
    summary: str = Field(description="A concise 2-sentence summary")
    
    # Make the specific extractions optional
    action_items: List[str] = Field(default_factory=list, description="List of tasks")
    
    # Use Optional for things that might not exist in the email
    sender_name: Optional[str] = Field(default="Unknown", description="Name of sender")
    key_question: Optional[str] = Field(default="None", description="Primary request")
    deadline: Optional[str] = Field(default="None", description="Mentioned date/time")