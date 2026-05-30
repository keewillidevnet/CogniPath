"""
test_acp_stub.py - Tests for the IoA Gateway ACP encapsulation stub.

These tests ensure that the ACP-to-CogniPath encapsulation roundtrip works
correctly. They lock in the contract for the AGNTCY integration showcase.
"""

import sys
import os
import importlib.util

# The module path uses a dash in the directory name, so we import via spec
_ACP_STUB_PATH = os.path.join(
    os.path.dirname(__file__), "..", "integrations", "ioa-gateway", "acp_stub.py"
)
_spec = importlib.util.spec_from_file_location("acp_stub", _ACP_STUB_PATH)
_acp_stub = importlib.util.module_from_spec(_spec)
sys.modules["acp_stub"] = _acp_stub
_spec.loader.exec_module(_acp_stub)
ACPStub = _acp_stub.ACPStub


def test_encapsulate_then_decapsulate_roundtrip():
    """ACP message encapsulated into a CogniPath Packet must decapsulate to the original."""
    stub = ACPStub()
    original_message = "Hello from ACP!"
    packet = stub.encapsulate_acp("AgentAlpha", "AgentBeta", original_message)
    recovered = stub.decapsulate_acp(packet)
    assert recovered == original_message


def test_encapsulated_packet_intent_prefixed():
    """Encapsulated ACP packets must carry the ACP: intent prefix."""
    stub = ACPStub()
    packet = stub.encapsulate_acp("AgentX", "AgentY", "ping")
    assert packet.intent.startswith("ACP:")
    assert packet.src == "AgentX"
    assert packet.dst == "AgentY"


def test_decapsulate_non_acp_packet_returns_none():
    """Non-ACP packets must return None from decapsulate, not raise."""
    from core.packet import Packet
    stub = ACPStub()
    non_acp_packet = Packet("NodeA", "NodeB", "ordinary intent without ACP prefix")
    assert stub.decapsulate_acp(non_acp_packet) is None
