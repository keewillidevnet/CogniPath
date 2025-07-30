# CogniPath™  
**Intent-Driven Networking Powered by Distributed Language Model Agents**  

---

## Overview  
CogniPath™ is a next-generation intent-driven packet networking system that leverages distributed language model (LM) agents to dynamically determine packet routing paths in real time. Instead of static configuration or legacy routing convergence delays, CogniPath™ embeds **intent** directly in packet metadata, enabling an intelligent, adaptive network that reacts instantly to topology changes, failures, and evolving policy requirements.  

Unlike traditional routing protocols (BGP, OSPF, EIGRP), CogniPath™ dynamically adapts to the **actual intent** of the packet using on-demand inference, enabling:  
- Adaptive routing based on live topology and telemetry.  
- Real-time rerouting around failures or degraded links.  
- Compatibility with legacy protocols via a protocol-agnostic interface.  

---

## Release Information
**Version:** v0.1.0 Initial Public Pre-release (Public Architecture Preview)  

See the [Release Notes](https://github.com/keewillidevnet/CogniPath/releases/tag/v0.1.0-public-preview) for details.

---

## Key Innovations  

### **1️⃣ Decentralization + Packet-Level LM Intent**  
- Each packet carries embedded intent in its header/payload.  
- Nodes act as autonomous LM agents interpreting this intent.  
- Eliminates reliance on a single centralized controller.  

### **2️⃣ Agentic Consensus + Determinism via LM**  
- Distributed LMs act as decision agents to agree on optimal paths.  
- Security hardened by token-hashing, UUID replay prevention, and consensus thresholds.  
- Ensures deterministic decision outcomes in distributed settings.  

### **3️⃣ Control-Plane Intelligence Shift**  
- Moves decision-making to the **edge control plane**.  
- Routing decisions are **triggered dynamically** by packets rather than static policies.  
- Enables continuous optimization as topology evolves.  

### **4️⃣ Adaptive Switching (Phase 4 Feature)**  
- Next‑generation replacement for spanning tree.  
- Keeps all links active while preventing loops in real time.  
- Dynamically adapts switching paths based on LM-driven network intent and live health telemetry.  

### **5️⃣ Wireless-Ready Adaptive Framework**  
- CogniPath’s architecture is designed for **wireline and wireless environments**, including LoRaMesh, Wi‑Fi 6, and 5G.  
- Intent‑driven routing seamlessly adapts to variable wireless link quality and mobility conditions.  
- Wireless capability is enabled through the same LM‑driven control plane, ensuring **link resilience and real‑time rerouting** without protocol‑specific dependencies.  

---

## Suggested Augmentations (Included in Roadmap)  

- **LM Prompt Adaptation:** Mutates LM inputs dynamically (e.g., excludes failed nodes) based on telemetry.  
- **LM Response Auditability:** Logs LM decisions in signed, traceable formats (`logs/lm_decisions.log`).  
- **Protocol-Agnostic Compatibility Layer:** Translates LM-generated paths to legacy protocol equivalents (e.g., OSPF/BGP route injection).  
- **Adaptive Switching:** Introduces LM-driven loop prevention and multi-path utilization for switching fabrics.  
- **Enterprise-Grade Switch Integration Demo**
  - Deployment of CogniPath-core in containerized environments on high-performance enterprise switches (e.g., Arista container-manager, Cisco IOx, Junos OS Evolved, etc.,).
  - Showcases LM-driven routing operating in parallel with traditional control planes.
  - Illustrates intent-aware routing capabilities on enterprise hardware without exposing proprietary mechanisms.

---

## Repository Structure (Public-Safe Layout)  

```
CogniPath/
│
├── config/                # Configuration files
│   └── lm_roles.yaml      # Defines LM roles: CogniCore™, CogniEdge™, CogniLite™
│
├── core/                  # Public-safe core architecture
│   ├── README.md          # Core overview (public-safe)
│   ├── __init__.py        # Package initialization
│   ├── agent.py           # LM orchestration layer (sanitized)
│   ├── node.py            # Node logic abstraction (sanitized)
│   ├── packet.py          # Packet structure & public-safe processing
│   ├── tokenlib.py        # Public-safe token validation
│   └── utils.py           # Utility functions
│
├── docs/                  # Documentation
│   └── README.md          # High-level technical overview
│
├── legacy_compat/         # Legacy routing protocol stubs (no LM logic)
│   ├── bgp/
│   │   └── parser.py      # BGP compatibility stub
│   ├── eigrp/
│   │   └── parser.py      # EIGRP compatibility stub
│   ├── ospf/
│   │   └── parser.py      # OSPF compatibility stub
│   └── README.md          # Legacy compatibility overview
│
├── logs/                  # Logs & auditing (public-safe)
│   ├── README.md          # Logging overview
│   ├── agent_audit.log    # LM agent audit trail (public scrubbed)
│   └── lm_decisions.log   # LM decision logs (public scrubbed)
│
├── tests/                 # Public-safe test suite
│   ├── README.md          # Overview of testing framework
│   ├── __init__.py        # Package init for test discovery
│   ├── test_agent.py      # Tests for agent abstraction layer
│   └── test_packet.py     # Tests for packet structure
│
├── .gitattributes         # Public repo IP boundaries & file handling
├── .gitignore             # Ignored files for public repo safety
├── LICENSE.md             # Proprietary license for CogniPath
├── NOTICE.md              # IP protection notice & patent language
├── README.md              # This file (overview & documentation)
├── main.py                # Demo entry point for public build
└── requirements.txt       # Public-safe dependencies
```

---

## Intellectual Property & Licensing  
This public repository contains a **limited, public-safe subset** of CogniPath’s architecture.  
Core intellectual property (LM internals, consensus algorithms, advanced prompt structures, and production routing logic) is maintained in the **private `CogniPath-core` repository**.  

Patent protection is in process via **USPTO Provisional Patent Application (PPA)** covering:  
- LM intent-embedded packet networking.  
- Distributed LM consensus routing.  
- Edge-triggered control plane inference.  
- Adaptive Switching (loop-free multipath switching).  

---

## Installation & Quickstart  

**Clone the repository:**
```bash
git clone https://github.com/<your-org>/CogniPath.git
cd CogniPath
```

**Create a virtual environment & install dependencies:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Run the demo:**
```bash
python3 main.py
```

---

## Legacy Protocol Compatibility  
CogniPath™ supports **interoperation with existing networks** by translating LM-decided paths to formats understood by:  
- OSPF  
- BGP  
- EIGRP  

**Note:**  
Legacy protocol translators in `legacy_compat/` are **public stubs**. Full compatibility modules are maintained in **private protected code**.

---

## License & Notice  
This public repository is released under a **restricted license**.  
Use is allowed for educational/research purposes.  
Production/commercial usage without explicit permission is prohibited.  

See `NOTICE.md` for detailed IP and licensing terms.

---

## Learn More  
- **Patent Status:** PPA filed (USPTO)  
- **Private Repo:** CogniPath-core (invite only)  
- **Public Roadmap:** See [Phase 3 & 4 Roadmap in Issues]  

---

## Community & Contact  
We welcome constructive collaboration, issue reports, and discussions.  

Contact: **Keenan Williams at telesis001@icloud.com**
