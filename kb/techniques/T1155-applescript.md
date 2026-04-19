---
id: T1155
name: AppleScript
created: 2017-12-14 16:46:06.044000+00:00
modified: 2025-10-24 17:48:50.030000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[execution|Execution]]

macOS and OS X applications send AppleEvent messages to each other for interprocess communications (IPC). These messages can be easily scripted with AppleScript for local or remote IPC. Osascript executes AppleScript and any other Open Scripting Architecture (OSA) language scripts. A list of OSA languages installed on a system can be found by using the <code>osalang</code> program.
AppleEvent messages can be sent independently or as part of a script. These events can locate open windows, send keystrokes, and interact with almost any open application locally or remotely. 

Adversaries can use this to interact with open SSH connection, move to remote machines, and even present users with fake dialog boxes. These events cannot start applications remotely (they can start them locally though), but can interact with applications if they're already running remotely. Since this is a scripting language, it can be used to launch more common techniques as well such as a reverse shell via python  (Citation: Macro Malware Targets Macs). Scripts can be run from the command-line via <code>osascript /path/to/script</code> or <code>osascript -e "script here"</code>.

## Properties

- id: T1155
- name: AppleScript
- created: 2017-12-14 16:46:06.044000+00:00
- modified: 2025-10-24 17:48:50.030000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Platforms

- macOS

