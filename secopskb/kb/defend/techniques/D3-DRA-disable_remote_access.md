---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DRA"
d3fend_name: "Disable Remote Access"
d3fend_ontology_id: "d3f:DisableRemoteAccess"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADisableRemoteAccess/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1114"
  - "T1114.003"
  - "T1562"
  - "T1562.002"
  - "T1562.003"
  - "T1564"
  - "T1564.008"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Limiting access to a computing device which is not required through or from a non-organization-controlled network.

## Workspace

- [[workspaces/defend/techniques/D3-DRA-disable_remote_access-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DRA-disable_remote_access-note]]

## Parent Technique

- [[D3-ACH-application_configuration_hardening|D3-ACH: Application Configuration Hardening]]

## Related ATT&CK Techniques

- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114003-email-forwarding-rule|T1114.003: Email Forwarding Rule]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]
- [[T1562-impair_defenses#^t1562003-impair-command-history-logging|T1562.003: Impair Command History Logging]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[T1564-hide_artifacts#^t1564008-email-hiding-rules|T1564.008: Email Hiding Rules]]

## Knowledge Base Article

## How It Works
There are several different methods of achieving remote access restriction. This could include: time-based controls, just-in-time authorization, and deny-by-default controls.

This can be done on a Windows machine by unchecking an "allow remote assistance" or checking the "don't allow remote connections" boxes; creating firewall rules to block remote access protocols; uninstalling remote access software; disabling Wi-Fi, Ethernet, Bluetooth, or other connection methods enabling remote access.

One way to achieve remote access restrictions in OT is by programming logic in the OT Controller to give the Operator authorizing abilities which ensures local control is maintained. In this situation, a remote access modem would be powered on/off using a discrete output from an I/O module of the OT controller.
    

## See Also

- https://www.dragos.com/blog/industry-news/value-of-plc-key-switch-monitoring/#:~:text=Run%20mode%E2%80%94The%20controller%20is,in%20the%20Remote%20Program%20mode

## Ontology Relationships

- [[D3-ACH-application_configuration_hardening|D3-ACH: Application Configuration Hardening]]

