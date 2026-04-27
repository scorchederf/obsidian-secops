---
sigma_id: "55f0a3a1-846e-40eb-8273-677371b8d912"
title: "Outlook EnableUnsafeClientMailRules Setting Enabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_outlook_enable_unsafe_client_mail_rules.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_outlook_enable_unsafe_client_mail_rules.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "55f0a3a1-846e-40eb-8273-677371b8d912"
  - "Outlook EnableUnsafeClientMailRules Setting Enabled"
attack_technique_ids:
  - "T1059"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Outlook EnableUnsafeClientMailRules Setting Enabled

Detects an attacker trying to enable the outlook security setting "EnableUnsafeClientMailRules" which allows outlook to run applications or execute macros

## Metadata

- Rule ID: 55f0a3a1-846e-40eb-8273-677371b8d912
- Status: test
- Level: high
- Author: Markus Neis, Nasreddine Bencherchali (Nextron Systems)
- Date: 2018-12-27
- Modified: 2023-02-09
- Source Path: rules/windows/process_creation/proc_creation_win_office_outlook_enable_unsafe_client_mail_rules.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  CommandLine|contains: \Outlook\Security\EnableUnsafeClientMailRules
condition: selection
```

## False Positives

- Unknown

## References

- https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html
- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=44
- https://support.microsoft.com/en-us/topic/how-to-control-the-rule-actions-to-start-an-application-or-run-a-macro-in-outlook-2016-and-outlook-2013-e4964b72-173c-959d-5d7b-ead562979048

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_outlook_enable_unsafe_client_mail_rules.yml)
