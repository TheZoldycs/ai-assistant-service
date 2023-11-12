### AI Assistant Service (JUNCTION 2023)

**Description:**

This is an AI bot chat service built in GPT autogen. It is written in Python using Django 4.2.7, RabbitMQ via pika, celery multithreading, PostgreSQL, and AutoGen. It provides a variety of features, including:

* Natural language processing
* Task management
* Knowledge base
* Customized bots
* Conversation between bots
* Human participation
* Various modes of operation

**Technologies:**

* Python
* Django 4.2.7
* RabbitMQ via pika
* celery multithreading
* PostgreSQL
* AutoGen

**Getting Started:**

To get started with the AI Assistant Service, clone this repository and run the following commands:

```
pip install -r requirements.txt
python manage.py migrate
celery -A ai_assistant_service worker --concurrency=4
python manage.py runserver
```

Once the server is running, you can access the AI Assistant Service at `http://localhost:8000/`.

You can also use the Django admin interface to manage the assistant and its data.

**Contributing:**

If you would like to contribute to the AI Assistant Service, please feel free to open a pull request. We welcome all contributions, big or small.


**AutoGen:**

AutoGen is a framework that enables development of LLM applications using multiple agents that can converse with each other to solve tasks. AutoGen agents are customizable, conversable, and seamlessly allow human participation. They can operate in various modes that employ combinations of LLMs, human inputs, and tools.

**Bots Team:**

The AI Assistant Service includes a team of bots, each with its own expertise:

* Gym expert: This bot can answer questions about fitness, nutrition, and exercise.
* Food expert: This bot can answer questions about food, recipes, and cooking.
* Final resumer: This bot can help you write a resume that will stand out to potential employers.

You can interact with these bots directly or use them to help you complete tasks, such as planning a workout, cooking a meal, or writing a resume.
