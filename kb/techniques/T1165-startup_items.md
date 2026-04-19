---
id: T1165
name: Startup Items
created: 2017-12-14 16:46:06.044000+00:00
modified: 2025-10-24 17:48:34.254000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[privilege_escalation|Privilege Escalation]]

Per Apple’s documentation, startup items execute during the final phase of the boot process and contain shell scripts or other executable files along with configuration information used by the system to determine the execution order for all startup items (Citation: Startup Items). This is technically a deprecated version (superseded by Launch Daemons), and thus the appropriate folder, <code>/Library/StartupItems</code> isn’t guaranteed to exist on the system by default, but does appear to exist by default on macOS Sierra. A startup item is a directory whose executable and configuration property list (plist), <code>StartupParameters.plist</code>, reside in the top-level directory. 

An adversary can create the appropriate folders/files in the StartupItems directory to register their own persistence mechanism (Citation: Methods of Mac Malware Persistence). Additionally, since StartupItems run during the bootup phase of macOS, they will run as root. If an adversary is able to modify an existing Startup Item, then they will be able to Privilege Escalate as well.

## Platforms

- macOS

