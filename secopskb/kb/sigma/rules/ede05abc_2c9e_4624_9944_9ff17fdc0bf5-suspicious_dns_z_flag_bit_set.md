---
sigma_id: "ede05abc-2c9e-4624-9944-9ff17fdc0bf5"
title: "Suspicious DNS Z Flag Bit Set"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_dns_susp_zbit_flag.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dns_susp_zbit_flag.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "zeek / dns"
aliases:
  - "ede05abc-2c9e-4624-9944-9ff17fdc0bf5"
  - "Suspicious DNS Z Flag Bit Set"
attack_technique_ids:
  - "T1095"
  - "T1571"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious DNS Z Flag Bit Set

The DNS Z flag is bit within the DNS protocol header that is, per the IETF design, meant to be used reserved (unused).
Although recently it has been used in DNSSec, the value being set to anything other than 0 should be rare.
Otherwise if it is set to non 0 and DNSSec is being used, then excluding the legitimate domains is low effort and high reward.
Determine if multiple of these files were accessed in a short period of time to further enhance the possibility of seeing if this was a one off or the possibility of larger sensitive file gathering.
This Sigma query is designed to accompany the Corelight Threat Hunting Guide, which can be found here: https://www3.corelight.com/corelights-introductory-guide-to-threat-hunting-with-zeek-bro-logs'

## Metadata

- Rule ID: ede05abc-2c9e-4624-9944-9ff17fdc0bf5
- Status: test
- Level: medium
- Author: @neu5ron, SOC Prime Team, Corelight
- Date: 2021-05-04
- Modified: 2022-11-29
- Source Path: rules/network/zeek/zeek_dns_susp_zbit_flag.yml

## Logsource

- product: zeek
- service: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1095-non-application_layer_protocol|T1095]]
- [[kb/attack/techniques/T1571-non-standard_port|T1571]]

## Detection

```yaml
z_flag_unset:
  Z: 0
most_probable_valid_domain:
  query|contains: .
exclude_tlds:
  query|endswith:
  - .arpa
  - .local
  - .ultradns.net
  - .twtrdns.net
  - .azuredns-prd.info
  - .azure-dns.com
  - .azuredns-ff.info
  - .azuredns-ff.org
  - .azuregov-dns.org
exclude_query_types:
  qtype_name:
  - ns
  - mx
exclude_responses:
  answers|endswith: \\x00
exclude_netbios:
  id.resp_p:
  - 137
  - 138
  - 139
condition: not z_flag_unset and most_probable_valid_domain and not (exclude_tlds or
  exclude_query_types or exclude_responses or exclude_netbios)
```

## False Positives

- Internal or legitimate external domains using DNSSec. Verify if these are legitimate DNSSec domains and then exclude them.
- If you work in a Public Sector then it may be good to exclude things like endswith ".edu", ".gov" and or ".mil"

## References

- https://twitter.com/neu5ron/status/1346245602502443009
- https://tdm.socprime.com/tdm/info/eLbyj4JjI15v#sigma
- https://tools.ietf.org/html/rfc2929#section-2.1
- https://www.netresec.com/?page=Blog&month=2021-01&post=Finding-Targeted-SUNBURST-Victims-with-pDNS

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dns_susp_zbit_flag.yml)
