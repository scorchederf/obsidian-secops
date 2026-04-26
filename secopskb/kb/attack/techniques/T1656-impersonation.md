---
mitre_id: "T1656"
mitre_name: "Impersonation"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--c9e0c59e-162e-40a4-b8b1-78fab4329ada"
mitre_created: "2023-08-08T15:42:18.906Z"
mitre_modified: "2025-04-15T22:41:31.140Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1656/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Office Suite"
  - "SaaS"
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may impersonate a trusted person or organization in order to persuade and trick a target into performing some action on their behalf. For example, adversaries may communicate with victims (via [[T1598-phishing_for_information|T1598: Phishing for Information]], [[T1566-phishing|T1566: Phishing]], or [[T1534-internal_spearphishing|T1534: Internal Spearphishing]]) while impersonating a known sender such as an executive, colleague, or third-party vendor. Established trust can then be leveraged to accomplish an adversary’s ultimate goals, possibly against multiple victims. 
 
In many cases of business email compromise or email fraud campaigns, adversaries use impersonation to defraud victims -- deceiving them into sending money or divulging information that ultimately enables [[T1657-financial_theft|T1657: Financial Theft]].

Adversaries will often also use social engineering techniques such as manipulative and persuasive language in email subject lines and body text such as `payment`, `request`, or `urgent` to push the victim to act quickly before malicious activity is detected. These campaigns are often specifically targeted against people who, due to job roles and/or accesses, can carry out the adversary’s goal.   
 
Impersonation is typically preceded by reconnaissance techniques such as [[T1589-gather_victim_identity_information|T1589: Gather Victim Identity Information]] and [[T1591-gather_victim_org_information|T1591: Gather Victim Org Information]] as well as acquiring infrastructure such as email domains (i.e. [[T1583-acquire_infrastructure#^t1583001-domains|T1583.001: Domains]]) to substantiate their false identity.(Citation: CrowdStrike-BEC)
 
There is the potential for multiple victims in campaigns involving impersonation. For example, an adversary may [[T1586-compromise_accounts|T1586: Compromise Accounts]] targeting one organization which can then be used to support impersonation against other entities.(Citation: VEC)

## Workspace

- [[workspaces/attack/techniques/T1656-impersonation-note|Open workspace note]]

![[workspaces/attack/techniques/T1656-impersonation-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1019-threat_intelligence_program|M1019: Threat Intelligence Program]]

## Tools

- [[nppspy|NPPSPY (S1131)]]

## Platforms

- Linux
- macOS
- Office Suite
- SaaS
- Windows

