from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>🎄 Merry Christmas 🎄</title>

<style>
body {
    margin: 0;
    height: 100vh;
    background: linear-gradient(#0f2027, #203a43, #2c5364);
    color: white;
    text-align: center;
    font-family: Arial;
    overflow: hidden;
}

h1 {
    margin-top: 20px;
}

.tree-container {
    margin-top: 30px;
    cursor: pointer;
}

svg {
    width: 320px;
    max-width: 90vw;
}

/* Glow */
.glow {
    filter: drop-shadow(0 0 15px #00ffcc);
}

/* Star animation */
.star {
    animation: starGlow 1.5s infinite alternate;
}

@keyframes starGlow {
    from { filter: drop-shadow(0 0 5px gold); }
    to { filter: drop-shadow(0 0 20px gold); }
}

/* Lights */
.light {
    animation: blink 1s infinite alternate;
}

@keyframes blink {
    from { opacity: 0.3; }
    to { opacity: 1; }
}

/* Message */
#message {
    display: none;
    margin-top: 25px;
    font-size: 22px;
    color: #ffd700;
    white-space: pre-line;
    text-shadow: 0 0 10px rgba(255,215,0,0.6);
}

/* Snow */
.snowflake {
    position: absolute;
    top: -10px;
    color: white;
    animation: fall linear infinite;
}

@keyframes fall {
    to {
        transform: translate(100px, 110vh);
    }
}
</style>
</head>

<body>

<h1>🎄 Merry Christmas 🎄</h1>

<div class="tree-container" onclick="showMessage()">
<svg viewBox="0 0 300 360" class="glow">

    <!-- Star -->
    <polygon class="star"
        points="150,10 160,40 190,40 165,60 175,90 150,70 125,90 135,60 110,40 140,40"
        fill="gold"/>

    <!-- Tree layers -->
    <polygon points="150,50 90,140 210,140" fill="#2ecc71"/>
    <polygon points="150,110 70,220 230,220" fill="#27ae60"/>
    <polygon points="150,180 50,320 250,320" fill="#1e8449"/>

    <!-- Trunk -->
    <rect x="130" y="320" width="40" height="30" fill="#8e5a2a"/>

    <!-- Lights -->
    <circle class="light" cx="150" cy="120" r="5" fill="red"/>
    <circle class="light" cx="120" cy="170" r="5" fill="yellow"/>
    <circle class="light" cx="180" cy="170" r="5" fill="cyan"/>
    <circle class="light" cx="100" cy="250" r="5" fill="pink"/>
    <circle class="light" cx="200" cy="250" r="5" fill="orange"/>

</svg>
</div>

<div id="message">
💖 Chúc Hương Giang Giáng Sinh vui vẻ,  
thi đâu qua đó, tiền rơi như tuyết ❄️  

— From your bro 💚
</div>

<script>
function showMessage() {
    document.getElementById("message").style.display = "block";
}

// Snow
function snow() {
    const s = document.createElement("div");
    s.className = "snowflake";
    s.innerHTML = "❄";
    s.style.left = Math.random() * window.innerWidth + "px";
    s.style.fontSize = 10 + Math.random() * 20 + "px";
    s.style.animationDuration = 3 + Math.random() * 3 + "s";
    document.body.appendChild(s);
    setTimeout(() => s.remove(), 6000);
}
setInterval(snow, 200);
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

