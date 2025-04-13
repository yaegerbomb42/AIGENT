from langgraph.graph import StateGraph
from langchain.chat_models import ChatOpenAI
from memory.chroma_memory import create_vectorstore_memory
from chains.planner_chain import planner_chain
from chains.build_chain import build_chain
from chains.test_chain import test_chain
from chains.deploy_chain import deploy_chain
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

llm = ChatOpenAI(temperature=0.2, model="gpt-4-1106-preview")
memory = create_vectorstore_memory()

graph = StateGraph()
graph.add_node("Plan", planner_chain)
graph.add_node("Build", build_chain)
graph.add_node("Test", test_chain)
graph.add_node("Deploy", deploy_chain)

graph.set_entry_point("Plan")
graph.add_edge("Plan", "Build")
graph.add_edge("Build", "Test")
graph.add_edge("Test", "Deploy")
graph.set_finish_point("Deploy")

workflow = graph.compile()

if __name__ == "__main__":
    try:
        goal = input("Describe the app you want to build: ")
        result = workflow.invoke({"input": goal})
        logger.info("\nFinal Result: %s", result)
    except Exception as e:
        logger.error("Agent failed: %s", str(e))
