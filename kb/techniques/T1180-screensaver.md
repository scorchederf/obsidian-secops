---
id: T1180
name: Screensaver
created: 2018-01-16 16:13:52.465000+00:00
modified: 2025-10-24 17:48:33.235000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[persistence|Persistence]]

Screensavers are programs that execute after a configurable time of user inactivity and consist of Portable Executable (PE) files with a .scr file extension.(Citation: Wikipedia Screensaver) The Windows screensaver application scrnsave.scr is located in <code>C:\Windows\System32\</code>, and <code>C:\Windows\sysWOW64\</code> on 64-bit Windows systems, along with screensavers included with base Windows installations. 

The following screensaver settings are stored in the Registry (<code>HKCU\Control Panel\Desktop\</code>) and could be manipulated to achieve persistence:

* <code>SCRNSAVE.exe</code> - set to malicious PE path
* <code>ScreenSaveActive</code> - set to '1' to enable the screensaver
* <code>ScreenSaverIsSecure</code> - set to '0' to not require a password to unlock
* <code>ScreenSaveTimeout</code> - sets user inactivity timeout before screensaver is executed

Adversaries can use screensaver settings to maintain persistence by setting the screensaver to run malware after a certain timeframe of user inactivity. (Citation: ESET Gazer Aug 2017)

## Properties

- id: T1180
- name: Screensaver
- created: 2018-01-16 16:13:52.465000+00:00
- modified: 2025-10-24 17:48:33.235000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Platforms

- Windows

