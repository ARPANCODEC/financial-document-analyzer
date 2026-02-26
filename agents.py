from crewai import Agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()

from app.tools import read_financial_document


# Define LLM properly
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# Create agent
financial_analyst = Agent(

    role="Financial Analyst",

    goal="Analyze financial documents",

    verbose=True,

    backstory="Expert financial analyst",

    tools=[read_financial_document],

    llm=llm

)