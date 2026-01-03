from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator, current_time, http_request, file_read

SYSTEM_PROMPT = """You are a log analysis agent.
You are execelent in reading and understanding the log files(.log /var/www/ /system log etc) 
You can deduce results in short and crisp manner.
You are helpful and use a devops mindset in analysts and root cause analysis.
You wouldn't hall and suggest new changes.
You will not annage in any produciotn actions but suggest changes and ideas to engineers.

"""

ollama_model = OllamaModel(
    host = "127.0.0.1:11434",
    model_id ="llama3.2"
)

agent = Agent(
    system_prompt= SYSTEM_PROMPT,
    model=ollama_model,
    tools=[file_read])
#agent("Can you read the file that is present in this direcory app.log")
agent("Detect how many times INFO , WARNNING , ERROR occures and returns the count only for /app.log  directory ")
