---
id: T1094
name: Custom Command and Control Protocol
created: 2017-05-31 21:31:10.314000+00:00
modified: 2025-10-24 17:49:37.745000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[command_and_control|Command and Control]]

Adversaries may communicate using a custom command and control protocol instead of encapsulating commands/data in an existing [Application Layer Protocol](https://attack.mitre.org/techniques/T1071). Implementations include mimicking well-known protocols or developing custom protocols (including raw sockets) on top of fundamental protocols provided by TCP/IP/another standard network stack.

## Platforms

- Linux
- macOS
- Windows

