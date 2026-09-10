# sveltekit
requires [node.js](https://nodejs.org/en/download) to run sveltekit
to create sveltekit project run
```bash
npm sv create frontend
```
then choose how the project is made
for this project I chose minimalistic,javascript,none and npm
then do the following
```bash
cd name
npm install
npm run dev
```
this should run the svelte local host
# python
create another directory named backend
add main.py to it
in the backend directory run
```bash
pip install fastapi uvicorn
```
this will install fastapi which will let the backend comunicate with the frontend
```python
from fastapi import FastAPI# Imports fast api lib which create and configure web applications
from fastapi.middleware.cors import CORSMiddleware# imports security tool that restricts web browsers from making requests to this API from a different domain or port.

app = FastAPI()# creates an instance of fastapi.handles routing and incoming HTTP requests.

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
```
