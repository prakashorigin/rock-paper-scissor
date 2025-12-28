# 🎮 Rock Paper Scissor Game

A classic Rock Paper Scissor game with both CLI and Web versions. Challenge the computer and test your luck!

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [CLI Version](#cli-version)
  - [Web Version](#web-version)
- [Game Rules](#game-rules)
- [How to Play](#how-to-play)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### CLI Version (rock_paper_scissor.py)
- Command-line interface for quick gameplay
- Real-time game logic with detailed explanations
- Input validation
- Beautiful formatted output
- Detailed game rules in code documentation

### Web Version (app.py)
- 🌐 Modern, responsive web interface
- 🎨 Beautiful gradient UI with animations
- 🚀 Flask-based backend
- 📱 Mobile-friendly design
- 🎯 Interactive button-based gameplay
- 📊 Real-time results with explanations
- ⚡ Zero installation for playing (just visit localhost)

## 📁 Project Structure

```
rock-paper-scissor/
│
├── rock_paper_scissor.py   # CLI version (Command-line game)
├── app.py                  # Web version (Flask application)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 📦 Prerequisites

- **Python 3.6+** (for CLI version)
- **Python 3.6+** and **Flask** (for Web version)
- **pip** (Python package manager)
- **git** (for version control)

### System Requirements
- **macOS/Linux/Windows** - All operating systems supported
- **RAM** - Minimal (< 100 MB)
- **Disk Space** - Less than 1 MB

## 🔧 Installation

### Step 1: Clone or Download the Repository

```bash
# If you have git installed
git clone https://github.com/yourusername/rock-paper-scissor.git
cd rock-paper-scissor

# Or manually download the files and navigate to the folder
cd /path/to/rock-paper-scissor
```

### Step 2: Install Dependencies (Web Version Only)

For the **CLI version**, no installation is needed. Python comes pre-installed on macOS.

For the **Web version**, install Flask:

```bash
pip install flask
```

Or install all dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

### CLI Version (Command-Line)

Run the classic CLI version:

```bash
python rock_paper_scissor.py
```

**Example Output:**
```
Enter your move (Rock, Paper, Scissor): Rock
User choice = Rock
Computer choice = Scissor
Rock smashes Scissor → You Win
```

### Web Version (Flask Application)

#### Step 1: Start the Flask Server

```bash
python app.py
```

You should see:
```
🎮 Rock Paper Scissor Web Game
========================================
Starting Flask server...
🌐 Open your browser: http://localhost:8000
========================================
```

#### Step 2: Open in Your Browser

Open your web browser and visit:
```
http://localhost:8000
```

#### Step 3: Play the Game

1. Click on **Rock**, **Paper**, or **Scissor** button
2. The computer will make a random choice
3. See your result instantly with beautiful animations
4. Click **Play Again** to play another round

#### Step 4: Stop the Server

Press `CTRL + C` in your terminal to stop the Flask server.

### Web Version Routes

- **`/`** - Home page with game buttons
- **`/play`** - Game logic and result display
- **`/rules`** - Detailed game rules explanation

## 🎯 Game Rules

### How the Game Works

Rock Paper Scissor is a hand game with three options:

1. **🪨 Rock**
   - Smashes Scissor → Rock Wins
   - Covered by Paper → Paper Wins
   - Versus Rock → Tie

2. **📄 Paper**
   - Covers Rock → Paper Wins
   - Cut by Scissor → Scissor Wins
   - Versus Paper → Tie

3. **✂️ Scissor**
   - Cuts Paper → Scissor Wins
   - Smashed by Rock → Rock Wins
   - Versus Scissor → Tie

### Win Conditions

```
Your Choice    vs   Computer's Choice   =   Result
─────────────────────────────────────────────────
Rock           vs   Scissor             =   You Win ✓
Paper          vs   Rock                =   You Win ✓
Scissor        vs   Paper               =   You Win ✓
X              vs   X                   =   Tie 🤝
Any Other      vs   Winning Choice      =   Computer Wins 🤖
```

## 📖 How to Play

### CLI Version

1. Run the Python script
2. Type your choice: `Rock`, `Paper`, or `Scissor` (case-insensitive)
3. Press Enter
4. Computer makes a random choice
5. Result is displayed with explanation
6. Run again to play another round

### Web Version

1. Start the Flask server (`python app.py`)
2. Open browser to `http://localhost:8000`
3. Click your choice button
4. See instant result with animations
5. Click "Play Again" for next round
6. Check "/rules" page for detailed game rules

## 💻 Technologies Used

### CLI Version
- **Language**: Python 3.6+
- **Libraries**: `random` (built-in)

### Web Version
- **Backend**: Python 3.6+ with Flask
- **Frontend**: HTML5, CSS3
- **Styling**: Modern CSS with gradients and animations
- **Responsiveness**: Mobile-friendly design

## 🔄 Git Workflow (To Push Your Own Copy)

### First Time Setup

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Add Rock Paper Scissor game"
```

### Push to GitHub

```bash
# Add your GitHub repository
git remote add origin https://github.com/yourusername/rock-paper-scissor.git

# Push to GitHub
git push -u origin main
```

### After Making Changes

```bash
# Stage all changes
git add .

# Commit with meaningful message
git commit -m "Update: Improve web interface with animations"

# Push to GitHub
git push
```

### Common Git Commands

```bash
# Check status
git status

# View commit history
git log

# View changes before committing
git diff

# Create a new branch
git checkout -b feature-name

# Merge branches
git merge feature-name
```

## 📝 Development Notes

### Code Structure - app.py

```python
# Game choices and rules
CHOICES = ["Rock", "Paper", "Scissor"]
RULES = { ... }

# Routes
@app.route("/")           # Home page
@app.route("/play")       # Game logic
@app.route("/rules")      # Rules page

# Emojis for better UX
choice_emoji = { "Rock": "🪨", "Paper": "📄", "Scissor": "✂️" }
```

### Styling Features

- **Gradient Background**: Purple/Blue gradient (`#667eea` → `#764ba2`)
- **Hover Effects**: Smooth transitions and transforms
- **Responsive Design**: Works on mobile, tablet, desktop
- **Accessibility**: Clear labels and semantic HTML
- **Color Scheme**:
  - Success: Green (#28a745)
  - Danger: Red (#f5c6cb)
  - Warning: Orange (#ffeaa7)

## 🐛 Troubleshooting

### Issue: "Python command not found"
**Solution**: Make sure Python is installed. Check with `python --version`

### Issue: "Flask not found"
**Solution**: Install Flask with `pip install flask`

### Issue: "Port 8000 already in use"
**Solution**: 
- Change port in `app.py`: `app.run(port=8001)`
- Or kill the process: `lsof -ti:8000 | xargs kill -9`

### Issue: "Connection refused" when visiting localhost:8000
**Solution**: 
- Make sure Flask server is running
- Check the terminal output for any errors
- Try `http://127.0.0.1:8000` instead

## 📚 Learning Resources

- [Python Official Docs](https://docs.python.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [HTML & CSS Guide](https://www.w3schools.com/)
- [Git & GitHub Guide](https://guides.github.com/)

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Suggested Improvements

- [ ] Add score tracking system
- [ ] Implement multiplayer mode
- [ ] Add difficulty levels
- [ ] Create statistics/analytics page
- [ ] Add sound effects
- [ ] Implement user accounts/login
- [ ] Add AI difficulty variations
- [ ] Create mobile app version

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created with ❤️ by You

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Create an issue on GitHub
3. Contact the author

---

**Happy Gaming! 🎮**

*Last Updated: December 29, 2025*
