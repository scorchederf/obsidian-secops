---
sigma_id: "8ae51330-899c-4641-8125-e39f2e07da72"
title: "DNS TXT Answer with Possible Execution Strings"
framework: "sigma"
generated: "true"
source_path: "rules/network/dns/net_dns_susp_txt_exec_strings.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_susp_txt_exec_strings.yml"
build_date: "2026-04-27 19:13:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects strings used in command execution in DNS TXT Answer

## Logsource

- category: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]

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
