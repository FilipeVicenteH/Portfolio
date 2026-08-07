import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
urls = [
    ("http://localhost:3005/clientes", r"c:\Users\User\Desktop\Portfolio\public\projects\unicocrm_clientes_real.jpg"),
    ("http://localhost:3005/relatorios", r"c:\Users\User\Desktop\Portfolio\public\projects\unicocrm_relatorios_real.jpg"),
]

for url, out_img in urls:
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
