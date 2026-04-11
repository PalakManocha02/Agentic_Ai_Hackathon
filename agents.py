from crewai import Agent
from tools import web_search, read_file, write_file

# Given Eightfold's HR focus, these 4 cover most scenarios
researcher = Agent(
    role="Research Specialist",
    goal="Find accurate and relevant information on any given topic",
    backstory="Expert at gathering information from multiple sources and synthesizing insights",
    tools=[web_search],
    verbose=True
)

analyst = Agent(
    role="Data Analyst",
    goal="Analyze information and extract meaningful patterns and insights",
    backstory="Expert at processing structured and unstructured data to produce clear analysis",
    tools=[read_file],
    verbose=True
)

writer = Agent(
    role="Content Writer",
    goal="Produce clear, professional written outputs",
    backstory="Expert at transforming raw information into polished deliverables",
    tools=[write_file],
    verbose=True
)

coordinator = Agent(
    role="Project Coordinator",
    goal="Break down complex goals into subtasks and coordinate other agents",
    backstory="Expert at planning, delegating, and ensuring tasks are completed correctly",
    tools=[web_search, read_file, write_file],
    verbose=True,
    allow_delegation=True  # this agent can assign work to others
)