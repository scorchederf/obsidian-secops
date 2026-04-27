---
atomic_guid: "0976990f-53b1-4d3f-a185-6df5be429d3b"
title: "Display group policy information via gpresult"
framework: "atomic"
generated: "true"
attack_technique_id: "T1615"
attack_technique_name: "Group Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1615/T1615.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "0976990f-53b1-4d3f-a185-6df5be429d3b"
  - "Display group policy information via gpresult"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Uses the built-in Windows utility gpresult to display the Resultant Set of Policy (RSoP) information for a remote user and computer
The /z parameter displays all available information about Group Policy. More parameters can be found in the linked Microsoft documentation
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult
https://unit42.paloaltonetworks.com/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/
Turla has used the /z and /v parameters: https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf

## ATT&CK Mapping

- [[kb/attack/techniques/T1615-group_policy_discovery|T1615: Group Policy Discovery]]

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
gpresult /z
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1615/T1615.yaml)
