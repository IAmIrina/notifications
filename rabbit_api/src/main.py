import pika
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.config import settings
from src.api.v1 import template, events
from src.db import rabbit
from src.db.postgres import engine
from src.models import models

app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    credentials = pika.PlainCredentials(
        username=settings.rabbit.user_name,
        password=settings.rabbit.password
    )
    connection_parameters = pika.ConnectionParameters(
        settings.rabbit.host,
        settings.rabbit.port,
        credentials=credentials
    )
    rabbit.rq = pika.BlockingConnection(connection_parameters)
    rabbit.rq.channel().queue_declare('fast')
    rabbit.rq.channel().queue_declare('slow')


@app.on_event('shutdown')
async def shutdown():
    rabbit.rq.close()


models.Base.metadata.create_all(bind=engine)

app.include_router(template.router, prefix='/api/v1/template', tags=['template'])
app.include_router(events.router, prefix='/api/v1/event', tags=['event'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        reload=settings.uvicorn_reload,
        host='0.0.0.0',
        port=8000,
    )
