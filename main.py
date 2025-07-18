import uvicorn

from framefox.application import Application

app = Application().boot_web().app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
