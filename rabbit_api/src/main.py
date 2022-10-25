import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.config import api_settings
from src.api.v1 import template
from src.db.postgres import engine
from src.models import models

app = FastAPI(
    title=api_settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    ...


@app.on_event('shutdown')
async def shutdown():
    ...


models.Base.metadata.create_all(bind=engine)

app.include_router(template.router, prefix='/api/v1/template', tags=['template'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        reload=api_settings.uvicorn_reload,
        host='0.0.0.0',
        port=8000,
    )
