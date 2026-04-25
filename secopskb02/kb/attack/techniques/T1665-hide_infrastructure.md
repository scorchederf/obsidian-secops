---
mitre_id: "T1665"
mitre_name: "Hide Infrastructure"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--eb897572-8979-4242-a089-56f294f4c91d"
mitre_created: "2024-02-13T17:00:00.175Z"
mitre_modified: "2025-10-22T03:57:22.646Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1665/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "Network Devices"
  - "Windows"
  - "macOS"
mitre_tactic_ids:
  - "TA0011"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may manipulate network traffic in order to hide and evade detection of their C2 infrastructure. This can be accomplished by identifying and filtering traffic from defensive tools,(Citation: TA571) masking malicious domains to obfuscate the true destination from both automated scanning tools and security researchers,(Citation: Schema-abuse)(Citation: Facad1ng)(Citation: Browser-updates) and otherwise hiding malicious artifacts to delay discovery and prolong the effectiveness of adversary infrastructure that could otherwise be identified, blocked, or taken down entirely.

C2 networks may include the use of [[T1090-proxy|T1090: Proxy]] or VPNs to disguise IP addresses, which can allow adversaries to blend in with normal network traffic and bypass conditional access policies or anti-abuse protections. For example, an adversary may use a virtual private cloud to spoof their IP address to closer align with a victim's IP address ranges. This may also bypass security measures relying on geolocation of the source IP address.(Citation: sysdig)(Citation: Orange Residential Proxies)

Adversaries may also attempt to filter network traffic in order to evade defensive tools in numerous ways, including blocking/redirecting common incident responder or security appliance user agents.(Citation: mod_rewrite)(Citation: SocGholish-update) Filtering traffic based on IP and geo-fencing may also avoid automated sandboxing or researcher activity (i.e., [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]).(Citation: TA571)(Citation: mod_rewrite)

Hiding C2 infrastructure may also be supported by [[TA0042-resource_development|TA0042: Resource Development]] activities such as [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] and [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]. For example, using widely trusted hosting services or domains such as prominent URL shortening providers or marketing services for C2 networks may enable adversaries to present benign content that later redirects victims to malicious web pages or infrastructure once specific conditions are met.(Citation: StarBlizzard)(Citation: QR-cofense)

## Workspace

- [[workspaces/attack/techniques/T1665-hide_infrastructure-note|Open workspace note]]

![[workspaces/attack/techniques/T1665-hide_infrastructure-note]]

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## Platforms

- ESXi
- Linux
- Network Devices
- Windows
- macOS

