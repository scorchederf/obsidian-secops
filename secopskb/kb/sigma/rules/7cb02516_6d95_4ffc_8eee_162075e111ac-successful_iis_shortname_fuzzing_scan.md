---
sigma_id: "7cb02516-6d95-4ffc-8eee-162075e111ac"
title: "Successful IIS Shortname Fuzzing Scan"
framework: "sigma"
generated: "true"
source_path: "rules/web/webserver_generic/web_iis_tilt_shortname_scan.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_iis_tilt_shortname_scan.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "webserver"
aliases:
  - "7cb02516-6d95-4ffc-8eee-162075e111ac"
  - "Successful IIS Shortname Fuzzing Scan"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Successful IIS Shortname Fuzzing Scan

When IIS uses an old .Net Framework it's possible to enumerate folders with the symbol "~"

## Metadata

- Rule ID: 7cb02516-6d95-4ffc-8eee-162075e111ac
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-10-06
- Modified: 2023-01-02
- Source Path: rules/web/webserver_generic/web_iis_tilt_shortname_scan.yml

## Logsource

- category: webserver

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection:
  cs-uri-query|contains: ~1
  cs-uri-query|endswith: a.aspx
  cs-method:
  - GET
  - OPTIONS
  sc-status:
  - 200
  - 301
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/projectdiscovery/nuclei-templates/blob/9d2889356eebba661c8407038e430759dfd4ec31/fuzzing/iis-shortname.yaml
- https://www.exploit-db.com/exploits/19525
- https://github.com/lijiejie/IIS_shortname_Scanner

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_iis_tilt_shortname_scan.yml)
