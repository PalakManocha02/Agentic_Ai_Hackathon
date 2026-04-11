from crewai import Task
from agents import researcher, analyst, writer

def make_research_task(topic: str) -> Task:
    return Task(
        description=f"Research the following thoroughly: {topic}. Provide a detailed summary.",
        expected_output="A comprehensive research summary with key findings",
        agent=researcher
    )

def make_analysis_task(data: str) -> Task:
    return Task(
        description=f"Analyze this data and extract insights: {data}",
        expected_output="A structured analysis with clear conclusions",
        agent=analyst
    )

def make_writing_task(instructions: str) -> Task:
    return Task(
        description=f"Write the following: {instructions}",
        expected_output="A polished, professional written output",
        agent=writer
    )