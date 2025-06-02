import requests
import threading
import time
import random # Added for jitter in backoff

# Target URL (use a test server you own or have permission to test)
target_url = "http://localhost:3001/api"

# Number of requests to send per thread
num_requests = 100

# Number of threads (simulating multiple sources)
num_threads = 10

# Constants for retry logic
MAX_RETRIES_429 = 3
INITIAL_BACKOFF_SECONDS = 1

def send_requests():
    thread_id = threading.get_ident()
    for i in range(num_requests):
        current_retries = 0
        while True: # Loop for retries
            try:
                response = requests.get(target_url) # Make the request
                
                if response.status_code == 429:
                    if current_retries < MAX_RETRIES_429:
                        current_retries += 1
                        
                        # Check for Retry-After header
                        retry_after_header = response.headers.get("Retry-After")
                        wait_duration = INITIAL_BACKOFF_SECONDS * (2 ** (current_retries - 1)) # Exponential backoff

                        if retry_after_header:
                            try:
                                # If it's a number, it's seconds
                                wait_duration = int(retry_after_header)
                                print(f"Thread {thread_id}: Got 429. Server suggests Retry-After: {wait_duration}s. Retrying ({current_retries}/{MAX_RETRIES_429})...")
                            except ValueError:
                                # It might be an HTTP-date, which is more complex to parse.
                                # For simplicity, we'll stick to our exponential backoff if parsing fails.
                                print(f"Thread {thread_id}: Got 429. Could not parse Retry-After: '{retry_after_header}'. Using exponential backoff: {wait_duration}s. Retrying ({current_retries}/{MAX_RETRIES_429})...")
                        else:
                            print(f"Thread {thread_id}: Got 429. Using exponential backoff: {wait_duration}s. Retrying ({current_retries}/{MAX_RETRIES_429})...")
                        
                        # Add jitter (a small random delay to prevent thundering herd)
                        jitter = random.uniform(0, 0.2 * wait_duration) # Jitter up to 20% of wait_duration
                        time.sleep(wait_duration + jitter)
                        continue # Retry the request
                    else:
                        print(f"Thread {thread_id}: Request {i+1}/{num_requests} failed after {MAX_RETRIES_429} retries due to 429.")
                        break # Give up on this request after exhausting retries for 429
                else:
                    # For non-429 responses (success or other errors)
                    if response.status_code >= 200 and response.status_code < 300:
                        print(f"Thread {thread_id}: Request {i+1}/{num_requests}, Status: {response.status_code} (Success)")
                    else: # Handles 404 and other non-429 client/server errors
                        print(f"Thread {thread_id}: Request {i+1}/{num_requests}, Status: {response.status_code} (Failed)")
                    # Break from retry loop as this request is considered handled (either success or non-429 error)
                    break # Break from retry loop (request processed)
            
            except requests.exceptions.RequestException as e:
                print(f"Thread {thread_id}: Request {i+1}/{num_requests} generated an exception: {e}")
                break # Break from retry loop on exception
        time.sleep(0.1)  # Small delay between initiating new logical requests

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