from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from crewai_tools import SerperDevTool


class TrendingProduct(BaseModel):
    """A trending SaaS product, application, or innovative product idea"""
    name: str = Field(description="Product or idea name")
    category: str = Field(description="Product category (e.g., AI Tool, SaaS, Developer Tool, Productivity)")
    description: str = Field(description="Brief description of the product or idea")
    why_trending: str = Field(description="Why this product/idea is trending and gaining attention")
    ai_potential: str = Field(description="How AI/LLM could be used in this product")


class TrendingProductList(BaseModel):
    """List of trending products and ideas"""
    products: List[TrendingProduct] = Field(description="List of trending products, apps, or innovative ideas")


class ProductFeasibilityAnalysis(BaseModel):
    """Detailed technical feasibility analysis for implementing a product"""
    name: str = Field(description="Product or idea name")
    implementation_approach: str = Field(description="How to implement using AI stack (Python, LLM, Langchain, CrewAI, etc.)")
    required_technologies: str = Field(description="List of required technologies, frameworks, and APIs")
    complexity_level: str = Field(description="Implementation complexity: Easy, Medium, or Hard")
    technical_challenges: str = Field(description="Key technical challenges and how to overcome them")
    architecture_overview: str = Field(description="High-level architecture and design recommendations")
    innovation_score: str = Field(description="Innovation potential and market fit (1-10 scale with justification)")


class ProductFeasibilityList(BaseModel):
    """List of feasibility analyses for all products"""
    analyses: List[ProductFeasibilityAnalysis] = Field(description="Comprehensive feasibility analysis for each product")


@CrewBase
class MyTrendingProducts():
    """MyTrendingProducts crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def trending_product_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['trending_product_finder'],
            tools=[SerperDevTool()]
        )

    @agent
    def tech_feasibility_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['tech_feasibility_researcher'],
            tools=[SerperDevTool()]
        )

    @agent
    def product_picker(self) -> Agent:
        return Agent(
            config=self.agents_config['product_picker']
        )

    @task
    def find_trending_products(self) -> Task:
        return Task(
            config=self.tasks_config['find_trending_products'],
            output_pydantic=TrendingProductList,
        )

    @task
    def research_product_feasibility(self) -> Task:
        return Task(
            config=self.tasks_config['research_product_feasibility'],
            output_pydantic=ProductFeasibilityList,
        )

    @task
    def pick_best_product(self) -> Task:
        return Task(
            config=self.tasks_config['pick_best_product'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TrendingProducts crew"""

        manager = Agent(
            config=self.agents_config['manager'],
            allow_delegation=True
        )

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            verbose=True,
            manager_agent=manager,
        )
