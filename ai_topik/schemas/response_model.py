from typing import List, Optional

from pydantic import BaseModel, Field

class PreInput(BaseModel):
    level: str = Field(..., description="TOPIK Level(e.g., '초급')")
    type: str = Field(..., description="TOPIK type (e.g., '읽기', '문법 등')")
    subtype: Optional[str] = Field(None, description="TOPIK subtype (optional)")
    topic: Optional[str] = Field(None, description="Specific topic for the question (optional)")