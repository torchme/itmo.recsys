import os
import uvicorn


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run("service.api.app.app:app", host=host, port=port)
