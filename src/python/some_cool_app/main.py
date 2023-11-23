import uvicorn
from fastapi import FastAPI
from some_cool_library.main import generate_df

app = FastAPI()


@app.get("/")
def read_root():
    return len(generate_df())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
