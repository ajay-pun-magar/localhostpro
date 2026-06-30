from fastapi import FastAPI
app = FastAPI(title="localhostpro")

@app.get("/")
def read_root():
    return {"message": f"Welcome to localhostpro. Environment is configured successfully!"}