---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-NNI"
d3fend_name: "Network Node Inventory"
d3fend_ontology_id: "d3f:NetworkNodeInventory"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ANetworkNodeInventory/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1114"
  - "T1114.002"
  - "T1505"
  - "T1505.002"
  - "T1505.003"
  - "T1562"
  - "T1562.013"
  - "T1578"
  - "T1578.002"
  - "T1578.003"
  - "T1578.004"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Network node inventorying identifies and records all the network nodes (hosts, routers, switches, firewalls, etc.) in the organization's architecture.

## Workspace

- [[workspaces/defend/techniques/D3-NNI-network_node_inventory-note|Open workspace note]]

![[workspaces/defend/techniques/D3-NNI-network_node_inventory-note]]

## Parent Technique

- [[D3-AI-asset_inventory|D3-AI: Asset Inventory]]

## Related ATT&CK Techniques

- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114002-remote-email-collection|T1114.002: Remote Email Collection]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
- [[T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses#^t1562013-disable-or-modify-network-device-firewall|T1562.013: Disable or Modify Network Device Firewall]]
- [[T1578-modify_cloud_compute_infrastructure|T1578: Modify Cloud Compute Infrastructure]]
- [[T1578-modify_cloud_compute_infrastructure#^t1578002-create-cloud-instance|T1578.002: Create Cloud Instance]]
- [[T1578-modify_cloud_compute_infrastructure#^t1578003-delete-cloud-instance|T1578.003: Delete Cloud Instance]]
- [[T1578-modify_cloud_compute_infrastructure#^t1578004-revert-cloud-instance|T1578.004: Revert Cloud Instance]]

## Knowledge Base Article

## How it works
Administrators collect information on network nodes in their architecture using a variety of administrative and management tools that query network devices and nodes for information.  In some cases, where such queries are not supported or provide specific information of interest, an administrator may also collect this information through network enumeration methods to include host discovery and scanning for active ports and services.

## Considerations
* Scanning and probing techniques using mapping tools can result in side effects to information technology (IT) and operational technology (OT) systems.
* An adversary conducting network enumeration may engage in activities that parallel normal network node inventorying activities, but would require escalating to admin privileges for most of the operations requiting administrative tools

## Examples
* Link-layer discovery
   * Link-layer Discovery Protocol (LLDP)
   * Cisco Discovery Protocol (CDP)
* Application-layer discovery
   * Simple Network Management Protocol (SNMP) collects MIB information
   * Web-based Enterprise Management (WBEM) collects CIM information
      * Windows Management Instrumentation (WMI)
      * Windows Management Infrastructure (MI)

## Ontology Relationships

- [[D3-AI-asset_inventory|D3-AI: Asset Inventory]]

