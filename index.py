import requests
import threading
import time

# Target URL (use a test server you own or have permission to test)
target_url = "http://localhost:3000/api/v1"

# Number of requests to send per thread
num_requests = 10

# Number of threads (simulating multiple sources)
num_threads = 10

def send_requests():
    for _ in range(num_requests):
        try:
            response = requests.get(target_url)
            print(f"Request sent, status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        time.sleep(0.1)  # Small delay to avoid immediate blocking

# Create and start multiple threads to simulate distributed requests
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=send_requests)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Attack simulation complete.")