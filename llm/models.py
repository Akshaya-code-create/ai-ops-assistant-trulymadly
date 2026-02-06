from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class Step(BaseModel):
    step_number: int
    description: str
    tool_name: str
    parameters: Dict[str, Any] = {}

class Plan(BaseModel):
    task: str
    reasoning: str
    steps: List[Step] = []
    expected_output_format: str = 'json'

class ExecutionResult(BaseModel):
    step_number: int
    tool_name: str
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

class VerificationResult(BaseModel):
    is_complete: bool = True
    is_correct: bool = True
    missing_items: List[str] = []
    feedback: str = ''
    retry_needed: bool = False

class FinalOutput(BaseModel):
    task: str
    status: str
    results: List[ExecutionResult] = []
    summary: str = ''
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
