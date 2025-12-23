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
            cursor: pointer;
        }

        #title {
            font-size: 32px;
            color: gold;
            margin-top: 10px;
            text-shadow: 0 0 15px gold;
            min-height: 40px;
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
                transform: translate(120px, 110vh);
            }
        }
    </style>
</head>
<body>

<h1>🎄 Merry Christmas 🎄</h1>

<canvas id="treeCanvas" width="300" height="420"></canvas>
<div id="title"></div>

<div id="message">
💖 Chúc Hương Giang Giáng Sinh vui vẻ,  
thi đâu qua đó, tiền rơi như tuyết ❄️  

— From your bro 💚
</div>

<script>
const canvas = document.getElementById("treeCanvas");
const ctx = canvas.getContext("2d");

// Các điểm viền cây thông (vẽ như video TikTok)
const path = [
    [150, 380],
    [80, 260], [120, 260],
    [60, 140], [120, 140],
    [150, 60],
    [180, 140], [240, 140],
    [180, 260], [220, 260],
    [150, 380]
];

let progress = 0;
let finished = false;

function drawTree() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.strokeStyle = "#00ffcc";
    ctx.lineWidth = 3;
    ctx.shadowBlur = 15;
    ctx.shadowColor = "#00ffcc";

    ctx.beginPath();
    ctx.moveTo(path[0][0], path[0][1]);

    for (let i = 1; i < progress && i < path.length; i++) {
        ctx.lineTo(path[i][0], path[i][1]);
    }

    ctx.stroke();

    if (progress < path.length) {
        progress += 0.05;
        requestAnimationFrame(drawTree);
    } else if (!finished) {
        drawStar();
        typeTitle();
        finished = true;
    }
}

// Vẽ sao trên đỉnh
function drawStar() {
    ctx.font = "32px Arial";
    ctx.fillStyle = "gold";
    ctx.shadowBlur = 25;
    ctx.shadowColor = "gold";
    ctx.fillText("⭐", 135, 45);
}

// Gõ chữ Merry Christmas
const titleText = "✨ Merry Christmas ✨";
let titleIndex = 0;

function typeTitle() {
    const el = document.getElementById("title");
    const typing = setInterval(() => {
        el.textContent += titleText[titleIndex];
        titleIndex++;
        if (titleIndex >= titleText.length) clearInterval(typing);
    }, 80);
}

// Click cây → hiện lời chúc
canvas.addEventListener("click", () => {
    if (!finished) return;
    document.getElementById("message").style.display = "block";
});

// Tuyết bay
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

// Start animation
drawTree();
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
