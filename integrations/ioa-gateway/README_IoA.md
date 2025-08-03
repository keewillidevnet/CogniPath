> **Cisco DevNet Note**  
> This Early Preview is part of CogniPath’s integration into Cisco Outshift’s [AGNTCY Internet of Agents](https://github.com/agntcy) ecosystem.  
> The IoA Gateway demonstrates ACP-over-CogniPath routing for multi-agent workflows and will be featured on Cisco Code Exchange.

---

# CogniPath IoA Gateway (Early Preview)

## Overview
The **CogniPath IoA Gateway** bridges Cisco Outshift’s [AGNTCY Internet of Agents](https://github.com/agntcy) ecosystem with the CogniPath intent-driven networking fabric.  

This integration allows CogniPath LM-driven routing nodes to:
- Register in AGNTCY’s **Open Agent Schema Framework (OASF)**
- Advertise capabilities in the **Agent Directory**
- Route **Agent Connect Protocol (ACP)** messages as CogniPackets across multi-hop LM-aware paths

This enables IoA multi-agent workflows to leverage CogniPath as a **resilient, intelligent network fabric**.

---

## How It Works
### 1. Agent Registration via OASF
Each CogniPath node exports an `oasf_metadata.json` describing its capabilities, making it discoverable by IoA-compatible agents.

### 2. ACP Encapsulation in CogniPackets
ACP messages are encapsulated into CogniPackets for routing across CogniPath mesh, benefiting from:
- LM-driven path planning
- Node availability memory
- Replay protection
- Clearance-level enforcement

### 3. Discovery and Routing
IoA Workflow Servers can query the Agent Directory for CogniPath nodes, establishing secure routing channels dynamically.

---

## File Structure
```
integrations/ioa-gateway/
│
├── README_IoA.md          # IoA Gateway overview and integration guide
├── oasf_metadata.json     # OASF-compliant agent capability metadata
├── acp_stub.py            # ACP-to-CogniPath encapsulation logic (stub)
├── example_topology.json  # Sample CogniPath topology for IoA workflow demo
```

---

## Example Use Case
- **Scenario**: A LangChain-built IoA workflow requires low-latency, policy-aware communication between two agents in different networks.
- **Solution**: The Workflow Server discovers CogniPath IoA Gateway nodes via Agent Directory, encapsulates ACP messages in CogniPackets, and routes over CogniPath mesh with intelligent LM decisioning.

---

## Status
**Early Preview**  
- OASF metadata stub available  
- ACP encapsulation scaffold in place  
- Demo topology example provided  

Full ACP transport and dynamic registration to follow in Phase 4.

---

## Next Steps
- Implement dynamic OASF registration from CogniPath nodes
- Complete ACP-to-CogniPacket encapsulation
- Deploy IoA Gateway in an Agent Workflow Server for end-to-end demo