import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_files = [
    (r"C:\Users\User\Desktop\Portfolio\scratch_repos\Telas-Unico\Ecommerce_Pedidos\DashBoard Completo.html", r"c:\Users\User\Desktop\Portfolio\public\projects\telas_dashboard_real.jpg"),
    (r"C:\Users\User\Desktop\Portfolio\scratch_repos\Telas-Unico\Ecommerce_Pedidos\Ranking de Produtos.html", r"c:\Users\User\Desktop\Portfolio\public\projects\telas_ranking_real.jpg"),
    (r"C:\Users\User\Desktop\Portfolio\scratch_repos\Telas-Unico\Ecommerce_Pedidos\Lista de Rastreio.html", r"c:\Users\User\Desktop\Portfolio\public\projects\telas_rastreio_real.jpg"),
]

for html_p, out_p in html_files:
    if os.path.exists(html_p):
        url = f"file:///{html_p.replace('\\', '/')}"
        cmd = [
            chrome_path,
            "--headless=new",
            "--disable-gpu",
            "--window-size=1440,900",
            f"--screenshot={out_p}",
            url
        ]
        subprocess.run(cmd)
        print(f"Captured: {out_p} -> Exists: {os.path.exists(out_p)}")
