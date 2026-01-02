from fastapi import FastAPI
from routers import matrics, aws

app = FastAPI(
    title= "Internal Devops Utilities API",
    description = "This is an Internal API Utilities app for Monitoring metrix",
    version= "1.0.0",
    doc_url="/docs",
    redoc_url="/redoc"

)

@app.get("/")
def hello():
    """
    This is a Hello API, just for testing
    """
    return {f"message":"Hello Doston This is Devops utilites API "}

app.include_router(matrics.router)
app.include_router(aws.router, prefix="/aws")