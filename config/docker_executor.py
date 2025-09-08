from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constant import WORK_DIR, TIMEOUT

def get_docker_executor():
    """
    Function to get the Docker code executor.
    This executor is responsible for running code in a Docker container.
    """
    docker_executor = DockerCommandLineCodeExecutor(
        work_dir=WORK_DIR,
        timeout=TIMEOUT
    )

    return docker_executor
   