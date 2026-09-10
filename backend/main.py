from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS so SvelteKit (port 5173) can talk to Python (port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

count = 0

@app.get("/api/greet")
def read_greet(name: str = "World"):
    global count
    count += 1
    return {"message": f"{count} Hello, {name} from Python!"}