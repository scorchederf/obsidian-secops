---
id: T1139
name: Bash History
created: 2017-12-14 16:46:06.044000+00:00
modified: 2025-10-24 17:48:43.139000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[credential_access|Credential Access]]

Bash keeps track of the commands users type on the command-line with the "history" utility. Once a user logs out, the history is flushed to the user’s <code>.bash_history</code> file. For each user, this file resides at the same location: <code>~/.bash_history</code>. Typically, this file keeps track of the user’s last 500 commands. Users often type usernames and passwords on the command-line as parameters to programs, which then get saved to this file when they log out. Attackers can abuse this by looking through the file for potential credentials. (Citation: External to DA, the OS X Way)

## Properties

- id: T1139
- name: Bash History
- created: 2017-12-14 16:46:06.044000+00:00
- modified: 2025-10-24 17:48:43.139000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Platforms

- Linux
- macOS

