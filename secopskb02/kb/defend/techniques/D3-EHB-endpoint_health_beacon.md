---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-EHB"
d3fend_name: "Endpoint Health Beacon"
d3fend_ontology_id: "d3f:EndpointHealthBeacon"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AEndpointHealthBeacon/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 20:43:29"
build_source: "script"
attack_technique_ids:
  - "T1114"
  - "T1114.002"
  - "T1505"
  - "T1505.002"
  - "T1505.003"
  - "T1562"
  - "T1562.009"
  - "T1562.013"
  - "T1578"
  - "T1578.002"
  - "T1578.003"
  - "T1578.004"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Monitoring the security status of an endpoint by sending periodic messages with health status, where absence of a response may indicate that the endpoint has been compromised.

## Workspace

- [[workspaces/defend/techniques/D3-EHB-endpoint_health_beacon-note|Open workspace note]]

![[workspaces/defend/techniques/D3-EHB-endpoint_health_beacon-note]]

## Parent Technique

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

## Related ATT&CK Techniques

- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114002-remote-email-collection|T1114.002: Remote Email Collection]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
- [[T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses#^t1562009-safe-mode-boot|T1562.009: Safe Mode Boot]]
- [[T1562-impair_defenses#^t1562013-disable-or-modify-network-device-firewall|T1562.013: Disable or Modify Network Device Firewall]]
- [[T1578-modify_cloud_compute_infrastructure|T1578: Modify Cloud Compute Infrastructure]]
- [[T1578-modify_cloud_compute_infrastructure#^t1578002-create-cloud-instance|T1578.002: Create Cloud Instance]]
- [[T1578-modify_cloud_compute_infrastructure#^t1578003-delete-cloud-instance|T1578.003: Delete Cloud Instance]]
- [[T1578-modify_cloud_compute_infrastructure#^t1578004-revert-cloud-instance|T1578.004: Revert Cloud Instance]]

## Knowledge Base Article

## How it works
Endpoints are configured to periodically generate and transmit a secure heartbeat that is delivered on a configured schedule and provides endpoint status information. Status information can include software details (version, configuration, etc), endpoint identification (MAC, IP address, machine ID) or other hardware/software configuration information. Interruption of the heartbeat can signal that the endpoint has been compromised.

## Considerations
* Security of heartbeat messages to ensure message integrity
* Disappearance of the heartbeat could simply mean that the endpoint is powered off or intentionally disconnected from the network. Therefore other criteria may need to be used to accurately detect endpoint compromise.
* Attacker presence on the machine may leave the heartbeat intact.
* An attacker may determine the format of the heartbeat and continue to send it even after the machine is compromised.

## Ontology Relationships

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

