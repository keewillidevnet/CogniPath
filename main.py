"""
main.py - Public demo entry point
Note: Full simulation engine is implemented in CogniPath-core.
"""

from core.agent import Agent
from core.node import Node
from core.packet import Packet

if __name__ == "__main__":
    agent = Agent()
    nodeA = Node("NodeA")
    packet = Packet("NodeA", "NodeB", "send diagnostic data")
    nodeA.receive_packet(packet)
