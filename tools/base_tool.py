from abc import ABC, abstractmethod
from typing import Dict, Any
import time
import random

class BaseTool(ABC):
    def __init__(self, name: str):
        self.name = name
        self.max_retries = 3
    
    @abstractmethod
    def execute(self, **kwargs) -> Dict[str, Any]:
        pass
    
    def execute_with_retry(self, **kwargs) -> Dict[str, Any]:
        base_delay = 1
        for attempt in range(self.max_retries):
            try:
                result = self.execute(**kwargs)
                return {'success': True, 'data': result, 'error': None}
            except Exception as e:
                if attempt < self.max_retries - 1:
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                    time.sleep(delay)
                else:
                    return {'success': False, 'data': None, 'error': str(e)}
