---
sigma_id: "5b768e71-86f2-4879-b448-81061cbae951"
title: "Suspicious Manipulation Of Default Accounts Via Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_user_default_accounts_manipulation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_user_default_accounts_manipulation.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5b768e71-86f2-4879-b448-81061cbae951"
  - "Suspicious Manipulation Of Default Accounts Via Net.EXE"
attack_technique_ids:
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Manipulation Of Default Accounts Via Net.EXE

Detects suspicious manipulations of default accounts such as 'administrator' and 'guest'. For example 'enable' or 'disable' accounts or change the password...etc

## Metadata

- Rule ID: 5b768e71-86f2-4879-b448-81061cbae951
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-01
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_net_user_default_accounts_manipulation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \net.exe
  - \net1.exe
- OriginalFileName:
  - net.exe
  - net1.exe
selection_user_option:
  CommandLine|contains: ' user '
selection_username:
  CommandLine|contains:
  - ' Järjestelmänvalvoja '
  - ' Rendszergazda '
  - ' Администратор '
  - ' Administrateur '
  - ' Administrador '
  - ' Administratör '
  - ' Administrator '
  - ' guest '
  - ' DefaultAccount '
  - ' "Järjestelmänvalvoja" '
  - ' "Rendszergazda" '
  - ' "Администратор" '
  - ' "Administrateur" '
  - ' "Administrador" '
  - ' "Administratör" '
  - ' "Administrator" '
  - ' "guest" '
  - ' "DefaultAccount" '
  - ' ''Järjestelmänvalvoja'' '
  - ' ''Rendszergazda'' '
  - ' ''Администратор'' '
  - ' ''Administrateur'' '
  - ' ''Administrador'' '
  - ' ''Administratör'' '
  - ' ''Administrator'' '
  - ' ''guest'' '
  - ' ''DefaultAccount'' '
filter:
  CommandLine|contains|all:
  - guest
  - /active no
condition: all of selection_* and not filter
```

## False Positives

- Some false positives could occur with the admin or guest account. It depends on the scripts being used by the admins in your env. If you experience a lot of FP you could reduce the level to medium

## References

- https://www.trellix.com/en-sg/about/newsroom/stories/threat-labs/lockergoga-ransomware-family-used-in-targeted-attacks.html
- https://redacted.com/blog/bianlian-ransomware-gang-gives-it-a-go/
- https://www.microsoft.com/security/blog/2022/09/07/profiling-dev-0270-phosphorus-ransomware-operations/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_user_default_accounts_manipulation.yml)
