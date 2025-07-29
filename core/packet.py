"""
packet.py - Public-safe packet representation
Note: Internal serialization, compression, TTL, and secure token handling are protected in CogniPath-core.
"""

class Packet:
    def __init__(self, src, dst, intent):
        self.src = src
        self.dst = dst
        self.intent = intent

    def __repr__(self):
        return f"<Packet src={self.src} dst={self.dst} intent={self.intent}>"