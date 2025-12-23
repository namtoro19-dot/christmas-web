from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
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

/* ===== TITLE ===== */
h1 {
    margin-top: 15px;
}

/* ===== TREE SVG ===== */
svg {
    width: 300px;
    height: 420px;
    margin-top: 20px;
    cursor: pointer;
}

/* Viền cây */
#treePath {
    fill: none;
    stroke: #00ffcc;
    stroke-width: 4;
    stroke-linecap: round;
    filter: drop-shadow(0 0 10px #00ffcc);
    stroke-dasharray: 1000;
    stroke-dashoffset: 1000;
    animation: drawTree 4s ease forwards;
}

/* Vẽ cây */
@keyframes drawTree {
    to {
        stroke-dashoffset: 0;
    }
}

/* Ngôi sao */
#star {
    opacity: 0;
    filter: drop-shadow(0 0 20px gold);
    animation: starGlow 1.5s infinite alternate;
    animation-delay: 4s;
    animation-fill-mode: forwards;
}

@keyframes starGlow {
    from { transform: scale(1); opacity: 1; }
    to { transform: scale(1.15); opacity: 1; }
}

/* ===== MERRY CHRISTMAS ===== */
#title {
    margin-top: 10px;
    font-size: 32px;
    color: gold;
    text-shadow: 0 0 15px gold;
    opacity: 0;
    animation: showTitle 2s ease forwards;
    animation-delay: 4.5s;
}

@keyframes showTitle {
    to { opacity: 1; }
}

/* ===== MESSAGE ===== */
#message {
    display: none;
    margin-top: 20px;
    font-size: 22px;
    color: #ffd700;
    white-space: pre-line;
    text-shadow: 0 0 10px rgba(255,215,0,0.6);
}

/* ===== SNOW ===== */
.snowflake {
    position: absolute;
    top: -10px;
    color: white;
    font-size: 16px;
    animation: fall linear infinite;
}

@keyframes fall {
    to {
        transform: translate(120px, 110vh);
    }
}
</style>
</head>

<body>

<h1>🎄 Merry Christmas 🎄</h1>

<!-- ===== SVG TREE ===== -->
<svg viewBox="0 0 300 420" onclick="showMessage()">

    <!-- Star -->
    <text id="star" x="150" y="40" text-anchor="middle" font-size="32">⭐</text>

    <!-- Tree outline (TikTok style) -->
    <path id="treePath"
        d="
        M150 380
        L90 280
        L120 280
        L70 180
        L120 180
        L150 100
        L180 180
        L230 180
        L180 280
        L210 280
        Z"
    />
</svg>

<div id="title">✨ Merry Christmas ✨</div>

<div id="message">
💖 Chúc Hương Giang Giáng Sinh vui vẻ,  
thi đâu qua đó, tiền rơi như tuyết ❄️  

— From your bro 💚
</div>

<script>
/* Click hiện lời chúc */
function showMessage() {
    document.getElementById("message").style.display = "block";
}

/* Snow */
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

