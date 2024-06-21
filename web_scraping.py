print("--------- Welcome to Web Scarping with Crew AI Technology  ------------")

#importing libraries
from crewai import Crew, Process
from agents import web_scrapper, data_analyst
from tasks import web_scraping_task, data_analyst_task
scraping_crew = Crew(
    agents = [web_scrapper,data_analyst],
    tasks=[web_scraping_task,data_analyst_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    share_crew=True
)

## start the task execution process with enhanced feedback
result=scraping_crew.kickoff(inputs={'topic':'Birthday'})
print(result)