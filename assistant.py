from autogen import UserProxyAgent
from customize import CONFIG_LIST, AssistantAgentCustomized
import autogen
from utils import ask_expert
#Autogen configuration
assistant_for_student = AssistantAgentCustomized(
    name="assistant_for_student",
    system_message="You are a helpful assistant. Reply TERMINATE when the task is done.",
    llm_config={
        "timeout": 600,
       # "cache_seed": 42,
        "config_list": CONFIG_LIST,
        "temperature": 0,
        "functions": [
            {
                "name": "ask_expert",
                "description": "ask expert when you can't solve the problem satisfactorily.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "question to ask expert. Ensure the question includes enough context, such as the code and the execution result. The expert does not know the conversation between you and the user unless you share the conversation with the expert.",
                        },
                    },
                    "required": ["message"],
                },
            }
        ],
    }
)

student = autogen.UserProxyAgent(
    name="student",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir": "student"},
    function_map={"ask_expert": ask_expert},
)

# the assistant receives a message from the student, which contains the task description
student.initiate_chat(
    assistant_for_student,
    message="""Find $a + b + c$, given that $x+y \\neq -1$ and 
\\begin{align}
	ax + by + c & = x + 7,\\
	a + bx + cy & = 2x + 6y,\\
	ay + b + cx & = 4x + y.
\\end{align}.
""",
)