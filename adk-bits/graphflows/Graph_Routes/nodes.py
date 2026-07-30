from google.adk import Event


def my_function_node(node_input: str):
    input_text_modified = node_input.upper()
    return Event(output=input_text_modified) 


# Notes ---
'''
This is an example Node. It is a simple FunctionNode that handles text inputs and sends a text output:

A graph is composed of execution nodes. 
These nodes can be Agents, ADK Tools, human input tasks, or code functions you write.
Nodes can take inputs from previously executed nodes, and emit data through Event objects.


'''