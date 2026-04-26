---
sigma_id: "8ae51330-899c-4641-8125-e39f2e07da72"
title: "DNS TXT Answer with Possible Execution Strings"
framework: "sigma"
generated: "true"
source_path: "rules/network/dns/net_dns_susp_txt_exec_strings.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_susp_txt_exec_strings.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "dns"
aliases:
  - "8ae51330-899c-4641-8125-e39f2e07da72"
  - "DNS TXT Answer with Possible Execution Strings"
attack_technique_ids:
  - "T1071.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS TXT Answer with Possible Execution Strings

Detects strings used in command execution in DNS TXT Answer

## Metadata

- Rule ID: 8ae51330-899c-4641-8125-e39f2e07da72
- Status: test
- Level: high
- Author: Markus Neis
- Date: 2018-08-08
- Modified: 2021-11-27
- Source Path: rules/network/dns/net_dns_susp_txt_exec_strings.yml

## Logsource

- category: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.004]]

## Detection

```yaml
selection:
  record_type: TXT
  answer|contains:
  - IEX
  - Invoke-Expression
  - cmd.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/stvemillertime/status/1024707932447854592
- https://github.com/samratashok/nishang/blob/414ee1104526d7057f9adaeee196d91ae447283e/Backdoors/DNS_TXT_Pwnage.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_susp_txt_exec_strings.yml)
