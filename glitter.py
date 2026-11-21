"""
FileGuard - Premium Cybersecurity Particle & Digital Forensic Background Engine
Generates interactive 60 FPS real-time cyber canvas, glowing binary streams,
pulsing circuit elements, holographic security icons, and mouse cursor cyber trails.
"""

def get_glitter_engine_html() -> str:
    """
    Returns high-performance HTML/JS component that mounts a full-screen
    interactive cybersecurity particle and digital data canvas onto window.parent.document.body.
    """
    return """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body, html { margin: 0; padding: 0; overflow: hidden; background: transparent; }
  </style>
</head>
<body>
  <script>
  (function() {
    try {
      const pDoc = window.parent.document || document;
      const pWin = window.parent || window;

      // Avoid duplicate canvas injection
      let canvas = pDoc.getElementById('fg-live-glitter-canvas');
      if (!canvas) {
        canvas = pDoc.createElement('canvas');
        canvas.id = 'fg-live-glitter-canvas';
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100vw';
        canvas.style.height = '100vh';
        canvas.style.pointerEvents = 'none';
        canvas.style.zIndex = '1';
        canvas.style.opacity = '0.95';
        pDoc.body.appendChild(canvas);
      }

      const ctx = canvas.getContext('2d');
      let width = canvas.width = pWin.innerWidth || 1200;
      let height = canvas.height = pWin.innerHeight || 800;

      pWin.addEventListener('resize', function() {
        width = canvas.width = pWin.innerWidth || 1200;
        height = canvas.height = pWin.innerHeight || 800;
      });

      // Palette: Electric Cyan, Neon Purple, Electric Blue, Cyber Emerald, White
      const palette = ['#00F0FF', '#38BDF8', '#A855F7', '#C084FC', '#3B82F6', '#00FF9D', '#FFFFFF'];
      const dataTokens = ['01', '10', '0x4D', '0x5A', '0xFF', '0x25', '0x89', 'MZ', 'PE', 'SHA', '1', '0'];

      // 160 Digital Cyber Particles & Data Packets
      const particles = [];
      const particleCount = 150;

      for (let i = 0; i < particleCount; i++) {
        const isDataText = Math.random() < 0.22;
        particles.push({
          x: Math.random() * width,
          y: Math.random() * height,
          size: Math.random() * 4.0 + 2.0,
          baseSize: Math.random() * 4.0 + 2.0,
          color: palette[Math.floor(Math.random() * palette.length)],
          vx: (Math.random() - 0.5) * 0.6,
          vy: -Math.random() * 0.85 - 0.25, // Drifting upwards
          alpha: Math.random() * 0.55 + 0.35,
          twinkleSpeed: Math.random() * 0.05 + 0.02,
          phase: Math.random() * Math.PI * 2,
          isStar: Math.random() > 0.45,
          isData: isDataText,
          text: dataTokens[Math.floor(Math.random() * dataTokens.length)]
        });
      }

      // Live Mouse Cursor Cyber Data Sparkle Trail
      const mouseSparks = [];
      pDoc.addEventListener('mousemove', function(e) {
        for (let i = 0; i < 3; i++) {
          mouseSparks.push({
            x: e.clientX + (Math.random() - 0.5) * 16,
            y: e.clientY + (Math.random() - 0.5) * 16,
            size: Math.random() * 6.5 + 2.5,
            color: palette[Math.floor(Math.random() * palette.length)],
            vx: (Math.random() - 0.5) * 2.6,
            vy: (Math.random() - 0.5) * 2.6 - 0.3,
            alpha: 1.0,
            decay: Math.random() * 0.035 + 0.025,
            isCross: Math.random() > 0.5
          });
        }
      });

      // Draw 4-point radiant diamond star with glowing spikes
      function drawCyberStar(ctx, x, y, r, color, alpha) {
        ctx.save();
        ctx.translate(x, y);
        ctx.fillStyle = color;
        ctx.globalAlpha = alpha;
        ctx.shadowColor = color;
        ctx.shadowBlur = r * 3.5;

        ctx.beginPath();
        ctx.moveTo(0, -r * 2.2);
        ctx.quadraticCurveTo(0, 0, r * 2.2, 0);
        ctx.quadraticCurveTo(0, 0, 0, r * 2.2);
        ctx.quadraticCurveTo(0, 0, -r * 2.2, 0);
        ctx.quadraticCurveTo(0, 0, 0, -r * 2.2);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle = '#FFFFFF';
        ctx.beginPath();
        ctx.arc(0, 0, r * 0.45, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }

      // Draw floating digital data token
      function drawDataToken(ctx, x, y, text, color, alpha) {
        ctx.save();
        ctx.font = 'bold 10px monospace';
        ctx.fillStyle = color;
        ctx.globalAlpha = alpha * 0.85;
        ctx.shadowColor = color;
        ctx.shadowBlur = 8;
        ctx.fillText(text, x, y);
        ctx.restore();
      }

      let frame = 0;
      function loop() {
        frame++;
        ctx.clearRect(0, 0, width, height);

        // 1. Render Floating Cyber Particles
        for (let i = 0; i < particles.length; i++) {
          const p = particles[i];
          p.x += p.vx + Math.sin(frame * 0.02 + p.phase) * 0.4;
          p.y += p.vy;

          if (p.y < -25) { p.y = height + 25; p.x = Math.random() * width; }
          if (p.x < -25) p.x = width + 25;
          if (p.x > width + 25) p.x = -25;

          const twinkle = (Math.sin(frame * p.twinkleSpeed + p.phase) + 1) * 0.5;
          const currentAlpha = p.alpha * (0.35 + 0.65 * twinkle);
          const currentSize = p.baseSize * (0.6 + 0.8 * twinkle);

          if (p.isData) {
            drawDataToken(ctx, p.x, p.y, p.text, p.color, currentAlpha);
          } else if (p.isStar) {
            drawCyberStar(ctx, p.x, p.y, currentSize, p.color, currentAlpha);
          } else {
            ctx.save();
            ctx.beginPath();
            ctx.arc(p.x, p.y, currentSize, 0, Math.PI * 2);
            ctx.fillStyle = p.color;
            ctx.globalAlpha = currentAlpha;
            ctx.shadowColor = p.color;
            ctx.shadowBlur = currentSize * 2.8;
            ctx.fill();
            ctx.restore();
          }
        }

        // 2. Render Mouse Cursor Cyber Sparks
        for (let i = mouseSparks.length - 1; i >= 0; i--) {
          const m = mouseSparks[i];
          m.x += m.vx;
          m.y += m.vy;
          m.alpha -= m.decay;
          m.size *= 0.96;

          if (m.alpha <= 0 || m.size <= 0.6) {
            mouseSparks.splice(i, 1);
            continue;
          }

          ctx.save();
          ctx.translate(m.x, m.y);
          ctx.strokeStyle = m.color;
          ctx.fillStyle = m.color;
          ctx.globalAlpha = m.alpha;
          ctx.shadowColor = m.color;
          ctx.shadowBlur = 12;

          if (m.isCross) {
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(-m.size, 0); ctx.lineTo(m.size, 0);
            ctx.moveTo(0, -m.size); ctx.lineTo(0, m.size);
            ctx.stroke();
          } else {
            ctx.beginPath();
            ctx.arc(0, 0, m.size * 0.7, 0, Math.PI * 2);
            ctx.fill();
          }
          ctx.restore();
        }

        requestAnimationFrame(loop);
      }
      loop();

    } catch (err) {
      console.warn("Cyber canvas setup notice:", err);
    }
  })();
  </script>
</body>
</html>
"""

