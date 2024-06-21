from crewai import Agent
from tools import scrape_tool
import os
from dotenv import load_dotenv
load_dotenv("creds.env")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

## Create a senior web scrapper
web_scrapper=Agent(
    role='Web scrapper for ecommerce sites',
    goal='Get the relevant flower products for the category {topic} from the provided website',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in scraping the relevant data from the provided web sites" 
    ),
    tools=[scrape_tool],
    allow_delegation=True
)

## creating a senior Data Analyst agent with scrape_tool
data_analyst=Agent(
    role='Seniour Data Analyst',
    goal='Analyse the product data and Give some insights out of it',
    verbose=True,
    memory=True,
    backstory=(
        "Analyze the product data and extract meaningful insights. Identify trends, patterns, and anomalies to provide actionable recommendations for improvement and strategy development"
    ),
    tools=[scrape_tool],
    allow_delegation=False

)