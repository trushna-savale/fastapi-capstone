#File that starts the FASTAPI application(main door of application)

from fastapi import FastAPI #imports the fast api class
from app.routes import router

app = FastAPI(
    title = "FastAPI Capstone" ,
    description = "Week 3 Capstone - Scafold a FastAPI Service" ,#tells what API does
    version = "1.0.0" #version no. because API change 
)  #creates api application

app.include_router(router)