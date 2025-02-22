from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import json
import finnhub

load_dotenv()
# Initialize finhub_client
finnhub_client = finnhub.Client(api_key="ctuo7lhr01qg98tdn5qgctuo7lhr01qg98tdn5r0")

web_agent = Agent(
    name="Web Agent",
    model=Gemini(id="gemini-1.5-flash"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

finance_agent1 = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Gemini(id="gemini-1.5-flash"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True,
                         historical_prices=True, technical_indicators=True)],
    show_tool_calls=True,
    markdown=True
)

finance_agent2 = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Gemini(id="gemini-1.5-flash"),
    tools=[finnhub_client.general_news('general', min_id=0)],
    show_tool_calls=True,
    markdown=True
)


finance_agent3 = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Gemini(id="gemini-1.5-flash"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True,
                         historical_prices=True, technical_indicators=True)],
    show_tool_calls=True,
    markdown=True
)


finance_agent4 = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Gemini(id="gemini-1.5-flash"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True,
                         historical_prices=True, technical_indicators=True)],
    show_tool_calls=True,
    markdown=True
)


def print_resp():
    # print response of all the agents
    return json.dumps({
        "web_agent": web_agent.print_response("Summarize analyst recommendations and share the latest news for Nvidia and Tesla", stream=True),
        "finance_agent": finance_agent.print_response("Summarize analyst recommendations and share the latest news for Nvidia and Tesla", stream=True)
    })

# agents_team_lead.print_response("Summarize analyst recommendations and share the latest news for Nvidia and Tesla", stream=True)