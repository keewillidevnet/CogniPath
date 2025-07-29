"""
node.py - Public-safe node orchestration for CogniPath
Note: Internal reroute, telemetry, and replay protection are implemented in CogniPath-core.
"""

class Node:
    def __init__(self, name):
        self.name = name
        print(f"[Node] Created node: {name}")

    def receive_packet(self, packet):
        print(f"[Node] {self.name} received packet: {packet}")