from autogen_agentchat.agents import CodeExecutorAgent  
from config.docker_executor import get_docker_executor

docker=get_docker_executor()

def get_code_executor_agent():
    """
    Function to get the code executor agent.
    This Agent is responsible for executing code.
    It will work with ProblemSolverAgent to execute code.
    """

    code_excecutor_agent = CodeExecutorAgent(
        name="CodeExecutorAgent",
        code_executor=docker)

    return code_excecutor_agent,docker