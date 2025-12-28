# SETUP & USAGE QUICK GUIDE

## 🚀 Quick Start

### 1️⃣ CLI VERSION (No Installation)
```bash
python rock_paper_scissor.py
```
Then type: Rock, Paper, or Scissor

---

### 2️⃣ WEB VERSION (Requires Flask)

#### Step 1: Install Flask
```bash
pip install flask
```

#### Step 2: Start the Server
```bash
python app.py
```

#### Step 3: Open Browser
Visit: http://localhost:8000

#### Step 4: Stop Server
Press: CTRL + C

---

## 📤 PUSH TO GITHUB

### First Time (One-time setup):
```bash
git init
git add .
git commit -m "Add Flask web version"
git remote add origin https://github.com/yourusername/rock-paper-scissor.git
git branch -M main
git push -u origin main
```

### After Making Changes:
```bash
git add .
git commit -m "Your commit message here"
git push
```

---

## 📁 PROJECT FILES

✅ **rock_paper_scissor.py** - CLI version (no setup needed)
✅ **app.py** - Web version with Flask
✅ **requirements.txt** - Python dependencies list
✅ **README.md** - Full documentation
✅ **.gitignore** - Git ignore rules
✅ **QUICKSTART.md** - This file

---

## 🎮 GAME RULES

| Your Choice | vs | Computer | = | Result |
|-------------|----|-----------|----|--------|
| Rock | vs | Scissor | = | YOU WIN ✓ |
| Paper | vs | Rock | = | YOU WIN ✓ |
| Scissor | vs | Paper | = | YOU WIN ✓ |
| Rock | vs | Paper | = | COMPUTER WINS |
| Paper | vs | Scissor | = | COMPUTER WINS |
| Scissor | vs | Rock | = | COMPUTER WINS |
| X | vs | X | = | TIE 🤝 |

---

## ✨ WEB VERSION FEATURES

- 🎨 Beautiful gradient UI with animations
- 📱 Mobile-responsive design
- 🎯 One-click gameplay
- 📊 Real-time results display
- ♿ Accessible design
- ⚡ Fast and lightweight

---

## 🐛 TROUBLESHOOTING

**Q: "Flask not found" error?**
A: Run `pip install flask`

**Q: "Port 8000 already in use"?**
A: Kill process: `lsof -ti:8000 | xargs kill -9`

**Q: Browser shows "Connection refused"?**
A: Check Flask server is running in terminal

---

## 📝 NOTES

- Python 3.6+ required
- Flask 2.3+ included in requirements.txt
- Both CLI and Web versions use same game logic
- No database needed - purely in-memory game
- Fully open source - MIT License

---

Happy Gaming! 🎮
