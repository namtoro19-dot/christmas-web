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

        /* ===== CÂY THÔNG ===== */
        .tree-wrapper {
            position: relative;
            margin-top: 40px;
            display: inline-block;
        }

        .star {
            position: absolute;
            top: -35px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 30px;
            color: gold;
            animation: glow 1.5s infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 5px gold; }
            to { text-shadow: 0 0 20px gold; }
        }

        .tree {
            font-size: 180px;
            cursor: pointer;
            filter: drop-shadow(0 0 25px rgba(0,255,200,0.6));
            transition: transform 0.3s ease, text-shadow 0.3s ease;
        }

        .tree:hover {
            transform: scale(1.1) rotate(-2deg);
            text-shadow: 0 0 25px #00ffcc;
        }

        .tree.clicked {
            animation: shake 0.4s;
        }

        @keyframes shake {
            0% { transform: rotate(0deg); }
            25% { transform: rotate(-5deg); }
            50% { transform: rotate(5deg); }
            75% { transform: rotate(-5deg); }
            100% { transform: rotate(0deg); }
        }

        /* ===== ĐÈN ===== */
        .lights {
            font-size: 26px;
            margin-top: 10px;
            animation: blink 1s infinite alternate;
        }

        @keyframes blink {
            from { opacity: 0.3; }
            to { opacity: 1; }
        }

        /* ===== LỜI CHÚC ===== */
        #message {
            display: none;
            margin-top: 25px;
            font-size: 22px;
            color: #ffd700;
            white-space: pre-line;
            text-shadow: 0 0 10px rgba(255,215,0,0.6);
        }

        /* ===== TUYẾT ===== */
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
    <p>(Bấm vào cây thông nha 👇)</p>

    <div class="tree-wrapper">
        <div class="star">⭐</div>
        <div class="tree" onclick="showMessage()">🎄</div>
        <div class="lights">✨ ✨ ✨ ✨ ✨</div>
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

