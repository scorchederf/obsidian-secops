---
sigma_id: "583aa0a2-30b1-4d62-8bf3-ab73689efe6c"
title: "Java Payload Strings"
framework: "sigma"
generated: "true"
source_path: "rules/web/webserver_generic/web_java_payload_in_access_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_java_payload_in_access_logs.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "webserver"
aliases:
  - "583aa0a2-30b1-4d62-8bf3-ab73689efe6c"
  - "Java Payload Strings"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Java Payload Strings

Detects possible Java payloads in web access logs

## Metadata

- Rule ID: 583aa0a2-30b1-4d62-8bf3-ab73689efe6c
- Status: test
- Level: high
- Author: frack113, Harjot Singh, "@cyb3rjy0t" (update)
- Date: 2022-06-04
- Modified: 2023-01-19
- Source Path: rules/web/webserver_generic/web_java_payload_in_access_logs.yml

## Logsource

- category: webserver

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
keywords:
- '%24%7B%28%23a%3D%40'
- ${(#a=@
- '%24%7B%40java'
- ${@java
- u0022java
- '%2F%24%7B%23'
- /${#
- new+java.
- getRuntime().exec(
- getRuntime%28%29.exec%28
condition: keywords
```

## False Positives

- Legitimate apps

## References

- https://www.rapid7.com/blog/post/2022/06/02/active-exploitation-of-confluence-cve-2022-26134/
- https://www.rapid7.com/blog/post/2021/09/02/active-exploitation-of-confluence-server-cve-2021-26084/
- https://github.com/httpvoid/writeups/blob/62d3751945289d088ccfdf4d0ffbf61598a2cd7d/Confluence-RCE.md
- https://twitter.com/httpvoid0x2f/status/1532924261035384832
- https://medium.com/geekculture/text4shell-exploit-walkthrough-ebc02a01f035

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_java_payload_in_access_logs.yml)
