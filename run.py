import uvicorn

from app.config import settings as cfg

if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host=cfg.APP_HOST,
        port=cfg.APP_PORT,
        reload=True,
        workers=1
    )
