"""A sample package that uses `poetry`"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def serve():
    """Launched with `poetry run start` at root level"""
    import uvicorn
    uvicorn.run("poetry_sample:app", host="0.0.0.0", port=8000, reload=True)
