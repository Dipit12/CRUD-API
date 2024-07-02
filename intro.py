# to run a virtual environment - python3 -m venv <virtaul_env_name>
"""
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

"""
# to start the live server : uvicorn file_name : instance_name
# eg uvicorn main:app
# to make the server run in background : uvicorn main:app --reload

"""
We ultimately want to force the client to send the data in a schema
Pydantic is the most widely used data validation library for Python.

it helps to validate the data sent by the client, so that it follows the schema
"""