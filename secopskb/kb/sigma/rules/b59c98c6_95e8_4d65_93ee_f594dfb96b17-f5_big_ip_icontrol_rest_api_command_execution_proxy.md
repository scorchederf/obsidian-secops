---
sigma_id: "b59c98c6-95e8-4d65-93ee-f594dfb96b17"
title: "F5 BIG-IP iControl Rest API Command Execution - Proxy"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_f5_tm_utility_bash_api_request.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_f5_tm_utility_bash_api_request.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "proxy"
aliases:
  - "b59c98c6-95e8-4d65-93ee-f594dfb96b17"
  - "F5 BIG-IP iControl Rest API Command Execution - Proxy"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# F5 BIG-IP iControl Rest API Command Execution - Proxy

Detects POST requests to the F5 BIG-IP iControl Rest API "bash" endpoint, which allows the execution of commands on the BIG-IP

## Metadata

- Rule ID: b59c98c6-95e8-4d65-93ee-f594dfb96b17
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Thurein Oo
- Date: 2023-11-08
- Source Path: rules/web/proxy_generic/proxy_f5_tm_utility_bash_api_request.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection:
  cs-method: POST
  c-uri|endswith: /mgmt/tm/util/bash
condition: selection
```

## False Positives

- Legitimate usage of the BIG IP REST API to execute command for administration purposes

## References

- https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.tm.util.html#module-f5.bigip.tm.util.bash
- https://community.f5.com/t5/technical-forum/icontrolrest-11-5-execute-bash-command/td-p/203029
- https://community.f5.com/t5/technical-forum/running-bash-commands-via-rest-api/td-p/272516

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_f5_tm_utility_bash_api_request.yml)
