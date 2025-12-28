"""
Rock Paper Scissor Game - Flask Web Application
This is a web-based version of the classic Rock-Paper-Scissor game.
Play against the computer in your browser!

Features:
- Beautiful, responsive web interface
- Play with emoji buttons (Rock, Paper, Scissor)
- Real-time game results with explanations
- Mobile-friendly design
- Detailed game rules page
"""

from flask import Flask, request
import random

app = Flask(__name__)

# Game choices
CHOICES = ["Rock", "Paper", "Scissor"]

# Game rules with explanations
RULES = {
    "Rock": {"Scissor": "Rock smashes Scissor → You Win", "Paper": "Paper covers Rock → Computer Wins"},
    "Paper": {"Rock": "Paper covers Rock → You Win", "Scissor": "Scissor cuts Paper → Computer Wins"},
    "Scissor": {"Paper": "Scissor cuts Paper → You Win", "Rock": "Rock smashes Scissor → Computer Wins"}
}


@app.route("/")
def home():
    """Home page with game form"""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Rock Paper Scissor Game</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
                padding: 40px;
                max-width: 500px;
                width: 100%;
                text-align: center;
            }
            
            h1 {
                color: #333;
                margin-bottom: 10px;
                font-size: 2.5em;
            }
            
            .subtitle {
                color: #666;
                margin-bottom: 30px;
                font-size: 1.1em;
            }
            
            .form-group {
                margin-bottom: 25px;
            }
            
            .form-group label {
                display: block;
                margin-bottom: 10px;
                color: #333;
                font-weight: 600;
                font-size: 1.1em;
            }
            
            .button-group {
                display: flex;
                gap: 10px;
                justify-content: center;
                margin-bottom: 20px;
                flex-wrap: wrap;
            }
            
            .choice-btn {
                padding: 12px 25px;
                font-size: 1em;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                background-color: #667eea;
                color: white;
                font-weight: 600;
                transition: all 0.3s ease;
                flex: 1;
                min-width: 120px;
            }
            
            .choice-btn:hover {
                background-color: #764ba2;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            }
            
            .choice-btn:active {
                transform: translateY(0);
            }
            
            .emoji {
                font-size: 2.5em;
                margin-right: 5px;
            }
            
            .info-box {
                background-color: #f0f4ff;
                border-left: 4px solid #667eea;
                padding: 15px;
                margin-top: 20px;
                text-align: left;
                border-radius: 5px;
                color: #333;
            }
            
            .info-box h3 {
                color: #667eea;
                margin-bottom: 10px;
            }
            
            .info-box p {
                font-size: 0.9em;
                margin-bottom: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎮 Rock Paper Scissor</h1>
            <p class="subtitle">Challenge the Computer!</p>
            
            <div class="form-group">
                <label>Choose Your Move:</label>
                <div class="button-group">
                    <form action="/play" method="GET" style="display: inline;">
                        <input type="hidden" name="user_choice" value="Rock">
                        <button type="submit" class="choice-btn">
                            <span class="emoji">🪨</span> Rock
                        </button>
                    </form>
                    <form action="/play" method="GET" style="display: inline;">
                        <input type="hidden" name="user_choice" value="Paper">
                        <button type="submit" class="choice-btn">
                            <span class="emoji">📄</span> Paper
                        </button>
                    </form>
                    <form action="/play" method="GET" style="display: inline;">
                        <input type="hidden" name="user_choice" value="Scissor">
                        <button type="submit" class="choice-btn">
                            <span class="emoji">✂️</span> Scissor
                        </button>
                    </form>
                </div>
            </div>
            
            <div class="info-box">
                <h3>📋 Game Rules:</h3>
                <p>🪨 <strong>Rock</strong> smashes Scissor</p>
                <p>📄 <strong>Paper</strong> covers Rock</p>
                <p>✂️ <strong>Scissor</strong> cuts Paper</p>
            </div>
        </div>
    </body>
    </html>
    """


@app.route("/play")
def play():
    """Game logic and result display"""
    user_choice = request.args.get("user_choice", "").capitalize()
    
    # Validate user choice
    if user_choice not in CHOICES:
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Invalid Choice</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }}
                .container {{
                    background: white;
                    border-radius: 15px;
                    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
                    padding: 40px;
                    max-width: 500px;
                    width: 100%;
                    text-align: center;
                }}
                h2 {{ color: #e74c3c; }}
                a {{
                    display: inline-block;
                    margin-top: 20px;
                    padding: 12px 30px;
                    background-color: #667eea;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-weight: 600;
                    transition: all 0.3s ease;
                }}
                a:hover {{ background-color: #764ba2; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>❌ Invalid Input!</h2>
                <p>Please select Rock, Paper, or Scissor</p>
                <a href="/">← Back to Game</a>
            </div>
        </body>
        </html>
        """
    
    # Computer's random choice
    comp_choice = random.choice(CHOICES)
    
    # Determine result
    if user_choice == comp_choice:
        result = "🤝 Match Tie"
        result_class = "tie"
    elif user_choice == comp_choice or (user_choice in RULES and comp_choice in RULES[user_choice]):
        result = "🎉 You Win"
        result_class = "win"
    else:
        result = "🤖 Computer Wins"
        result_class = "lose"
    
    # Get explanation from rules
    if user_choice == comp_choice:
        explanation = "Both chose the same!"
    else:
        explanation = RULES[user_choice].get(comp_choice, "")
    
    # Get emojis for choices
    choice_emoji = {
        "Rock": "🪨",
        "Paper": "📄",
        "Scissor": "✂️"
    }
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Game Result</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }}
            
            .container {{
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
                padding: 40px;
                max-width: 600px;
                width: 100%;
                text-align: center;
            }}
            
            h1 {{
                color: #333;
                margin-bottom: 30px;
                font-size: 2.2em;
            }}
            
            .choices {{
                display: flex;
                justify-content: space-around;
                margin-bottom: 30px;
                align-items: center;
                flex-wrap: wrap;
                gap: 20px;
            }}
            
            .choice {{
                flex: 1;
                min-width: 150px;
            }}
            
            .choice h3 {{
                color: #666;
                margin-bottom: 10px;
                font-size: 0.9em;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            
            .choice-item {{
                font-size: 4em;
                margin-bottom: 10px;
            }}
            
            .choice-name {{
                font-size: 1.3em;
                color: #333;
                font-weight: 600;
            }}
            
            .vs {{
                font-size: 2em;
                color: #667eea;
                font-weight: bold;
            }}
            
            .result {{
                margin: 30px 0;
                padding: 25px;
                border-radius: 10px;
                font-size: 2em;
                font-weight: 700;
            }}
            
            .result.win {{
                background-color: #d4edda;
                color: #155724;
                border: 2px solid #28a745;
            }}
            
            .result.lose {{
                background-color: #f8d7da;
                color: #721c24;
                border: 2px solid #f5c6cb;
            }}
            
            .result.tie {{
                background-color: #fff3cd;
                color: #856404;
                border: 2px solid #ffeaa7;
            }}
            
            .explanation {{
                color: #666;
                margin: 15px 0;
                font-size: 1.1em;
                font-style: italic;
            }}
            
            .button-group {{
                display: flex;
                gap: 15px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 30px;
            }}
            
            .button-group a {{
                padding: 12px 30px;
                background-color: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                font-weight: 600;
                transition: all 0.3s ease;
                border: none;
                cursor: pointer;
                font-size: 1em;
            }}
            
            .button-group a:hover {{
                background-color: #764ba2;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            }}
            
            .stats {{
                background-color: #f0f4ff;
                border-left: 4px solid #667eea;
                padding: 15px;
                margin-top: 20px;
                text-align: left;
                border-radius: 5px;
                color: #333;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎮 Game Result</h1>
            
            <div class="choices">
                <div class="choice">
                    <h3>Your Choice</h3>
                    <div class="choice-item">{choice_emoji.get(user_choice, '')}</div>
                    <div class="choice-name">{user_choice}</div>
                </div>
                
                <div class="vs">VS</div>
                
                <div class="choice">
                    <h3>Computer Choice</h3>
                    <div class="choice-item">{choice_emoji.get(comp_choice, '')}</div>
                    <div class="choice-name">{comp_choice}</div>
                </div>
            </div>
            
            <div class="result {result_class}">
                {result}
            </div>
            
            <div class="explanation">
                {explanation}
            </div>
            
            <div class="stats">
                <strong>📊 How to Win:</strong>
                <p>🪨 Rock smashes Scissor</p>
                <p>📄 Paper covers Rock</p>
                <p>✂️ Scissor cuts Paper</p>
            </div>
            
            <div class="button-group">
                <a href="/">← Play Again</a>
            </div>
        </div>
    </body>
    </html>
    """


@app.route("/rules")
def rules():
    """Display game rules"""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Game Rules</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
                padding: 40px;
                max-width: 600px;
                width: 100%;
            }
            
            h1 { color: #333; text-align: center; margin-bottom: 30px; }
            
            .rule { 
                background-color: #f9f9f9;
                border-left: 4px solid #667eea;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 8px;
            }
            
            .rule h3 {
                color: #667eea;
                margin-bottom: 10px;
                font-size: 1.3em;
            }
            
            .rule p { color: #666; margin: 8px 0; }
            
            .rule-emoji { font-size: 2em; margin-right: 10px; }
            
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 12px 30px;
                background-color: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                font-weight: 600;
                transition: all 0.3s ease;
            }
            
            a:hover {
                background-color: #764ba2;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📋 How to Play</h1>
            
            <div class="rule">
                <h3><span class="rule-emoji">🪨</span> Rock</h3>
                <p>• Rock vs Rock → Tie</p>
                <p>• Rock vs Paper → Paper Wins (Paper covers Rock)</p>
                <p>• Rock vs Scissor → Rock Wins (Rock smashes Scissor)</p>
            </div>
            
            <div class="rule">
                <h3><span class="rule-emoji">📄</span> Paper</h3>
                <p>• Paper vs Paper → Tie</p>
                <p>• Paper vs Rock → Paper Wins (Paper covers Rock)</p>
                <p>• Paper vs Scissor → Scissor Wins (Scissor cuts Paper)</p>
            </div>
            
            <div class="rule">
                <h3><span class="rule-emoji">✂️</span> Scissor</h3>
                <p>• Scissor vs Scissor → Tie</p>
                <p>• Scissor vs Rock → Rock Wins (Rock smashes Scissor)</p>
                <p>• Scissor vs Paper → Scissor Wins (Scissor cuts Paper)</p>
            </div>
            
            <a href="/">← Back to Game</a>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    print("🎮 Rock Paper Scissor Web Game")
    print("=" * 40)
    print("Starting Flask server...")
    print("🌐 Open your browser: http://localhost:8000")
    print("=" * 40)
    app.run(host="0.0.0.0", port=8000, debug=True)
