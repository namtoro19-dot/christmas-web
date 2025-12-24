from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>🎄 Merry Christmas Hương Giang 🎄</title>
    <style>
        /* CSS Gộp từ cả 2 project */
        body {
            background-color: #0f2027;
            margin: 0;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            height: 100vh;
            font-family: Arial, sans-serif;
        }

        svg.mainSVG {
            width: 100%;
            height: 60vh;
            display: block;
            margin: 0 auto;
            visibility: hidden; /* Sẽ hiện sau khi GSAP load */
        }

        #message {
            margin-top: 20px;
            font-size: 22px;
            color: #ffd700;
            text-align: center;
            white-space: pre-line;
            text-shadow: 0 0 10px rgba(255,215,0,0.6);
            opacity: 0; /* Hiện dần sau khi vẽ cây xong */
            transition: opacity 2s;
        }

        .snowflake {
            position: fixed;
            top: -10px;
            color: white;
            font-size: 16px;
            pointer-events: none;
            animation: fall linear infinite;
        }

        @keyframes fall {
            to { transform: translateY(110vh); }
        }
    </style>
</head>

<body>
    <svg class="mainSVG" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
        <defs>
            <circle id="circ" cx="0" cy="0" r="1" />
            <polygon id="star" points="4.55,0 5.95,2.85 9.1,3.3 6.82,5.52 7.36,8.65 4.55,7.17 1.74,8.65 2.27,5.52 0,3.3 3.14,2.85 " />
        </defs>
        <g class="whole">
            <path class="treePath" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2" 
                d="M400,500 C400,500 200,450 250,350 C300,250 500,250 550,350 C600,450 400,500 400,500 Z M400,400 C400,400 250,370 280,300 C310,230 490,230 520,300 C550,370 400,400 400,400 Z M400,300 C400,300 300,280 320,230 C340,180 460,180 480,230 C500,280 400,300 400,300 Z M400,200 C400,200 340,190 350,150 C360,110 440,110 450,150 C460,190 400,200 400,200 Z" />
            
            <g class="pContainer"></g>
            <text class="treeStar" x="400" y="90" text-anchor="middle" font-size="50" fill="gold">⭐</text>
        </g>
    </svg>

    <div id="message">
        💖 Chúc Hương Giang Giáng Sinh vui vẻ,  
        thi đâu qua đó, tiền rơi như tuyết ❄️  

        — From your bro 💚
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/MotionPathPlugin.min.js"></script>

    <script>
        gsap.registerPlugin(MotionPathPlugin);

        const mainSVG = document.querySelector('.mainSVG');
        const pContainer = document.querySelector('.pContainer');
        const numParticles = 100;

        // Tạo hạt lấp lánh
        function createParticles() {
            for (let i = 0; i < numParticles; i++) {
                let p = document.createElementNS("http://www.w3.org/2000/svg", "use");
                p.setAttributeNS("http://www.w3.org/1999/xlink", "href", "#star");
                p.setAttribute("fill", ["#E8F6F8", "#ACE8F8", "#FFD700", "#5DBA72"][i % 4]);
                pContainer.appendChild(p);
                gsap.set(p, { x: -50, y: -50, scale: gsap.utils.random(0.5, 1.5) });
            }
        }

        function animateTree() {
            gsap.set(mainSVG, { visibility: 'visible' });
            const particles = document.querySelectorAll('.pContainer use');
            
            // Vẽ cây
            const tl = gsap.timeline({
                onComplete: () => {
                    document.getElementById('message').style.opacity = 1;
                }
            });

            particles.forEach((p, i) => {
                tl.to(p, {
                    duration: 4,
                    motionPath: {
                        path: ".treePath",
                        align: ".treePath",
                        autoRotate: true,
                        start: i / numParticles,
                        end: (i / numParticles) + 0.1
                    },
                    repeat: -1,
                    ease: "none",
                    delay: i * 0.02
                }, 0);
            });

            // Ngôi sao hiện ra lấp lánh
            gsap.from(".treeStar", { scale: 0, duration: 2, ease: "elastic.out(1, 0.3)", delay: 1 });
        }

        // Tuyết rơi
        function createSnow() {
            const snow = document.createElement("div");
            snow.className = "snowflake";
            snow.textContent = "❄";
            snow.style.left = Math.random() * 100 + "vw";
            snow.style.animationDuration = (Math.random() * 3 + 2) + "s";
            document.body.appendChild(snow);
            setTimeout(() => snow.remove(), 5000);
        }

        createParticles();
        animateTree();
        setInterval(createSnow, 100);
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

