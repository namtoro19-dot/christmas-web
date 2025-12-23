from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>🎄 Merry Christmas 🎄</title>

<style>
body {
    margin: 0;
    height: 100vh;
    background: linear-gradient(#0f2027, #203a43, #2c5364);
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
    overflow: hidden;
}

h1 {
    margin-top: 20px;
}

svg {
    display: block;
    margin: 0 auto;
}

#treePath {
    fill: none;
    stroke: #00ffcc;
    stroke-width: 4;
    stroke-linecap: round;
    stroke-linejoin: round;
    filter: drop-shadow(0 0 10px #00ffcc);
    stroke-dasharray: 1200;
    stroke-dashoffset: 1200;
    animation: drawTree 4s ease-out forwards;
}

@keyframes drawTree {
    to { stroke-dashoffset: 0; }
}

#star {
    opacity: 0;
    filter: drop-shadow(0 0 20px gold);
    animation: showStar 1s ease forwards;
    animation-delay: 4s;
}

@keyframes showStar {
    to { opacity: 1; }
}

#title {
    margin-top: 10px;
    font-size: 32px;
    color: gold;
    text-shadow: 0 0 15px gold;
    min-height: 40px;
}

#message {
    display: none;
    margin-top: 20px;
    font-size: 22px;
    color: #ffd700;
    white-space: pre-line;
    text-shadow: 0 0 10px rgba(255,215,0,.6);
}

/* Snow */
.snowflake {
    position: absolute;
    top: -10px;
    color: white;
    animation: fall linear infinite;
}

@keyframes fall {
    to { transform: translate(120px, 110vh); }
}
</style>
</head>

<body>

<h1>🎄 Merry Christmas 🎄</h1>

<svg width="300" height="420" viewBox="0 0 300 420">
    <!-- CÂY THÔNG -->
    <path id="treePath"
        d="M150 380
           L90 260
           L120 260
           L70 140
           L120 140
           L150 60
           L180 140
           L230 140
           L180 260
           L210 260
           Z" />

    <!-- SAO -->
    <text id="star" x="150" y="45" text-anchor="middle" font-size="32">⭐</text>
</svg>

<div id="title"></div>

<div id="message">
💖 Chúc Hương Giang Giáng Sinh vui vẻ,  
thi đâu qua đó, tiền rơi như tuyết ❄️  

— From your bro 💚
</div>

<script>
// Typing title
const titleText = "✨ Merry Christmas ✨";
let i = 0;
const titleEl = document.getElementById("title");

setTimeout(() => {
    const typing = setInterval(() => {
        titleEl.textContent += titleText[i];
        i++;
        if (i >= titleText.length) clearInterval(typing);
    }, 80);
}, 4200);

// Click show message
document.querySelector("svg").addEventListener("click", () => {
    document.getElementById("message").style.display = "block";
});

// Snow
function snow() {
    const s = document.createElement("div");
    s.className = "snowflake";
    s.textContent = "❄";
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

