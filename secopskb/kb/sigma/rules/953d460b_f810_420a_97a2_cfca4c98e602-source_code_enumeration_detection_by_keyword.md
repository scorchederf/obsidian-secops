---
sigma_id: "953d460b-f810-420a-97a2-cfca4c98e602"
title: "Source Code Enumeration Detection by Keyword"
framework: "sigma"
generated: "true"
source_path: "rules/web/webserver_generic/web_source_code_enumeration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_source_code_enumeration.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "webserver"
aliases:
  - "953d460b-f810-420a-97a2-cfca4c98e602"
  - "Source Code Enumeration Detection by Keyword"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Source Code Enumeration Detection by Keyword

Detects source code enumeration that use GET requests by keyword searches in URL strings

## Metadata

- Rule ID: 953d460b-f810-420a-97a2-cfca4c98e602
- Status: test
- Level: medium
- Author: James Ahearn
- Date: 2019-06-08
- Modified: 2022-10-05
- Source Path: rules/web/webserver_generic/web_source_code_enumeration.yml

## Logsource

- category: webserver

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
keywords:
- .git/
condition: keywords
```

## False Positives

- Unknown

## References

- https://pentester.land/tutorials/2018/10/25/source-code-disclosure-via-exposed-git-folder.html
- https://medium.com/@logicbomb_1/bugbounty-how-i-was-able-to-download-the-source-code-of-indias-largest-telecom-service-52cf5c5640a1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_source_code_enumeration.yml)
