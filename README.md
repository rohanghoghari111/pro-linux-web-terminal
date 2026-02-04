# Pro Linux Web Terminal (WSL Powered)

A **professional, fast, and realistic Linux web terminal** built using **FastAPI + WSL + Vanilla HTML/CSS/JS**.
This project provides a browser-based Linux terminal experience that executes **real Linux commands via WSL**, with strict input locking, zero UI hanging, and production-grade behavior.

---

## ✨ Features

* ⚡ **Real Linux commands via WSL** (not simulated)
* 🔒 **Strict input lock** – user cannot type a new command until output arrives
* 🧠 **WSL warm-up** for fast first command execution
* 🖥️ **Persistent working directory** (`cd` works exactly like Linux)
* 🎯 **No subprocess timeout** – long commands handled correctly
* 🧼 `clear` command handled instantly (frontend + backend)
* 🧵 Non-blocking backend using `subprocess.Popen`
* 🎨 Professional terminal UI with Matrix background
* 🟢 Visual execution status (loading dots)
* 🧪 Tested for strict company-level QA checks

---

## 🏗️ Project Structure

```
linux_prj/
│
├── app.py              # FastAPI backend (WSL command execution)
├── index.html          # Frontend terminal UI
├── run_server.bat      # One-click server launcher (Windows)
├── README.md           # Project documentation
└── .gitignore          # Git ignore rules
```

---

## 🔧 Requirements

### System

* Windows 10 / 11
* **WSL installed** (Ubuntu recommended)
* Python **3.9+**

### Python Packages

```
fastapi
uvicorn
```

Install using:

```
pip install fastapi uvicorn
```

---

## 🐧 WSL Setup (One Time)

Make sure WSL is installed and working:

```
wsl --install
```

Check Linux:

```
wsl
pwd
```

Set your project directory inside WSL:

```
/home/ghoghari/linux_prj
```

⚠️ **Important:** The path above must exist in WSL. Modify `current_dir` in `app.py` if needed.

---

## ▶️ How to Run

### Option 1: Using BAT file (Recommended)

Double-click:

```
run_server.bat
```

This will:

* Activate Python
* Start FastAPI using Uvicorn
* Bind server to `http://127.0.0.1:8000`

---

### Option 2: Manual Run

```
python app.py
```

Then open browser:

```
http://127.0.0.1:8000
```

---

## 🧠 Backend Design (Important)

### WSL Warm-Up

WSL is initialized **once at server start** to avoid first-command delay:

```python
subprocess.run(["wsl","bash","-lc","echo WSL_READY"])
```

### Command Execution Flow

* Uses `subprocess.Popen`
* No timeout
* No blocking calls
* `pwd` appended to track working directory

### Security Scope

⚠️ This project is designed for **local / internal usage**.
Do NOT expose publicly without:

* Authentication
* Command filtering
* Sandboxing

---

## 🖥️ Frontend Behavior

* Input is **disabled while command runs**
* User cannot spam commands
* Output must finish before next prompt
* Scroll handled smoothly
* Black scrollbar (fully themed)

---

## 🧪 QA / Tester Notes

✔ Real Linux execution (WSL)
✔ Correct command behavior (`cd`, `pwd`, `ls`, `ping`, etc.)
✔ No UI hang
✔ No backend hang
✔ Accurate prompt updates
✔ Professional-grade terminal simulation

---

## 🚀 Future Improvements (Optional)

* Command allowlist
* Multi-user sessions
* WebSocket streaming output
* Docker-based Linux instead of WSL

---

## 👨‍💻 Author

**Rohan Ghoghari**
Linux • FastAPI • System Design

---

## 📜 License

This project is for **educational and internal use**.
Reuse and modify freely for learning purposes.
