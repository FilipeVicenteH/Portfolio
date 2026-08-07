import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
dist_html = r"C:\Users\User\Desktop\Portfolio\scratch_repos\Analise-de-Dados-Unico\dist\index.html"
out_img = r"c:\Users\User\Desktop\Portfolio\public\projects\analise_dados_real.jpg"

url = f"file:///{dist_html.replace('\\', '/')}"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1440,900",
    f"--screenshot={out_img}",
    url
]
subprocess.run(cmd)
print(f"Captured: {out_img} -> Exists: {os.path.exists(out_img)}")
