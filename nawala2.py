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
for keyword in keywords:
    if keyword in domains:
        print(f"{keyword}: Blocked")
    else:
        print(f"{keyword}: Unblocked")