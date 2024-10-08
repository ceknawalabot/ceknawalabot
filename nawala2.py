import os
import time
from datetime import datetime

import git
import pytz
import requests

# Step 1: Read the list of keywords from list.txt
with open('list.txt', 'r') as f:
    keywords = [line.strip() for line in f.readlines()]

# Step 2: Fetch the data from the URL
url = 'https://raw.githubusercontent.com/Skiddle-ID/blocklist/main/domains'
response = requests.get(url)
data = response.text

# Step 3: Parse the data from the URL
domains = data.splitlines()

# Step 4: Check if the keyword is in the list of domains
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Nawala bot (Trust Positif Checker)")

    # Inisialisasi index_html di sini
    index_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nawala Bot - Trust Positif Checker</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
            body {
                background-color: #f8f9fa;
            }
            h1 {
                color: #343a40;
            }
            .blocked {
                color: red;
            }
            .not-blocked {
                color: green;
            }
        </style>
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="text-center">Nawala Bot Empire Group(Trust Positif Checker)</h1>
            <ul class="list-group mt-4">
    """

    # Proxy providers
    providers = {
        "by.u": "http://z35HIuGaVkMdOwMw:mobile;id;by.u;jakarta;jakarta@proxy.soax.com:9000",
        "indosat": "http://z35HIuGaVkMdOwMw:mobile;id;indosat;jakarta;jakarta@proxy.soax.com:9000",
        "smartfren": "http://z35HIuGaVkMdOwMw:mobile;id;smartfren;jakarta;jakarta@proxy.soax.com:9000",
        "telkomsel": "http://z35HIuGaVkMdOwMw:mobile;id;telkomsel;jakarta;jakarta@proxy.soax.com:9000",
        "xl axiata": "http://z35HIuGaVkMdOwMw:mobile;id;xl+axiata;jakarta;jakarta@proxy.soax.com:9000"
    }

    # Function to check domain with proxy
    def check_domain_with_proxy(domain, provider):
        proxy = providers.get(provider)
        if proxy:
            try:
                # Add the scheme (https) to the domain
                full_url = f"https://{domain}"
                response = requests.get(full_url, proxies={"http": proxy, "https": proxy}
                , timeout=10)
                print(f"Domain: {domain}, Provider: {provider}, Status : \033[92mNot Blocked\033[0m")
                # Log the response status code for debugging
                return response.status_code == 200
            except Exception as e:
                print(f"{domain} with {provider}: \033[91mBlocked\033[0m")
                return False
        else:
            return False
    # Check each keyword with each proxy provider
    for keyword in keywords:
        if keyword in domains:
            index_html += f'<li class="list-group-item list-group-item-danger">{keyword}: <span class="blocked">Blocked</span></li>'
            print(f"{keyword}: \033[91mBlocked\033[0m")
        else:
            print(f"{keyword}: \033[92mNot Blocked\033[0m")

        # Display proxy check results in a table
        index_html += f"""
            <div class="mt-4">
                <h4 class="text-center">{keyword}</h4>
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>Provider</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
        """

        for provider_name, proxy_url in providers.items():
            is_blocked = check_domain_with_proxy(keyword, provider_name)
            status = "Blocked" if not is_blocked else "Not-Blocked"
            index_html += f"""
                            <tr>
                                <td>{provider_name}</td>
                                <td><span class="{status.lower()}">{status}</span></td>
                            </tr>
            """

        index_html += """
                    </tbody>
                </table>
            </div>
        """

    # Mengatur zona waktu Jepang
    japan_tz = pytz.timezone('Asia/Tokyo')

    # Mendapatkan waktu saat ini di zona waktu Jepang
    japan_time = datetime.now(japan_tz)

    # Menampilkan waktu
    print("Waktu di Jepang:", japan_time.strftime('%Y-%m-%d %H:%M:%S'))

    # Mendapatkan waktu saat ini dengan zona waktu lokal
    local_tz = pytz.timezone('Asia/Jakarta')
    local_time = datetime.now(local_tz)
    local_time_with_tz = local_time.strftime('%Y-%m-%d %H:%M:%S') + ' WIB'

    # Mendapatkan waktu saat ini dengan zona waktu Jepang
    japan_time = datetime.now(japan_tz)
    japan_time_with_tz = f"{japan_time.strftime('%Y-%m-%d %H:%M:%S')} JST"  # Format waktu Jepang

    print(
        f"Last update checked: {local_time_with_tz} (WIB), {japan_time_with_tz} (JST)"
    )
    index_html += f"""
            </ul>
            <p class="text-center mt-4">Last update checked: {local_time_with_tz} (WIB), {japan_time_with_tz} (JST)</p>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    """

    # Simpan index ke file HTML
    with open('index.html', 'w') as f:
        f.write(index_html)

    # Push ke GitHub
    repo = git.Repo('.')  # Inisialisasi repository
    repo = repo.git.config('github.token','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')
    repo.index.add(['index.html'])  # Tambahkan file index.html ke staging
    repo.index.commit('Update index.html')  # Commit perubahan
    repo.git.push('--set-upstream', 'origin', 'main')  # Setelah commit
    origin = repo.remote(name='origin')  # Ambil remote origin
    origin.push()  # Push ke GitHub

    time.sleep(1800)  # Tunggu selama 5 menit (300 detik)
