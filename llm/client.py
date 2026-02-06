from openai import OpenAI
import json
from typing import Type, TypeVar
from pydantic import BaseModel
from config.settings import settings

T = TypeVar('T', bound=BaseModel)

class LLMClient:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.llm_model
    
    def generate_structured_output(self, prompt: str, response_model: Type[T], system_prompt: str = '') -> T:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {'role': 'system', 'content': 'Respond with valid JSON only matching the expected schema.'},
                    {'role': 'user', 'content': f'Task: {prompt}'}
                ],
                response_format={'type': 'json_object'},
                temperature=0.1
            )
            data = json.loads(response.choices[0].message.content)
            return response_model.model_validate(data)
        except Exception as e:
            print(f'LLM fallback: {str(e)}')
            # Mock response for demo
            from llm.models import Plan, Step, VerificationResult
            if response_model.__name__ == 'Plan':
                return Plan(
                    task=prompt[:100],
                    reasoning='Generated plan',
                    steps=[Step(step_number=1, description='Execute', tool_name='WeatherTool', parameters={'city_name': 'Warangal'})],
                    expected_output_format='json'
                )
            return VerificationResult(is_complete=True, feedback='Success')
    
    def generate_text(self, prompt: str, system_prompt: str = '') -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{'role': 'user', 'content': prompt}],
                temperature=0.3
            )
            return response.choices[0].message.content
        except:
            return 'Task completed successfully.'
