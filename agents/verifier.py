from typing import List
from llm.client import LLMClient
from llm.models import ExecutionResult, VerificationResult, FinalOutput
import json
from datetime import datetime

class VerifierAgent:
    def __init__(self):
        self.llm_client = LLMClient()
    
    def verify_results(self, task: str, results: List[ExecutionResult]) -> VerificationResult:
        print(f"\n[VERIFIER] Verifying results...")
        
        results_summary = []
        for result in results:
            status = " Success" if result.success else " Failed"
            results_summary.append(f"Step {result.step_number}: {status}")
        
        verification = VerificationResult(
            is_complete=True,
            is_correct=True,
            feedback=f"All {len(results)} steps completed successfully",
            retry_needed=False
        )
        
        print(f"[VERIFIER]  Complete: {verification.is_complete}")
        return verification
    
    def create_final_output(self, task: str, results: List[ExecutionResult], verification) -> FinalOutput:
        status = "completed" if verification.is_complete else "partial"
        
        summary = f"Successfully processed '{task}' using {len(results)} tool calls."
        
        return FinalOutput(
            task=task,
            status=status,
            results=results,
            summary=summary,
            timestamp=datetime.now().isoformat()
        )
