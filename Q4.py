import time
import threading

class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.user_requests = {} 
        self.lock = threading.Lock()  

    def allow_request(self, user_id):
        current_time = time.time()
        with self.lock:  
            if user_id not in self.user_requests:
                self.user_requests[user_id] = []

            self.user_requests[user_id] = [t for t in self.user_requests[user_id] if current_time - t < self.time_window]

            if len(self.user_requests[user_id]) < self.max_requests:
                self.user_requests[user_id].append(current_time)
                return True
            else:
                return False

rate_limiter = RateLimiter()

def make_request(user_id):
    if rate_limiter.allow_request(user_id) == True:
        print("Request by user",user_id,"allowed.")
    else:
        print("Request by user",user_id,"denied.")


for i in range(7):
    make_request('user_1')
    time.sleep(10)
