class AgentRegistry:
    def __init__(self):
        self._agents = {}

    def register(self, name: str, capabilities: list, handler):
        self._agents[name] = {
            "capabilities": capabilities,
            "handler": handler
        }

    def get_agent(self, name: str):
        return self._agents.get(name)

    def find_by_capability(self, capability: str):
        return {
            name: agent
            for name, agent in self._agents.items()
            if capability in agent["capabilities"]
        }

    def list_agents(self):
        return self._agents