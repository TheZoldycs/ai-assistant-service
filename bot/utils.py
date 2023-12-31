import autogen
from decouple import config
from .customize import AssistantAgentCustomized, UserProxyAgentJunction2023
#Autogen configuration
CONFIG_LIST_GRP = [
    {
        'model': 'gpt-4',
        'api_key': config("OPENAI_API_KEY"),
    },
]

llm_config = {"config_list": CONFIG_LIST_GRP,}


def start_chat(user_info,chat_id):
    """
    Srarting chat `function`
    """

    user_proxy = UserProxyAgentJunction2023(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
    human_input_mode="TERMINATE",
    chat_id=chat_id
    
    )

    food_expert = AssistantAgentCustomized(
        name="food_expert",
        system_message="Creative and expert in food",
        llm_config=llm_config,
    )

    gym_expert = AssistantAgentCustomized(
        name="gym_expert",
        system_message="Creative and expert in gym and workout",
        llm_config=llm_config,
    )

    #set an advanced ai groupchat 
    groupchat = autogen.GroupChat(agents=[user_proxy, gym_expert, food_expert], messages=[], max_round=1)
    #set a group manager
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    user_proxy.initiate_chat(
    manager,
    message=f"""Get me recommendation food today with this provided information,\n
        "vegetarian":{user_info["vegetarian"]},
        "vegan":{user_info["vegan"]},
        "gluten_free":{user_info["gluten_free"]},
        "dairy_free":{user_info["dairy_free"]},
        "nut_allergy":{user_info["nut_allergy"]},
        "age":{user_info["age"]} years,
        "calories_goal":{user_info["calories_goal"]}Kcal,
        "weight":{user_info["weight"]} kg
    """,
    )
