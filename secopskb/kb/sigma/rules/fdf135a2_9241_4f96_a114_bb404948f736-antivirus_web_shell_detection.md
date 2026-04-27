---
sigma_id: "fdf135a2-9241-4f96-a114-bb404948f736"
title: "Antivirus Web Shell Detection"
framework: "sigma"
generated: "true"
source_path: "rules/category/antivirus/av_webshell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/category/antivirus/av_webshell.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "antivirus"
aliases:
  - "fdf135a2-9241-4f96-a114-bb404948f736"
  - "Antivirus Web Shell Detection"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Antivirus Web Shell Detection

Detects a highly relevant Antivirus alert that reports a web shell.
It's highly recommended to tune this rule to the specific strings used by your anti virus solution by downloading a big WebShell repository from e.g. github and checking the matches.
This event must not be ignored just because the AV has blocked the malware but investigate, how it came there in the first place.

## Metadata

- Rule ID: fdf135a2-9241-4f96-a114-bb404948f736
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Arnim Rupp
- Date: 2018-09-09
- Modified: 2024-11-02
- Source Path: rules/category/antivirus/av_webshell.yml

## Logsource

- category: antivirus

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
selection:
- Signature|startswith:
  - ASP.
  - IIS/BackDoor
  - JAVA/Backdoor
  - JSP.
  - Perl.
  - PHP.
  - Troj/ASP
  - Troj/JSP
  - Troj/PHP
  - VBS/Uxor
- Signature|contains:
  - ASP_
  - 'ASP:'
  - ASP.Agent
  - ASP/
  - Aspdoor
  - ASPXSpy
  - Backdoor.ASP
  - Backdoor.Java
  - Backdoor.JSP
  - Backdoor.PHP
  - Backdoor.VBS
  - Backdoor/ASP
  - Backdoor/Java
  - Backdoor/JSP
  - Backdoor/PHP
  - Backdoor/VBS
  - C99shell
  - Chopper
  - filebrowser
  - JSP_
  - 'JSP:'
  - JSP.Agent
  - JSP/
  - 'Perl:'
  - Perl/
  - PHP_
  - 'PHP:'
  - PHP.Agent
  - PHP/
  - PHPShell
  - PShlSpy
  - SinoChoper
  - Trojan.ASP
  - Trojan.JSP
  - Trojan.PHP
  - Trojan.VBS
  - VBS.Agent
  - VBS/Agent
  - Webshell
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.nextron-systems.com/?s=antivirus
- https://github.com/tennc/webshell
- https://www.virustotal.com/gui/file/bd1d52289203866645e556e2766a21d2275877fbafa056a76fe0cf884b7f8819/detection
- https://www.virustotal.com/gui/file/308487ed28a3d9abc1fec7ebc812d4b5c07ab025037535421f64c60d3887a3e8/detection
- https://www.virustotal.com/gui/file/7d3cb8a8ff28f82b07f382789247329ad2d7782a72dde9867941f13266310c80/detection
- https://www.virustotal.com/gui/file/e841675a4b82250c75273ebf0861245f80c6a1c3d5803c2d995d9d3b18d5c4b5/detection
- https://www.virustotal.com/gui/file/a80042c61a0372eaa0c2c1e831adf0d13ef09feaf71d1d20b216156269045801/detection
- https://www.virustotal.com/gui/file/b219f7d3c26f8bad7e175934cd5eda4ddb5e3983503e94ff07d39c0666821b7e/detection
- https://www.virustotal.com/gui/file/b8702acf32fd651af9f809ed42d15135f842788cd98d81a8e1b154ee2a2b76a2/detection
- https://www.virustotal.com/gui/file/13ae8bfbc02254b389ab052aba5e1ba169b16a399d9bc4cb7414c4a73cd7dc78/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/category/antivirus/av_webshell.yml)
