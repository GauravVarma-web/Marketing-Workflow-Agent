# Marketing Workflow Agent

This AI agent demonstrates automation of multi-step marketing workflows using the ReAct (Reasoning + Acting) pattern. The agent can analyze marketing campaign data, generate content based on insights, and schedule content for publishing.

## Features

- **Campaign Analysis**: Analyze marketing campaign data to extract metrics, insights, and recommendations
- **Content Generation**: Create marketing content based on topics, audience, and tone preferences
- **Content Scheduling**: Schedule content for publication across various platforms
- **Workflow Automation**: Chain multiple marketing tasks into end-to-end workflows

## Project Structure

```
Marketing-Workflow-Agent/
├── actions.py        # Implementation of marketing actions/tools
├── json_helpers.py   # Helper functions for JSON manipulation
├── main.py           # Main execution file
├── prompts.py        # System prompts for the agent
├── .env              # Environment variables
└── README.md         # Documentation
```

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Setup

1. Clone this repository:
```bash
git clone https://github.com/YourUsername/Marketing-Workflow-Agent.git
cd Marketing-Workflow-Agent
```

2. Install the required packages:
```bash
pip install openai python-dotenv
```

3. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the agent with:

```bash
python main.py
```

### Example Workflows

The agent can execute various marketing workflows such as:

#### Content Creation Workflow
1. Research trending topics in a specific industry
2. Generate content ideas based on research
3. Create a content piece optimized for target audience
4. Schedule content for publication

#### Campaign Analysis Workflow
1. Import campaign data
2. Analyze performance metrics
3. Generate insights and recommendations
4. Create a summary report

#### Content Calendar Workflow
1. Analyze content gaps
2. Generate content ideas for different platforms
3. Create a content calendar
4. Schedule content creation tasks

## How It Works

The Marketing Workflow Agent uses a three-step process:

1. **Reasoning**: The agent analyzes the task and determines the appropriate sequence of actions
2. **Acting**: The agent executes specialized marketing functions to complete each step
3. **Reflection**: The agent evaluates the results and adjusts its approach if needed

This process allows the agent to handle complex, multi-step marketing tasks autonomously.

## Customization

- Modify the prompts in `prompts.py` to customize the agent's domain expertise
- Add new marketing actions in `actions.py` to expand functionality
- Adjust workflows in `main.py` to create custom marketing automation sequences

## Integration

This Marketing Workflow Agent is designed to be part of a larger Agent Orchestration system, where it can work alongside:

- RAG Marketing Agent (for knowledge retrieval)
- Travel Planning Agent (for event marketing)
- Analytics Agents (for deeper performance analysis)

## License

MIT

## Author

Gaurav Varma - AI-First Marketer & Self-Taught Agent Builder
