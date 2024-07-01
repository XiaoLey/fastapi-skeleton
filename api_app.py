from bootstrap.application import create_app

app = create_app()


@app.get("/")
async def root():
    return "welcome to fastapi skeleton"
