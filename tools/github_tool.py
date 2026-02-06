import requests
from typing import Dict, Any, List
from .base_tool import BaseTool
from config.settings import settings

class GitHubTool(BaseTool):
    def __init__(self):
        super().__init__('GitHubTool')
        self.base_url = 'https://api.github.com'
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'token {settings.github_token}'
        }
    
    def execute(self, action: str = 'search_repositories', **kwargs) -> Dict[str, Any]:
        if action == 'search_repositories':
            return self.search_repositories(kwargs.get('query', ''))
        raise ValueError(f'Unknown action: {action}')
    
    def search_repositories(self, query: str, limit: int = 5) -> Dict[str, Any]:
        url = f'{self.base_url}/search/repositories'
        params = {'q': query, 'sort': 'stars', 'order': 'desc', 'per_page': limit}
        response = requests.get(url, headers=self.headers, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        repos = []
        for item in data.get('items', [])[:limit]:
            repos.append({
                'name': item['name'],
                'full_name': item['full_name'],
                'description': item.get('description', 'No description'),
                'stars': item['stargazers_count'],
                'language': item.get('language', 'Unknown'),
                'url': item['html_url']
            })
        return {'total_count': data.get('total_count', 0), 'repositories': repos}
