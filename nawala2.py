import requests
import time  # Tambahkan import ini
import os
import git  # Tambahkan import ini
import pytz  # Tambahkan import ini
from datetime import datetime

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
while True:  # Tambahkan perulangan tak terbatas
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

    for keyword in keywords:
        if keyword in domains:
            index_html += f'<li class="list-group-item list-group-item-danger">{keyword}: <span class="blocked">Blocked</span></li>'
            print(f"{keyword}: \033[91mBlocked\033[0m")
        # Hapus bagian ini untuk tidak menampilkan yang not-blocked
        # else:
        #     index_html += f'<li class="list-group-item list-group-item-success">{keyword}: <span class="not-blocked">Not Blocked</span></li>'

    # Mengatur zona waktu Jepang
    japan_tz = pytz.timezone('Asia/Tokyo')

    # Mendapatkan waktu saat ini di zona waktu Jepang
    japan_time = datetime.now(japan_tz)

    # Menampilkan waktu
    print("Waktu di Jepang:", japan_time.strftime('%Y-%m-%d %H:%M:%S'))

    # Mendapatkan waktu saat ini dengan zona waktu lokal
    local_tz = pytz.timezone('Asia/Jakarta')  # Zona waktu lokal
    local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    local_time_with_tz = f"{local_time} WIB"  # Format waktu lokal

    # Mendapatkan waktu saat ini dengan zona waktu Jepang
    japan_time = datetime.now(japan_tz)
    japan_time_with_tz = f"{japan_time.strftime('%Y-%m-%d %H:%M:%S')} JST"  # Format waktu Jepang

    print(f"Last update checked: {local_time_with_tz} (WIB), {japan_time_with_tz} (JST)")
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
    repo.index.add(['index.html'])  # Tambahkan file index.html ke staging
    repo.index.commit('Update index.html')  # Commit perubahan
    repo.git.push('--set-upstream', 'origin', 'main')  # Setelah commit
    origin = repo.remote(name='origin')  # Ambil remote origin
    origin.push()  # Push ke GitHub

    time.sleep(300)  # Tunggu selama 5 menit (300 detik)