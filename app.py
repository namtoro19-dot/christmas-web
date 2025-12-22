from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
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

        canvas {
            display: block;
            margin: 0 auto;
        }

        #typingTitle {
            font-size: 32px;
            margin-top: 10px;
            color: gold;
            text-shadow: 0 0 15px gold;
            height: 40px;
        }

        #message {
            display: none;
            margin-top: 25px;
            font-size: 22px;
            color: #ffd700;
            white-space: pre-line;
            text-shadow: 0 0 10px rgba(255,215,0,0.6);
        }

        .snowflake {
            position: absolute;
            top: -10px;
            color: white;
            font-size: 16px;
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

<canvas id="treeCanvas" width="300" height="400"></canvas>
<div id="typingTitle"></div>

<div id="message">
💖 Chúc Hương Giang Giáng Sinh vui vẻ,  
thi đâu qua đó, tiền rơi như tuyết ❄️  

— From your bro 💚
</div>

<script>
const canvas = document.getElementById("treeCanvas");
const ctx = canvas.getContext("2d");

let t = 0;
let drawing = true;

// Vẽ cây thông bằng đường zigzag
function drawTree() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = "#00ffcc";
    ctx.lineWidth = 2;
    ctx.shadowBlur = 10;
    ctx.shadowColor = "#00ffcc";

    ctx.beginPath();
    ctx.moveTo(150, 350);

    for (let y = 350; y > 50; y -= 10) {
        let x = 150 + Math.sin((350 - y + t) * 0.1) * (350 - y) * 0.08;
        ctx.lineTo(x, y);
    }

    ctx.stroke();

    t += 2;
    if (t < 300) {
        requestAnimationFrame(drawTree);
    } else {
        drawStar();
        typeTitle();
        document.getElementById("message").style.display = "block";
    }
}

// Vẽ ngôi sao
function drawStar() {
    ctx.fillStyle = "gold";
    ctx.shadowBlur = 20;
    ctx.shadowColor = "gold";
    ctx.font = "30px Arial";
    ctx.fillText("⭐", 135, 40);
}

// Gõ chữ Merry Christmas
const titleText = "✨ Merry Christmas ✨";
let titleIndex = 0;

function typeTitle() {
    const el = document.getElementById("typingTitle");
    const typing = setInterval(() => {
        el.textContent += titleText[titleIndex];
        titleIndex++;
        if (titleIndex >= titleText.length) clearInterval(typing);
    }, 80);
}

// Tuyết
function createSnowflake() {
    const snowflake = document.createElement("div");
    snowflake.className = "snowflake";
    snowflake.innerHTML = "❄";
    snowflake.style.left = Math.random() * window.innerWidth + "px";
    snowflake.style.animationDuration = (3 + Math.random() * 3) + "s";
    snowflake.style.fontSize = (10 + Math.random() * 20) + "px";
    document.body.appendChild(snowflake);

    setTimeout(() => snowflake.remove(), 6000);
}

setInterval(createSnowflake, 200);

// Bắt đầu vẽ khi load
drawTree();
</script>

</body>
</html>

<body>
    <h1>🎄 Merry Christmas 🎄</h1>
    <p>(Bấm vào cây thông nha 👇)</p>

    <div class="tree-wrapper">
        <div class="star">⭐</div>
        <div class="tree-wrapper" onclick="showMessage()">

<svg width="300" height="420" viewBox="0 0 300 420">
    <!-- Cây thông -->
    <path id="treePath"
        d="M150 20
           L90 140
           L120 140
           L70 260
           L110 260
           L50 380
           L250 380
           L190 260
           L230 260
           L180 140
           L210 140
           Z"
        fill="none"
        stroke="#00ffcc"
        stroke-width="4"
        stroke-linecap="round"
    />

    <!-- Ngôi sao -->
    <text id="star" x="150" y="35" text-anchor="middle" font-size="32">⭐</text>
</svg>

<div id="title">Merry Christmas 🎄</div>

</div>

    </div>

    <div id="message"></div>

    <script>
        const text = `💖 Chúc Hương Giang Giáng Sinh vui vẻ,
thi đâu qua đó, tiền rơi như tuyết ❄️

— From your bro 💚`;

        let index = 0;
        let typing = null;

        function showMessage() {
            const tree = document.querySelector(".tree");
            tree.classList.add("clicked");
            setTimeout(() => tree.classList.remove("clicked"), 400);

            const messageDiv = document.getElementById("message");
            messageDiv.style.display = "block";
            messageDiv.innerHTML = "";
            index = 0;

            if (typing) clearInterval(typing);

            typing = setInterval(() => {
                messageDiv.innerHTML += text[index];
                index++;
                if (index >= text.length) clearInterval(typing);
            }, 50);
        }

        function createSnowflake() {
            const snowflake = document.createElement("div");
            snowflake.className = "snowflake";
            snowflake.innerHTML = "❄";
            snowflake.style.left = Math.random() * window.innerWidth + "px";
            snowflake.style.animationDuration = (3 + Math.random() * 3) + "s";
            snowflake.style.fontSize = (10 + Math.random() * 20) + "px";
            document.body.appendChild(snowflake);

            setTimeout(() => snowflake.remove(), 6000);
        }

        setInterval(createSnowflake, 200);
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


