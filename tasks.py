from crewai import Task
from tools import scrape_tool
from agents import web_scrapper,data_analyst

## web scraping task
web_scraping_task = Task( 
    description=(
    "Identify {topic} flower category related products"
    "scrape the provided category products data"
  ),
  expected_output="Product table which contains product name, price range, product image, product offers if any, product sizes along with their price and Shipping details",
  tools=[scrape_tool],
  agent=web_scrapper
)

# data analyst task
data_analyst_task = Task(
  description=(
    "get the {topic} category data and give insights out of it "
  ),
  expected_output='Analyze the product data and extract meaningful insights. Identify trends, patterns, and anomalies to provide actionable recommendations for improvement and strategy development',
  tools=[scrape_tool],
  agent=data_analyst,
  async_execution=False,
  output_file='Flower_output_data.json'  # Example of output customization
)