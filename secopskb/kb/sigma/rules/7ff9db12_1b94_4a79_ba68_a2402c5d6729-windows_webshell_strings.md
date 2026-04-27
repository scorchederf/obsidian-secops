---
sigma_id: "7ff9db12-1b94-4a79-ba68-a2402c5d6729"
title: "Windows Webshell Strings"
framework: "sigma"
generated: "true"
source_path: "rules/web/webserver_generic/web_win_webshells_in_access_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_win_webshells_in_access_logs.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "high"
logsource: "webserver"
aliases:
  - "7ff9db12-1b94-4a79-ba68-a2402c5d6729"
  - "Windows Webshell Strings"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects common commands used in Windows webshells

## Logsource

- category: webserver

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]

## Detection

```yaml
selection_method:
  cs-method: GET
selection_keywords:
- =whoami
- =net%20user
- =net+user
- =net%2Buser
- =cmd%20/c%
- =cmd+/c+
- =cmd%2B/c%
- =cmd%20/r%
- =cmd+/r+
- =cmd%2B/r%
- =cmd%20/k%
- =cmd+/k+
- =cmd%2B/k%
- =powershell%
- =powershell+
- =tasklist%
- =tasklist+
- =wmic%
- =wmic+
- =ssh%
- =ssh+
- =python%
- =python+
- =python3%
- =python3+
- =ipconfig
- =wget%
- =wget+
- =curl%
- =curl+
- =certutil
- =copy%20%5C%5C
- =dsquery%
- =dsquery+
- =nltest%
- =nltest+
condition: all of selection_*
```

## False Positives

- Web sites like wikis with articles on os commands and pages that include the os commands in the URLs
- User searches in search boxes of the respective website

## References

- https://bad-jubies.github.io/RCE-NOW-WHAT/
- https://m365internals.com/2022/10/07/hunting-in-on-premises-exchange-server-logs/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_win_webshells_in_access_logs.yml)
