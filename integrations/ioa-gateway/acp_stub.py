"""
ACP Stub for CogniPath IoA Gateway
Phase A — Early Preview

This module will handle encapsulating Agent Connect Protocol (ACP) messages
into CogniPackets for routing over the CogniPath mesh.
"""

from packet import CogniPacket

class ACPStub:
    def __init__(self):
        self.status = "early-preview"
    
    def encapsulate_acp(self, src_agent, dst_agent, acp_message):
        """
        Encapsulates an ACP message inside a CogniPacket.
        """
        print(f"[ACPStub] Encapsulating ACP message from {src_agent} to {dst_agent}")
        packet = CogniPacket(
            src=src_agent,
            dst=dst_agent,
            intent=f"ACP:{acp_message}"
        )
        return packet

    def decapsulate_acp(self, cognipacket):
        """
        Extracts ACP message from a CogniPacket.
        """
        if cognipacket.prompt.startswith("ACP:"):
            acp_payload = cognipacket.prompt.replace("ACP:", "", 1)
            print(f"[ACPStub] Decapsulated ACP message: {acp_payload}")
            return acp_payload
        else:
            print("[ACPStub] No ACP payload found.")
            return None

if __name__ == "__main__":
    # Example run
    stub = ACPStub()
    pkt = stub.encapsulate_acp("AgentAlpha", "AgentBeta", "Hello from ACP!")
    stub.decapsulate_acp(pkt)