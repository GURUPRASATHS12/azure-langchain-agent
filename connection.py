import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# Configure LLM
llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    deployment_name=os.getenv("OPENAI_DEPLOYMENT_NAME"),
    temperature=0.3
)

# Human query
query = input("Enter your question:")
human_message = HumanMessage(content=query)

# Generate response
# `AzureChatOpenAI.generate` expects a list of message lists: [[HumanMessage, ...]]
response = llm.generate([[human_message]])
# Extract the content from the first generation
reply = response.generations[0][0].message.content
print("Query:", query)
print("Response:", reply)

