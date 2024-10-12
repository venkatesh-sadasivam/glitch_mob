class ExternalIntegration:
    def connect_to_api(self, agent, api_endpoint):
        # Connect an agent to an external API
        print(f"Agent {agent.name} connected to API at {api_endpoint}")

    def fetch_data(self, agent, data_source):
        # Fetch data from an external source
        print(f"Agent {agent.name} fetching data from {data_source}")