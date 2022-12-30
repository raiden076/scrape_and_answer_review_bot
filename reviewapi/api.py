from fastapi import FastAPI
from reviewapi import brain

app = FastAPI()


@app.get("/api")
async def root():
    return {"this api will return the response to the latest review of a google place"}


@app.get("/api/{full_path:path}")
async def api(full_path: str):  # type: ignore
    return brain(full_path)  # type: ignore


brain("https://goo.gl/maps/uizsBv1sdDK8CG9Z8")
