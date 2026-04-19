---
id: T1152
name: Launchctl
created: 2017-12-14 16:46:06.044000+00:00
modified: 2025-10-24 17:48:48.110000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Launchctl controls the macOS launchd process which handles things like launch agents and launch daemons, but can execute other commands or programs itself. Launchctl supports taking subcommands on the command-line, interactively, or even redirected from standard input. By loading or reloading launch agents or launch daemons, adversaries can install persistence or execute changes they made  (Citation: Sofacy Komplex Trojan). Running a command from launchctl is as simple as <code>launchctl submit -l <labelName> -- /Path/to/thing/to/execute "arg" "arg" "arg"</code>. Loading, unloading, or reloading launch agents or launch daemons can require elevated privileges. 

Adversaries can abuse this functionality to execute code or even bypass whitelisting if launchctl is an allowed process.

## Properties

- id: T1152
- name: Launchctl
- created: 2017-12-14 16:46:06.044000+00:00
- modified: 2025-10-24 17:48:48.110000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Platforms

- macOS

