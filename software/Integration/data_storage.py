from threading import Lock

# Shared data storage with thread-safe access
class DataStorage:
    def __init__(self):
        self.data = None
        self.lock = Lock()

    def update_data(self, new_data):
        with self.lock:
            self.data = new_data

    def get_latest_data(self):
        with self.lock:
            return self.data

# Global instance
shared_data = DataStorage()


