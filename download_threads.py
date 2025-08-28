import threading
import time
import requests
import os

OUT_DIR = "downloads"
os.makedirs(OUT_DIR, exist_ok=True)

URLS = [
    "https://www.example.com",
    "https://httpbin.org/get",
    "https://api.github.com",
    "https://www.python.org",
    "https://jsonplaceholder.typicode.com/posts/1"
]

def download_url(url, index):
    """Download URL and save to a file named file_{index+1}.html"""
    fname = os.path.join(OUT_DIR, f"file_{index+1}.html")
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        with open(fname, "wb") as f:
            f.write(r.content)
        print(f"[OK]   {url} -> {fname} ({len(r.content)} bytes)")
    except requests.RequestException as e:
        print(f"[ERR]  {url} -> {e}")

def main():
    threads = []
    start = time.perf_counter()

    for i, url in enumerate(URLS):
        t = threading.Thread(target=download_url, args=(url, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start
    print(f"\nAll downloads done. Total time: {elapsed:.2f} seconds")
    print(f"Files saved in folder: {OUT_DIR}")

if __name__ == "__main__":
    main()
