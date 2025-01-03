# network/message_queue.py
"""
Handles prioritization for broadcasting critical transactions or blocks.
"""

import queue
import threading


class MessageQueue:
    def __init__(self):
        self.queue = queue.PriorityQueue()
        self.lock = threading.Lock()

    def add_message(self, priority, message):
        """
        Adds a message with a given priority.
        """
        with self.lock:
            self.queue.put((priority, message))

    def get_message(self):
        """
        Retrieves the highest-priority message.
        """
        with self.lock:
            return self.queue.get()

    def process_messages(self, broadcast_callback):
        """
        Continuously processes and broadcasts messages.
        """
        while True:
            priority, message = self.get_message()
            broadcast_callback(message)
