---
id: S0057
name: Tasklist
created: 2017-05-31 21:32:39.233000+00:00
modified: 2024-02-12 19:14:37.984000+00:00
type: tool
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

# Tasklist

The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist)

## Properties

- id: S0057
- name: Tasklist
- created: 2017-05-31 21:32:39.233000+00:00
- modified: 2024-02-12 19:14:37.984000+00:00
- type: tool
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1007-system_service_discovery|T1007: System Service Discovery]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1518-software_discovery|T1518: Software Discovery]]
    - [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]

