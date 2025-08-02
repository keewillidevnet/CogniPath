# CogniPath – CiscoDevNet Early Preview

> View this project on Cisco Code Exchange: 
[CogniPath on Cisco Code Exchange](https://developer.cisco.com/codeexchange/github/repo/keewillidevnet/CogniPath/)

> **Note for Cisco Code Exchange Reviewers**  
> This branch (`cisco-devnet`) is licensed under the Cisco Sample Code License to meet Cisco Code Exchange submission requirements.  
> The `main` branch of this repository is licensed under Apache 2.0 to support broader vendor compatibility.  
> Both branches contain the same sanitized, public-facing demonstration code.

## Overview
CogniPath is an intent-driven packet networking platform that augments traditional routing with LM-guided path selection.

This early preview demonstrates CogniPath running in a containerized environment on enterprise-class switches, including Cisco Catalyst 9300 (IOx).

⚠️ Note: This is an early preview. Future releases will include advanced features (resilience, policy modules, governance) in alignment with CogniPath’s roadmap.

---

## Use Cases

CogniPath on Cisco Catalyst 9300 (IOx) enables several early-stage demonstration scenarios:

- **Intent-Driven Routing Demo**  
  Dynamically route packets based on LM-embedded intent fields instead of static routing tables.

- **IOx Container Deployment Simulation**  
  Deploy CogniPath as a containerized service on Catalyst 9300 in a lab environment, showcasing adaptability to enterprise-class switches.

- **Topology-Aware Path Selection**  
  Demonstrate LM-guided path adjustments in response to topology changes (e.g., adding/removing neighbor nodes).

- **Multi-Vendor Edge Preparedness**  
  Show compatibility path toward future support for Arista, Juniper, and other enterprise switch platforms.

---

## Quick Start – Catalyst 9300 IOx Deployment (Lab Simulation)
Lab Target: Cisco Catalyst 9300 running IOx container support.

Step 1: Build Docker Image  
    docker build -t cognipath-public .

Step 2: Export for IOx Deployment (Run in Catalyst IOx environment, not on developer machine)  
    ioxclient docker package cognipath-public .  
    ioxclient docker deploy cognipath-public.tar

Step 3: Configure Topology  
    cp examples/topology_example.json topology.json

Step 4: Start CogniPath  
    python main.py --topology topology.json

---

## Example Topology
examples/topology_example.json

```json
{
  "NodeA": ["NodeB", "NodeC"],
  "NodeB": ["NodeA", "NodeD"],
  "NodeC": ["NodeA", "NodeD"],
  "NodeD": ["NodeB", "NodeC"]
}
```

---

## Roadmap Highlights
- Phase 3 (In Development): Resilience enhancements, dynamic policy control, expanded observability
- Phase 4 (Planned): Advanced wireless mesh adaptation, multi-agent consensus, enterprise switch integration (Catalyst IOx, Arista, Junos)

---

## Resources
- CiscoDevNet GitHub: https://github.com/CiscoDevNet
- Cisco Code Exchange: https://developer.cisco.com/codeexchange/
- Cisco IOx Documentation: https://developer.cisco.com/docs/iox/
