---
mitre_id: "T1667"
mitre_name: "Email Bombing"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--bed81616-3dde-4685-be6e-ba9820f9a7ed"
mitre_created: "2025-01-31T14:39:58.478Z"
mitre_modified: "2025-04-15T19:59:03.350Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1667/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Office Suite"
  - "Windows"
  - "macOS"
mitre_tactic_ids:
  - "TA0040"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may flood targeted email addresses with an overwhelming volume of messages. This may bury legitimate emails in a flood of spam and disrupt business operations.(Citation: sophos-bombing)(Citation: krebs-email-bombing)

An adversary may accomplish email bombing by leveraging an automated bot to register a targeted address for e-mail lists that do not validate new signups, such as online newsletters. The result can be a wave of thousands of e-mails that effectively overloads the victim’s inbox.(Citation: krebs-email-bombing)(Citation: hhs-email-bombing)

By sending hundreds or thousands of e-mails in quick succession, adversaries may successfully divert attention away from and bury legitimate messages including security alerts, daily business processes like help desk tickets and client correspondence, or ongoing scams.(Citation: hhs-email-bombing) This behavior can also be used as a tool of harassment.(Citation: krebs-email-bombing)

This behavior may be a precursor for [[T1566-phishing#^t1566004-spearphishing-voice|T1566.004: Spearphishing Voice]]. For example, an adversary may email bomb a target and then follow up with a phone call to fraudulently offer assistance. This social engineering may lead to the use of [Remote Access Software](https://attack.mitre.org/techniques/T1663) to steal credentials, deploy ransomware, conduct [[T1657-financial_theft|T1657: Financial Theft]](Citation: sophos-bombing), or engage in other malicious activity.(Citation: rapid7-email-bombing)


## Workspace

- [[workspaces/attack/techniques/T1667-email_bombing-note|Open workspace note]]

![[workspaces/attack/techniques/T1667-email_bombing-note]]

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- Linux
- Office Suite
- Windows
- macOS

