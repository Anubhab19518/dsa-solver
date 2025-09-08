import streamlit as st
from team.dsa_team import get_create_dsa_team_and_docker
from config.docker_utils import start_docker_container, stop_docker_container
import asyncio
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage

st.title("Algogenie - Our DSA Problem Solver")
st.write("Welcome to Algogenie! This application helps you solve Data Structures and Algorithms (DSA) problems using advanced AI techniques.")

task=st.text_input("Enter your DSA problem statement:", value="Write a Python Code to add two numbers")

async def run(team,docker,task):
    try:
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(msg:=f"{message.source}: {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:= f"Stop Reason: {message.stop_reason}")
                yield msg
        print("Task Completed...")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        await stop_docker_container(docker)

if st.button("Run"):
    st.write(f"Running task: {task}")

    team, docker= get_create_dsa_team_and_docker()

    async def collect_messages():
        async for msg in run(team, docker, task):
            if isinstance(msg, str):
                if msg.startswith("user"):
                    with st.chat_message('user', avatar="🧑"):
                        st.markdown(msg)
                elif msg.startswith("DSA_ProblemSolverAgent"):
                    with st.chat_message('assistant', avatar="🤖"):
                        st.markdown(msg)
                elif msg.startswith("CodeExecutorAgent"):
                    with st.chat_message('assistant', avatar="🐳"):
                        st.markdown(msg)

            elif isinstance(msg, TaskResult):
                st.markdown(f"STOP Reason: {msg.stop_reason}")
    asyncio.run(collect_messages())           
