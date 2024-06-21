from crewai_tools import ScrapeWebsiteTool
# To enable scrapping any website it finds during it's execution
scrape_tool = ScrapeWebsiteTool(website_url='https://www.teleflora.com')