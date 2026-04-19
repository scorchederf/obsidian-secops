---
id: T1153
name: Source
created: 2017-12-14 16:46:06.044000+00:00
modified: 2025-10-24 17:48:43.489000+00:00
type: attack-pattern
x_mitre_version: 2.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[execution|Execution]]

**This technique has been deprecated and should no longer be used.**

The <code>source</code> command loads functions into the current shell or executes files in the current context. This built-in command can be run in two different ways <code>source /path/to/filename [arguments]</code> or <code>.**This technique has been deprecated and should no longer be used.** /path/to/filename [arguments]</code>. Take note of the space after the ".". Without a space, a new shell is created that runs the program instead of running the program within the current context. This is often used to make certain features or functions available to a shell or to update a specific shell's environment.(Citation: Source Manual)

Adversaries can abuse this functionality to execute programs. The file executed with this technique does not need to be marked executable beforehand.

## Properties

- id: T1153
- name: Source
- created: 2017-12-14 16:46:06.044000+00:00
- modified: 2025-10-24 17:48:43.489000+00:00
- type: attack-pattern
- x_mitre_version: 2.1
- x_mitre_domains: enterprise-attack

## Platforms

- Linux
- macOS

