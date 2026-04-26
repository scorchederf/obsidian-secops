---
mitre_id: "T1659"
mitre_name: "Content Injection"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--43c9bc06-715b-42db-972f-52d25c09a20c"
mitre_created: "2023-09-01T21:03:13.406Z"
mitre_modified: "2025-04-15T22:10:29.343Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1659/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0001"
  - "TA0011"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may gain access and continuously communicate with victims by injecting malicious content into systems through online network traffic. Rather than luring victims to malicious payloads hosted on a compromised website (i.e., [[T1608-stage_capabilities#^t1608004-drive-by-target|T1608.004: Drive-by Target]] followed by [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]), adversaries may initially access victims through compromised data-transfer channels where they can manipulate traffic and/or inject their own content. These compromised online network channels may also be used to deliver additional payloads (i.e., [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]) and other data to already compromised systems.(Citation: ESET MoustachedBouncer)

Adversaries may inject content to victim systems in various ways, including:

* From the middle, where the adversary is in-between legitimate online client-server communications (**Note:** this is similar but distinct from [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]], which describes AiTM activity solely within an enterprise environment) (Citation: Kaspersky Encyclopedia MiTM)
* From the side, where malicious content is injected and races to the client as a fake response to requests of a legitimate online server (Citation: Kaspersky ManOnTheSide)

Content injection is often the result of compromised upstream communication channels, for example at the level of an internet service provider (ISP) as is the case with "lawful interception."(Citation: Kaspersky ManOnTheSide)(Citation: ESET MoustachedBouncer)(Citation: EFF China GitHub Attack)

## Workspace

- [[workspaces/attack/techniques/T1659-content_injection-note|Open workspace note]]

![[workspaces/attack/techniques/T1659-content_injection-note]]

## Tactics

- [[TA0001-initial_access|TA0001: Initial Access]]
- [[TA0011-command_and_control|TA0011: Command and Control]]

## Mitigations

- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]

## Platforms

- Linux
- macOS
- Windows

