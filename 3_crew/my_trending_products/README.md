# MyTrendingProducts Crew

Welcome to the MyTrendingProducts Crew project, powered by [crewAI](https://crewai.com). This crew helps you discover trending SaaS applications, products, and innovative ideas that can be implemented using AI technologies like Python, LLM, Langchain, CrewAI, and other AI stack components.

## What This Crew Does

This crew consists of specialized AI agents that work together to:

1. **Find Trending Products** - Searches Product Hunt, Hacker News, tech blogs, and AI communities for trending SaaS products and innovative ideas
2. **Analyze Technical Feasibility** - Evaluates how each product can be implemented using modern AI stack (Python, LLM, Langchain, CrewAI, OpenAI API)
3. **Select Best Product** - Picks the best product/idea to build based on feasibility, innovation, and market potential

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
crewai install
```

### Configuration

**Add your `OPENAI_API_KEY` and `SERPER_API_KEY` into the `.env` file**

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

You can get:
- OpenAI API key from: https://platform.openai.com/api-keys
- Serper API key from: https://serper.dev/

### Customizing

- Modify `src/my_trending_products/config/agents.yaml` to define your agents
- Modify `src/my_trending_products/config/tasks.yaml` to define your tasks
- Modify `src/my_trending_products/crew.py` to add your own logic, tools and specific args
- Modify `src/my_trending_products/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
crewai run
```

Or use the package script:

```bash
uv run my_trending_products
```

This command initializes the MyTrendingProducts Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Output

The crew will generate three reports in the `output/` directory:

1. **trending_products.md** - List of trending products and ideas found
2. **feasibility_report.md** - Detailed technical analysis of each product
3. **product_decision.md** - Final decision with implementation roadmap

## Understanding Your Crew

The MyTrendingProducts Crew is composed of multiple AI agents:

1. **Trending Product Finder** - Monitors tech communities and finds trending products/ideas
2. **Tech Feasibility Researcher** - Analyzes implementation feasibility with AI stack
3. **Product Picker** - Selects the best product and creates implementation plan
4. **Manager** - Coordinates the entire research and decision process

These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve the objective of finding the best AI product to build.

## Example Use Cases

- Discover trending AI tools and SaaS products
- Find product ideas that leverage LLMs and AI
- Evaluate technical feasibility of building AI products
- Get implementation roadmaps for AI/ML projects
- Stay updated on innovative AI applications

## Support

For support, questions, or feedback regarding the MyTrendingProducts Crew or crewAI:
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's discover amazing AI products together with the power and simplicity of crewAI!
