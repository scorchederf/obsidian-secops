---
mitre_id: "T1534"
mitre_name: "Internal Spearphishing"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--9e7452df-5144-4b6e-b04a-b66dd4016747"
mitre_created: "2019-09-04T19:26:12.441Z"
mitre_modified: "2025-10-24T17:49:09.394Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1534/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "macOS"
  - "Linux"
  - "SaaS"
  - "Office Suite"
mitre_tactic_ids:
  - "TA0008"
---

# T1534: Internal Spearphishing

After they already have access to accounts or systems within the environment, adversaries may use internal spearphishing to gain access to additional information or compromise other users within the same organization. Internal spearphishing is multi-staged campaign where a legitimate account is initially compromised either by controlling the user's device or by compromising the account credentials of the user. Adversaries may then attempt to take advantage of the trusted internal account to increase the likelihood of tricking more victims into falling for phish attempts, often incorporating [[T1656-impersonation|T1656: Impersonation]].(Citation: Trend Micro - Int SP)

For example, adversaries may leverage [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]] or [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]] as part of internal spearphishing to deliver a payload or redirect to an external site to capture credentials through [[T1056-input_capture|T1056: Input Capture]] on sites that mimic login interfaces.

Adversaries may also leverage internal chat apps, such as Microsoft Teams, to spread malicious content or engage users in attempts to capture sensitive information and/or credentials.(Citation: Int SP - chat apps)

## Tactics

- [[TA0008-lateral_movement|TA0008: Lateral Movement]]

## Platforms

- Windows
- macOS
- Linux
- SaaS
- Office Suite

