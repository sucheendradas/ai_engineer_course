
import os
import asyncio
from dotenv import load_dotenv


from openai import OpenAI
from agents import Agent, Runner, trace

load_dotenv(override=True)  # Loads the .env file

# Make an agent with name, instructions, model

async def main():
    agent = Agent(name="Jokester", instructions="You are a joke teller", model="gpt-4.1-nano")

    # Run the joke with Runner.run(agent, prompt) then print final_output   

    # workflow - "Telling a joke"
    # model    - "gpt-4.1-nano"
    # flow     - "jokester"
    # instructions   - "You are a joke teller" (System Instructions)
    # input (user)   - "Tell a joke about Autonomous AI Agents"
    # output (final) - result.final_output


    with trace("Telling a joke"):
        result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
        print(result.final_output)

asyncio.run(main())