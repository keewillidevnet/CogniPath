"""
test_packet.py - Public-safe unit test placeholder for Packet
"""

from core.packet import Packet

def test_packet_repr():
    p = Packet("NodeA", "NodeB", "diagnostic")
    assert "Packet" in repr(p)