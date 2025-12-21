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

        .tree {
            font-size: 100px;
            cursor: pointer;
            margin-top: 40px;
        }

        #message {
            display: none;
            margin-top: 20px;
            font-size: 22px;
            color: #ffd700;
            white-space: pre-line;
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
                transform: translateY(110vh);
            }
        }
    </style>
</head>
<body>

<h1>🎄 Merry Christmas 🎄</h1>
<p>(Bấm vào cây thông nha 👇)</p>

<div class="tree" onclick="showMessage()">🎄</div>

<div id="message"></div>

<script>
const text = `💖 Chúc Hương Giang Giáng Sinh vui vẻ,  
thi đâu qua đó, tiền rơi như tuyết ❄️  

— From your bro 💚`;

let index = 0;

function showMessage() {
    const messageDiv = document.getElementById("message");
    messageDiv.style.display = "block";
    messageDiv.innerHTML = "";
    index = 0;

    const typing = setInterval(() => {
        messageDiv.textContent += text[index];
        index++;

        if (index >= text.length) {
            clearInterval(typing);
        }
    }, 50); // tốc độ chữ (ms)
}

function createSnowflake() {
    const snowflake = document.createElement("div");
    snowflake.className = "snowflake";
    snowflake.innerHTML = "❄";
    snowflake.style.left = Math.random() * window.innerWidth + "px";
    snowflake.style.animationDuration = (2 + Math.random() * 3) + "s";
    snowflake.style.fontSize = (10 + Math.random() * 20) + "px";
    document.body.appendChild(snowflake);

    setTimeout(() => snowflake.remove(), 5000);
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


