from google.adk import Workflow

root_agent = Workflow(
    name="parent_workflow",
    edges=[
       ("START", task_A1, router),
       (router, {
            "RUN_WORKFLOW_B": workflow_B,
            "RUN_WORKFLOW_C": workflow_C,
            },
       ),
    ],
)

'''
This is a really simple example of a parent workflow that can route to different workflows based on the output of a router node. 
The router node can be a simple function that returns a string that matches one of the keys in the dictionary passed to it. 
The router node can also be an agent that uses a model to determine which workflow to run next.

Output for nested Workflow objects works slightly differently from individual nodes.
When the nested workflow completes one of its nodes,
it transmits data to the next node in the nested workflow's graph and the system bubbles up the Event for that node to the parent
 workflow for process traceability.
When the nested workflow completes the last node in its process,
 the parent node extracts data from the final leaf nodes and emits it as the output of the nested workflow.

'''