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
            text-align: center;
            font-family: Arial, sans-serif;
            overflow: hidden;
        }

        h1 {
            margin-top: 20px;
            font-size: 42px;
        }

        .hint {
            opacity: 0.8;
            margin-bottom: 10px;
        }

        /* ===== TREE ===== */
        .tree {
            font-size: 180px; /* PHÓNG TO CÂY */
            cursor: pointer;
            display: inline-block;
            position: relative;
            filter: drop-shadow(0 0 30px rgba(0,255,200,0.6));
            transition: transform 0.3s ease;
        }

        .tree:hover {
            transform: scale(1.05);
        }

        /* ===== STAR ===== */
        .star {
            position: absolute;
            top: -85px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 48px;
            color: gold;
            animation: starGlow 1.5s infinite alternate;
        }

        @keyframes starGlow {
            from { text-shadow: 0 0 10px gold; }
            to { text-shadow: 0 0 35px gold; }
        }

        /* ===== LIGHTS ===== */
        .lights {
            position: absolute;
            inset: 0;
            pointer-events: none;
        }

        .light {
            position: absolute;
            width: 14px;
            height: 14px;
            border-radius: 50%;
            animation: blink 1s infinite alternate;
        }

        @keyframes blink {
            from { opacity: 0.4; }
            to { opacity: 1; }
        }

        /* ===== MESSAGE ===== */
        #message {
            display: none;
            margin-top: 30px;
            font-size: 24px;
            color: #ffd700;
            white-space: pre-line;
            text-shadow: 0 0 12px rgba(255,215,0,0.6);
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
<div class="hint">(Bấm vào cây thông nha 👇)</div>

<div class="tree" onclick="showMessage()">
    <div class="star">⭐</div>
    🎄
    <div class="lights" id="lights"></div>
</div>

<div id="message">
💖 Chúc Hương Giang Giáng Sinh vui vẻ,  
thi đâu qua đó, tiền rơi như tuyết ❄️  

— From your bro 💚
</div>

<script>
/* ===== LIGHT COLORS ===== */
const colors = ["#ff3b3b", "#ffd700", "#00ffcc", "#ff66cc"];

const lightsContainer = document.getElementById("lights");

/* CREATE LIGHTS */
for (let i = 0; i < 14; i++) {
    const light = document.createElement("div");
    light.className = "light";

    light.style.left = Math.random() * 100 + "%";
    light.style.top = Math.random() * 100 + "%";
    light.style.background = colors[Math.floor(Math.random() * colors.length)];
    light.style.animationDuration = (0.5 + Math.random()) + "s";

    lightsContainer.appendChild(light);
}

/* RANDOM COLOR CHANGE */
setInterval(() => {
    document.querySelectorAll(".light").forEach(light => {
        light.style.background = colors[Math.floor(Math.random() * colors.length)];
    });
}, 500);

/* SHOW MESSAGE */
function showMessage() {
    document.getElementById("message").style.display = "block";
}

/* SNOW */
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

setInterval(snow, 180);
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

