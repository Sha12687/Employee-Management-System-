from fastapi import FastAPI
import os
from dotenv import load_dotenv
app=FastAPI()

from App.routes.employee import router as employee_router
from App.routes.department import router as dept_router
from App.routes.auth import router as auth_router
app.include_router(employee_router)
app.include_router(dept_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Welcome to Employee API and Department API"}