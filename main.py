from app import app
import uvicorn

if '__main__' == __name__:
    uvicorn.run(app, reload=True, port="5000")