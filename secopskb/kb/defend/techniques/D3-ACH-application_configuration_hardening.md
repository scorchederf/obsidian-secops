---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-ACH"
d3fend_name: "Application Configuration Hardening"
d3fend_ontology_id: "d3f:ApplicationConfigurationHardening"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AApplicationConfigurationHardening/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Modifying an application's configuration to reduce its attack surface.

## Workspace

- [[workspaces/defend/techniques/D3-ACH-application_configuration_hardening-note|Open workspace note]]

![[workspaces/defend/techniques/D3-ACH-application_configuration_hardening-note]]

## Parent Technique

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

## Child Techniques

- [[D3-DRA-disable_remote_access|D3-DRA: Disable Remote Access]]

## Related ATT&CK Techniques

- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114003-email-forwarding-rule|T1114.003: Email Forwarding Rule]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]
- [[T1562-impair_defenses#^t1562003-impair-command-history-logging|T1562.003: Impair Command History Logging]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[T1564-hide_artifacts#^t1564008-email-hiding-rules|T1564.008: Email Hiding Rules]]

## Knowledge Base Article

## How it works
Application configuration settings can be configured to limit the permissions on an application or disable certain vulnerable application features.

Hardening an application's configuration involves analyzing not only the application but also the environment in which the application is run in for potential vulnerabilities.

## Ontology Relationships

- [[D3-AH-application_hardening|D3-AH: Application Hardening]]

