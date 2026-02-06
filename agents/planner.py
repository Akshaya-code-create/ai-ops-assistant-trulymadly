from llm.client import LLMClient
from llm.models import Plan

class PlannerAgent:
    def __init__(self):
        self.llm_client = LLMClient()
    
    def create_plan(self, task: str) -> Plan:
        print(f"\n[PLANNER] Creating plan for: {task}")
        
        prompt = f"""
        Create a step-by-step execution plan for this task.
        Available tools: GitHubTool (search repositories), WeatherTool (get weather)
        
        Task: {task}
        
        Return JSON plan with steps, each having: step_number, description, tool_name, parameters
        """
        
        plan = self.llm_client.generate_structured_output(
            prompt=prompt,
            response_model=Plan,
            system_prompt="You are an expert task planner. Break tasks into logical tool steps."
        )
        
        print(f"[PLANNER] Created plan with {len(plan.steps)} steps")
        return plan
