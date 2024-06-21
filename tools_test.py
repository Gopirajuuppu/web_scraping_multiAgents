from crewai_tools import ScrapeWebsiteTool

# Initialize the tool with the website URL, so the agent can only scrap the content of the specified website
tool = ScrapeWebsiteTool(website_url='https://www.1800flowers.com/')

# Extract the text from the site
text = tool.run()
print(text)