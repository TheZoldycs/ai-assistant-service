
from customize import AssistantAgentCustomized,CONFIG_LIST
from autogen import UserProxyAgent


def ask_expert(message):
    assistant_for_expert = AssistantAgentCustomized(
        name="assistant_for_expert",
        llm_config={
            "temperature": 0,
            "config_list": CONFIG_LIST,
        },
    )
    expert = UserProxyAgent(
        name="expert",
        human_input_mode="ALWAYS",
        code_execution_config={"work_dir": "expert"},
    )

    expert.initiate_chat(assistant_for_expert, message=message)
    expert.stop_reply_at_receive(assistant_for_expert)
    # expert.human_input_mode, expert.max_consecutive_auto_reply = "NEVER", 0
    # final message sent from the expert
    expert.send("summarize the solution and explain the answer in an easy-to-understand way", assistant_for_expert)
    # return the last message the expert received
    return expert.last_message()["content"]