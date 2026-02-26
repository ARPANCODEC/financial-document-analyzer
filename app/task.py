from crewai import Task
from app.agents import financial_analyst


analyze_financial_document = Task(

description="""
Analyze financial document:

File:
{file_path}

Query:
{query}

Give:

1 Summary
2 Insights
3 Risks
""",

expected_output="Financial report",

agent=financial_analyst
)