# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI()

# # Define a Pydantic model for the data to be received in the POST request
# class NameRequest(BaseModel):
#     name: str
#     age: Optional[int] = None  # Optional field

# # Define the POST endpoint
# @app.post("/save_name/")
# async def save_name(data: NameRequest):
#     # Process the data (e.g., save to the database, etc.)
#     response_data = {
#         "message": "Data received successfully",
#         "name": data.name,
#         "age": data.age if data.age is not None else "Not provided"
#     }
#     return response_data

# # To run the app, use the following command:
# # uvicorn <filename>:app --reload

#app.py

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_world():
    return "Hello,World"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
