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
    """Detailed technical and business feasibility analysis for implementing a product"""
    name: str = Field(description="Product or idea name")
    implementation_approach: str = Field(description="How to implement using AI stack (Python, LLM, Langchain, CrewAI, etc.)")
    required_technologies: List[str] = Field(description="List of required technologies, frameworks, and APIs")
    complexity_level: str = Field(description="Implementation complexity: Easy, Medium, or Hard")
    mvp_time_estimate: str = Field(description="Estimated time to build MVP (e.g., '4-6 weeks', '2-3 months')")
    monthly_costs: str = Field(description="Estimated monthly infrastructure costs breakdown (APIs, hosting, databases, services)")
    team_structure: str = Field(description="Required team structure (e.g., 'Solo developer', 'Developer + Designer', 'Full team')")
    solo_developer_feasible: bool = Field(description="Whether a solo developer can realistically build and maintain this")
    solo_developer_assessment: str = Field(description="Detailed assessment of solo developer viability - challenges, time commitment, skills needed")
    technical_challenges: str = Field(description="Key technical challenges and how to overcome them")
    architecture_overview: str = Field(description="High-level architecture and design recommendations")
    innovation_score: int = Field(description="Innovation potential and market fit score from 1-10")
    innovation_justification: str = Field(description="Justification for the innovation score")


class ProductFeasibilityList(BaseModel):
    """List of feasibility analyses for all products"""
    analyses: List[ProductFeasibilityAnalysis] = Field(description="Comprehensive feasibility analysis for each product")


class ProductDecision(BaseModel):
    """Final product selection decision with implementation roadmap"""
    chosen_product: str = Field(description="Name of the selected product/idea")
    selection_rationale: str = Field(description="Why this product was chosen over others")
    solo_developer_verdict: bool = Field(description="YES (True) or NO (False) - can a solo developer build this?")
    solo_developer_justification: str = Field(description="Detailed justification for the solo developer verdict")
    mvp_timeline: str = Field(description="Total estimated time to MVP")
    monthly_running_costs: str = Field(description="Estimated monthly costs after launch")
    tech_stack: List[str] = Field(description="Recommended technology stack")
    implementation_phases: List[str] = Field(description="Phase-by-phase or week-by-week implementation roadmap")
    expected_challenges: List[str] = Field(description="Expected challenges and how to overcome them alone")
    required_skills: List[str] = Field(description="Skills needed to build this product")
    skills_to_learn: List[str] = Field(description="Skills you may need to learn")
    rejected_products: List[str] = Field(description="Products not selected and brief reason why")


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
            output_pydantic=ProductDecision,
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
