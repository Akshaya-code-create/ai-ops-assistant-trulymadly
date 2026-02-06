from typing import List
from llm.models import Plan, ExecutionResult, Step
from tools import ToolRegistry

class ExecutorAgent:
    def __init__(self):
        self.tool_registry = ToolRegistry()
    
    def execute_plan(self, plan: Plan) -> List[ExecutionResult]:
        print(f"\n[EXECUTOR] Executing {len(plan.steps)} steps")
        results = []
        
        for step in plan.steps:
            print(f"\n[EXECUTOR] Step {step.step_number}: {step.description}")
            result = self.execute_step(step)
            results.append(result)
            
            if not result.success:
                print(f"[EXECUTOR]  Step {step.step_number} failed")
        
        return results
    
    def execute_step(self, step: Step) -> ExecutionResult:
        tool = self.tool_registry.get_tool(step.tool_name)
        
        if not tool:
            return ExecutionResult(
                step_number=step.step_number,
                tool_name=step.tool_name,
                success=False,
                error=f"Tool {step.tool_name} not found"
            )
        
        try:
            result = tool.execute_with_retry(**step.parameters)
            return ExecutionResult(
                step_number=step.step_number,
                tool_name=step.tool_name,
                success=result["success"],
                data=result["data"],
                error=result["error"]
            )
        except Exception as e:
            return ExecutionResult(
                step_number=step.step_number,
                tool_name=step.tool_name,
                success=False,
                error=str(e)
            )
