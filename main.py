from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent
from llm.models import FinalOutput
import uvicorn

app = FastAPI(title="AI Operations Assistant", version="1.0.0")

class TaskRequest(BaseModel):
    task: str

class AIOperationsAssistant:
    def __init__(self):
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.verifier = VerifierAgent()
    
    def process_task(self, task: str) -> FinalOutput:
        print(f"\n{'='*60}")
        print(f" PROCESSING TASK: {task}")
        print(f"{'='*60}")
        
        # 1. PLAN
        plan = self.planner.create_plan(task)
        
        # 2. EXECUTE
        results = self.executor.execute_plan(plan)
        
        # 3. VERIFY
        verification = self.verifier.verify_results(task, results)
        
        # 4. FINAL OUTPUT
        final_output = self.verifier.create_final_output(task, results, verification)
        
        print(f"\n{'='*60}")
        print(f"✅ TASK COMPLETED: {final_output.status}")
        print(f"{'='*60}")
        
        return final_output

assistant = AIOperationsAssistant()

@app.post("/process", response_model=FinalOutput)
async def process_task(request: TaskRequest):
    try:
        result = assistant.process_task(request.task)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/")
async def root():
    return {"message": "AI Operations Assistant is running!", "docs": "/docs"}

if __name__ == "__main__":
    print(" Starting AI Operations Assistant...")
    print(" API Docs: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
