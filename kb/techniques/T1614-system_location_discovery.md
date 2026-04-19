---
id: T1614
name: System Location Discovery
created: 2021-04-01 16:42:08.735000+00:00
modified: 2025-10-24 17:49:22.536000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]


Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from [System Location Discovery](https://attack.mitre.org/techniques/T1614) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings.(Citation: FBI Ragnar Locker 2020)(Citation: Sophos Geolocation 2016)(Citation: Bleepingcomputer RAT malware 2020) Windows API functions such as <code>GetLocaleInfoW</code> can also be used to determine the locale of the host.(Citation: FBI Ragnar Locker 2020) In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance.(Citation: AWS Instance Identity Documents)(Citation: Microsoft Azure Instance Metadata 2021)

Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.(Citation: Securelist Trasparent Tribe 2020)(Citation: Sophos Geolocation 2016)

## Subtechniques

### T1614.001: System Language Discovery
^t1614001-system-language-discovery

**Parent Technique**
- [[T1614-system_location_discovery|T1614: System Location Discovery]]

**Tactic**
- [[discovery|Discovery]]

Adversaries may attempt to gather information about the system language of a victim in order to infer the geographical location of that host. This information may be used to shape follow-on behaviors, including whether the adversary infects the target and/or attempts specific actions. This decision may be employed by malware developers and operators to reduce their risk of attracting the attention of specific law enforcement agencies or prosecution/scrutiny from other entities.(Citation: Malware System Language Check)

There are various sources of data an adversary could use to infer system language, such as system defaults and keyboard layouts. Specific checks will vary based on the target and/or adversary, but may involve behaviors such as [Query Registry](https://attack.mitre.org/techniques/T1012) and calls to [Native API](https://attack.mitre.org/techniques/T1106) functions.(Citation: CrowdStrike Ryuk January 2019) 

For example, on a Windows system adversaries may attempt to infer the language of a system by querying the registry key <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language</code> or parsing the outputs of Windows API functions <code>GetUserDefaultUILanguage</code>, <code>GetSystemDefaultUILanguage</code>, <code>GetKeyboardLayoutList</code> and <code>GetUserDefaultLangID</code>.(Citation: Darkside Ransomware Cybereason)(Citation: Securelist JSWorm)(Citation: SecureList SynAck Doppelgänging May 2018)

On a macOS or Linux system, adversaries may query <code>locale</code> to retrieve the value of the <code>$LANG</code> environment variable.

#### Properties

- id: T1614.001
- name: System Language Discovery
- created: 2021-08-18 14:06:45.244000+00:00
- modified: 2025-10-24 17:49:20.039000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Platforms

- IaaS
- Linux
- macOS
- Windows

## Tools

- [[quasarrat|QuasarRAT]]

