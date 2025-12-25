from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🎄 Merry Christmas 🎄</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            font-size: 150px;
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
        /* ===== SANTA ===== */
#santa {
    position: absolute;
    bottom: 40px;
    right: -120px;            /* ban đầu ở ngoài màn hình */
    font-size: 90px;
    opacity: 0;
    transition: right 1.2s ease, opacity 1s ease;
    animation: wave 1s infinite;
    pointer-events: none;
}

#santa.show {
    right: -100px;              /* chạy vào màn hình */
    opacity: 1;
}

@keyframes wave {
    0%   { transform: rotate(0deg); }
    25%  { transform: rotate(8deg); }
    50%  { transform: rotate(0deg); }
    75%  { transform: rotate(-8deg); }
    100% { transform: rotate(0deg); }
}

    </style>
</head>

<body>
    <h1>🎄 Merry Christmas 🎄</h1>
    <p>(Bấm vào cây thông nha 🎁)</p>

    <div class="tree-wrapper">
        <div class="star">⭐</div>
        <div class="tree" onclick="showMessage()">🎄</div>
        <div class="lights">✨ ✨ ✨ ✨ ✨</div>
    </div>

    <div id="message"></div>
    <div id="santa">🎅</div>


    <script>
        const text = `To Hương Giang🐰
        Hi bestie, Merry Christmas! 🎄
Chúc bạn một mùa Giáng Sinh ấm áp, an lành, tràn ngập niềm vui và những khoảnh khắc hạnh phúc nhỏ bé nha.
Mong những ngày tháng khó khăn mệt mỏi sẽ qua đi, và năm mới sẽ chào đón bạn với hy vọng, sức mạnh và nhiều điều tốt đẹp phía trước.🎁

Mình rất biết ơn khi được đồng hành, chia sẻ cùng với bạn cho đến nay!
Chúc bạn may mắn với kỳ thi học phần, hãy bình tĩnh, tin tưởng vào bản thân. Đến được đây bạn đã làm rất tốt rồi.❤️‍🔥

From your partner,
Belgium 💚`;

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
            const santa = document.getElementById("santa");
            santa.classList.add("show");
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

