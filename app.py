from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <!-- ✅ QUAN TRỌNG: FIX GIẬT / THU NHỎ TRÊN ĐIỆN THOẠI -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <title>🎄 Merry Christmas 🎄</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: linear-gradient(#0f2027, #203a43, #2c5364);
            color: white;
            font-family: Arial, sans-serif;
            overflow: hidden;

            display: flex;
            flex-direction: column;
            align-items: center;
        }

        h1 {
            margin-top: 16px;
            font-size: 1.8rem;
        }

        p {
            margin: 4px 0 10px;
            font-size: 0.9rem;
            opacity: 0.85;
        }

        /* ===== CÂY THÔNG ===== */
        .tree-wrapper {
            position: relative;
            margin-top: 20px;
        }

        .star {
            position: absolute;
            top: -40px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 36px;
            color: gold;
            animation: glow 1.5s infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 6px gold; }
            to { text-shadow: 0 0 22px gold; }
        }

        .tree {
            font-size: min(48vw, 200px); /* ✅ tự co theo màn hình */
            cursor: pointer;
            filter: drop-shadow(0 0 30px rgba(0,255,200,0.7));
            transition: transform 0.25s ease;
            user-select: none;
        }

        .tree:active {
            transform: scale(1.05);
        }

        /* ===== ĐÈN ===== */
        .lights {
            font-size: 22px;
            margin-top: 8px;
            animation: blink 1s infinite alternate;
        }

        @keyframes blink {
            from { opacity: 0.4; }
            to { opacity: 1; }
        }

        /* ===== LỜI CHÚC ===== */
        #message {
            display: none;
            margin: 18px 16px 0;
            font-size: 1rem;
            line-height: 1.45;
            color: #ffd700;
            white-space: pre-line;
            text-shadow: 0 0 8px rgba(255,215,0,0.6);
            max-width: 520px;
        }

        /* ===== TUYẾT ===== */
        .snowflake {
            position: fixed;
            top: -10px;
            color: white;
            pointer-events: none;
            animation: fall linear forwards;
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
    <p>(Tap the tree 🎁)</p>

    <div class="tree-wrapper">
        <div class="star">⭐</div>
        <div class="tree" onclick="showMessage()">🎄</div>
        <div class="lights">✨ ✨ ✨ ✨ ✨</div>
    </div>

    <div id="message"></div>

    <script>
        const text = `To Huong Giang 🐰
Hi bestie, Merry Christmas! 🎄
Wishing you a warm, peaceful Christmas filled with joy and small happy moments.
May the last days of this year be gentle to you, and may the new year welcome you with hope, strength, and many good things ahead. 🎁

I’m really thankful for everything we’ve shared so far.
And good luck with your exams — stay calm, stay confident, and trust yourself. You’ve already done so well. ❤️‍🔥

From your best friend,
Belgium 💚`;

        let index = 0;
        let typing = null;

        function showMessage() {
            const messageDiv = document.getElementById("message");
            messageDiv.style.display = "block";
            messageDiv.innerHTML = "";
            index = 0;

            if (typing) clearInterval(typing);

            typing = setInterval(() => {
                messageDiv.innerHTML += text[index];
                index++;
                if (index >= text.length) clearInterval(typing);
            }, 45);
        }

        /* ===== TUYẾT (FIX MOBILE) ===== */
        function createSnowflake() {
            const s = document.createElement("div");
            s.className = "snowflake";
            s.innerHTML = "❄";
            s.style.left = Math.random() * window.innerWidth + "px";
            s.style.fontSize = (10 + Math.random() * 16) + "px";
            s.style.animationDuration = (4 + Math.random() * 3) + "s";
            document.body.appendChild(s);

            setTimeout(() => s.remove(), 8000);
        }

        setInterval(createSnowflake, 250);
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


