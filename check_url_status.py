import csv
import requests

def check_url_status(csv_file, target_url=None):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)  # Use csv.reader instead of csv.DictReader
        for row in reader:
            url = row[0]  # Assuming the URL is in the first column (index 0)
            if target_url and target_url.lower() not in url.lower():
                continue
            try:
                response = requests.get(url, timeout=10)
                print(f"({response.status_code}) {url}")
            except requests.exceptions.RequestException as e:
                print(f"(Error) {url}: {e}")

file_path = r"Task 2 - Intern.csv"
check_url_status(file_path)
