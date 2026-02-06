from .github_tool import GitHubTool
from .weather_tool import WeatherTool

class ToolRegistry:
    def __init__(self):
        self.tools = {
            "GitHubTool": GitHubTool(),
            "WeatherTool": WeatherTool()
        }
    
    def get_tool(self, tool_name: str):
        return self.tools.get(tool_name)
    
    def list_tools(self):
        return list(self.tools.keys())
