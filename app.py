import subprocess
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# START PATH IN WSL
current_dir = "/home/ghoghari/linux_prj"

# ---- WSL WARM-UP (ONE TIME, BLOCKING, NO TIMEOUT) ----
subprocess.run(
    ["wsl", "bash", "-lc", "echo WSL_READY"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)
# ----------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/execute")
async def execute(request: Request):
    global current_dir
    data = await request.json()
    command = data.get("command", "").strip()

    if not command:
        return {"output": "", "cwd": current_dir, "status": "success"}

    if command == "clear":
        return {"output": "__CLEAR__", "cwd": current_dir, "status": "success"}

    bash_cmd = f'cd "{current_dir}" && {command} ; pwd'

    # IMPORTANT: NO timeout, NO subprocess.run
    process = subprocess.Popen(
        ["wsl", "bash", "-lc", bash_cmd],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate()

    if stdout:
        lines = stdout.rstrip().split("\n")
        current_dir = lines[-1]
        output = "\n".join(lines[:-1])
    else:
        output = stderr.strip()

    return {
        "output": output,
        "cwd": current_dir,
        "status": "success"
    }

if __name__ == "__main__":
    print("Server running at http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)




















































































