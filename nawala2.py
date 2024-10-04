import requests
import time  # Tambahkan import ini
import os
import git  # Tambahkan import ini

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
output_html = "<html><body><h1>Nawala bot (Trust Positif Checker)</h1><ul>"

while True:  # Tambahkan perulangan tak terbatas
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Nawala bot (Trust Positif Checker)")
    for keyword in keywords:
        if keyword in domains:
            output_html += f"<li>{keyword}: <span style='color:red;'>Blocked</span></li>"
            print(f"{keyword}: \033[91mBlocked\033[0m")
        else:
            output_html += f"<li>{keyword}: Not Blocked</li>"
    print(f"Last update checked: {time.ctime()}")
    output_html += f"</ul><p>Last update checked: {time.ctime()}</p></body></html>"

    # Simpan output ke file HTML
    with open('output.html', 'w') as f:
        f.write(output_html)

    # Push ke GitHub
    repo = git.Repo('.')  # Inisialisasi repository
    repo.index.add(['output.html'])  # Tambahkan file output.html ke staging
    repo.index.commit('Update output.html')  # Commit perubahan
    origin = repo.remote(name='origin')  # Ambil remote origin
    origin.push()  # Push ke GitHub

    time.sleep(300)  # Tunggu selama 5 menit (300 detik)