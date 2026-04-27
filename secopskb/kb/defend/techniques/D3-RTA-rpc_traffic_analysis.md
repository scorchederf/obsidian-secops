---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-RTA"
d3fend_name: "RPC Traffic Analysis"
d3fend_ontology_id: "d3f:RPCTrafficAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ARPCTrafficAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1558"
  - "T1558.003"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Monitoring the activity of remote procedure calls in communication traffic to establish standard protocol operations and potential attacker activities.

## Workspace

- [[workspaces/defend/techniques/D3-RTA-rpc_traffic_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-RTA-rpc_traffic_analysis-note]]

## Parent Technique

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

## Related ATT&CK Techniques

- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]

## Knowledge Base Article

## How it works
A remote procedure call (RPC) enables one computer to execute a specific function on another computer, as if it were a local application process. There are numerous RPC specifications and implementations. RPC capabilities can be abused by attackers in order to achieve a variety of tactical objectives including execution, persistence, initial access, and more. RPC proxies may be used to collect and store RPC traffic. RPCs can occur over network sockets or named pipes.

Analytics look for unauthorized behavior such as:

* Processes being launched or scheduled remotely
* System configurations being changed remotely
* Unauthorized file read activity

Example RPC Protocols:

* DCE/RPC
* CORBA
* Open Network Computing Remote Procedure Call
* D-Bus
* XML-RPC
* JSON-RPC
* SOAP
* Apache Thrift

## Considerations
* RPC is widely used in enterprise environments, and significant data filtering may be required in large environments to enable analytic processing.
* RPC traffic may occur over a pipe, or within a host over loopback interface, thus making network collection difficult.

## Ontology Relationships

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

