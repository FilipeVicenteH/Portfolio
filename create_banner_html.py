import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap');
  
  * { box-sizing: border-box; margin: 0; padding: 0; }
  
  body {
    width: 1584px;
    height: 396px;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    font-family: 'Inter', sans-serif;
    color: #ffffff;
    display: flex;
    align-items: center;
    position: relative;
    overflow: hidden;
  }

  /* Decorative Grid Pattern */
  .grid-pattern {
    position: absolute;
    right: 0;
    top: 0;
    width: 70%;
    height: 100%;
    background-image: 
      linear-gradient(to right, rgba(255,255,255,0.03) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 32px 32px;
    mask-image: linear-gradient(to right, transparent 0%, black 30%);
    -webkit-mask-image: linear-gradient(to right, transparent 0%, black 30%);
  }

  /* Glowing ambient shapes */
  .glow-1 {
    position: absolute;
    right: 10%;
    top: -20%;
    width: 450px;
    height: 450px;
    background: radial-gradient(circle, rgba(13, 148, 136, 0.18) 0%, transparent 70%);
    border-radius: 50%;
  }

  .glow-2 {
    position: absolute;
    right: 35%;
    bottom: -30%;
    width: 350px;
    height: 350px;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.12) 0%, transparent 70%);
    border-radius: 50%;
  }

  /* Main Content Container (Shifted right to avoid Avatar overlap) */
  .content {
    margin-left: 520px;
    z-index: 10;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  .header-name {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #ffffff;
    line-height: 1;
  }

  .header-tagline {
    font-size: 20px;
    font-weight: 600;
    color: #14b8a6;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .badges {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 2px;
  }

  .badge {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(8px);
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 500;
    color: #e2e8f0;
  }

  .badge-highlight {
    background: rgba(13, 148, 136, 0.15);
    border-color: rgba(20, 184, 166, 0.3);
    color: #2dd4bf;
  }

  .footer-contact {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-top: 6px;
    padding-top: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    font-size: 14px;
    color: #94a3b8;
    font-family: 'JetBrains Mono', monospace;
  }

  .contact-item {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .contact-item svg {
    color: #14b8a6;
  }
</style>
</head>
<body>
  <div class="grid-pattern"></div>
  <div class="glow-1"></div>
  <div class="glow-2"></div>

  <div class="content">
    <div class="header-name">Filipe Vicente Hidalgo</div>
    
    <div class="header-tagline">
      <span>Front-End Developer</span>
      <span style="opacity: 0.4">•</span>
      <span>Suporte Técnico N1/N2</span>
      <span style="opacity: 0.4">•</span>
      <span>Customer Success</span>
    </div>

    <div class="badges">
      <span class="badge badge-highlight">React</span>
      <span class="badge badge-highlight">JavaScript</span>
      <span class="badge">APIs & Webhooks</span>
      <span class="badge">Power BI</span>
      <span class="badge">Troubleshooting</span>
      <span class="badge">UI/UX Design</span>
    </div>

    <div class="footer-contact">
      <div class="contact-item">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
        <span>filipevicenteh.vercel.app</span>
      </div>
      <span style="opacity: 0.3">•</span>
      <div class="contact-item">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        <span>filipe_vicente@hotmail.com</span>
      </div>
      <span style="opacity: 0.3">•</span>
      <div class="contact-item">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <span>(11) 96615-2956</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

html_path = r"C:\Users\User\Desktop\Portfolio\banner.html"
png_path = r"C:\Users\User\Desktop\linkedin_banner_filipe.png"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--window-size=1584,396",
    f"--screenshot={png_path}",
    html_path
]

subprocess.run(chrome_cmd)
print(f"Rendered banner to {png_path}")