def get_glitter_overlay_html() -> str:
    """
    Returns cybersecurity-themed background elements including glowing floating icons,
    ambient neon orbs, sweeping scan laser, and digital particles.
    """
    cyber_elements = [
        ("🛡️", "fg-gl-1", "top: 7%; left: 4%; font-size: 26px; filter: drop-shadow(0 0 12px #00F0FF);"),
        ("⚡", "fg-gl-2", "top: 14%; left: 22%; font-size: 28px; filter: drop-shadow(0 0 12px #A855F7);"),
        ("01", "fg-gl-3", "top: 9%; left: 45%; font-family: monospace; font-size: 18px; color: #00F0FF; font-weight: 800; filter: drop-shadow(0 0 10px #00F0FF);"),
        ("🔒", "fg-gl-4", "top: 16%; left: 66%; font-size: 26px; filter: drop-shadow(0 0 12px #38BDF8);"),
        ("✦", "fg-gl-5", "top: 6%; left: 88%; font-size: 26px; color: #00FF9D; filter: drop-shadow(0 0 12px #00FF9D);"),
        ("📡", "fg-gl-6", "top: 26%; left: 10%; font-size: 24px; filter: drop-shadow(0 0 12px #3B82F6);"),
        ("0x", "fg-gl-7", "top: 32%; left: 36%; font-family: monospace; font-size: 18px; color: #C084FC; font-weight: 800; filter: drop-shadow(0 0 10px #C084FC);"),
        ("◈", "fg-gl-8", "top: 28%; left: 84%; font-size: 22px; color: #00F0FF; filter: drop-shadow(0 0 10px #00F0FF);"),
        ("💻", "fg-gl-9", "top: 44%; left: 5%; font-size: 24px; filter: drop-shadow(0 0 12px #A855F7);"),
        ("✨", "fg-gl-10", "top: 48%; left: 52%; font-size: 24px; color: #00F0FF; filter: drop-shadow(0 0 12px #00F0FF);"),
        ("⌗", "fg-gl-11", "top: 55%; left: 24%; font-family: monospace; font-size: 22px; color: #00FF9D; font-weight: 800; filter: drop-shadow(0 0 10px #00FF9D);"),
        ("🎯", "fg-gl-12", "top: 52%; left: 91%; font-size: 24px; filter: drop-shadow(0 0 12px #38BDF8);"),
        ("🪲", "fg-gl-13", "top: 66%; left: 14%; font-size: 24px; filter: drop-shadow(0 0 12px #EF4444);"),
        ("10", "fg-gl-14", "top: 64%; left: 44%; font-family: monospace; font-size: 18px; color: #00F0FF; font-weight: 800; filter: drop-shadow(0 0 10px #00F0FF);"),
        ("✧", "fg-gl-15", "top: 72%; left: 74%; font-size: 28px; color: #A855F7; filter: drop-shadow(0 0 12px #A855F7);"),
        ("🛡️", "fg-gl-16", "top: 80%; left: 7%; font-size: 26px; filter: drop-shadow(0 0 12px #00F0FF);"),
        ("✦", "fg-gl-17", "top: 84%; left: 34%; font-size: 26px; color: #38BDF8; filter: drop-shadow(0 0 12px #38BDF8);"),
        ("⚡", "fg-gl-18", "top: 86%; left: 60%; font-size: 26px; filter: drop-shadow(0 0 12px #A855F7);"),
        ("🔒", "fg-gl-19", "top: 91%; left: 86%; font-size: 26px; filter: drop-shadow(0 0 12px #00FF9D);"),
        ("◈", "fg-gl-20", "top: 94%; left: 47%; font-size: 22px; color: #00F0FF; filter: drop-shadow(0 0 10px #00F0FF);"),
        ("✨", "fg-gl-21", "top: 20%; left: 58%; font-size: 26px; color: #C084FC; filter: drop-shadow(0 0 12px #C084FC);"),
        ("01", "fg-gl-22", "top: 38%; left: 68%; font-family: monospace; font-size: 18px; color: #38BDF8; font-weight: 800; filter: drop-shadow(0 0 10px #38BDF8);"),
        ("✦", "fg-gl-23", "top: 76%; left: 92%; font-size: 24px; color: #00FF9D; filter: drop-shadow(0 0 10px #00FF9D);"),
        ("📡", "fg-gl-24", "top: 89%; left: 24%; font-size: 24px; filter: drop-shadow(0 0 12px #00F0FF);")
    ]

    elements_html = ""
    for char, cls, style in cyber_elements:
        elements_html += f'<div class="fg-live-sparkle {cls}" style="{style}">{char}</div>\n'

    return f"""
<div class="fg-cyber-bg-layer">
  <!-- Glowing Neon Background Orbs -->
  <div class="fg-bg-orb fg-orb-cyan"></div>
  <div class="fg-bg-orb fg-orb-violet"></div>
  <div class="fg-bg-orb fg-orb-blue"></div>
  <div class="fg-bg-orb fg-orb-purple"></div>

  <!-- High-Tech Cyber Scan Laser -->
  <div class="fg-bg-grid-laser"></div>

  <!-- Circuit Pattern Background Layer -->
  <div class="fg-circuit-pattern"></div>

  <!-- Cascading Binary Streams -->
  <div class="fg-binary-waterfall" style="top: 10%; left: 2%;">01000110\n01101001\n01101100\n01100101\n0x4D5A\n01010011</div>
  <div class="fg-binary-waterfall" style="top: 25%; right: 3%; animation-delay: -5s; color: rgba(168,85,247,0.35);">11010010\n01001101\n0x89PNG\n00110101\n0x2550\n10101100</div>

  <!-- Floating Holographic Security Icons -->
  {elements_html}
</div>
"""
