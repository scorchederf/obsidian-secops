---
id: T1113
name: Screen Capture
created: 2017-05-31 21:31:25.060000+00:00
modified: 2025-10-24 17:48:19.886000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[collection|Collection]]

Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation. Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations. Taking a screenshot is also typically possible through native utilities or API calls, such as <code>CopyFromScreen</code>, <code>xwd</code>, or <code>screencapture</code>.(Citation: CopyFromScreen .NET)(Citation: Antiquated Mac Malware)


## Properties

- id: T1113
- name: Screen Capture
- created: 2017-05-31 21:31:25.060000+00:00
- modified: 2025-10-24 17:48:19.886000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Platforms

- Linux
- Windows
- macOS

## Tools

- [[S0192-pupy|S0192: Pupy]]
- [[S0194-powersploit|S0194: PowerSploit]]
- [[S0332-remcos|S0332: Remcos]]
- [[S0363-empire|S0363: Empire]]
- [[S0591-connectwise|S0591: ConnectWise]]
- [[S0592-remoteutilities|S0592: RemoteUtilities]]
- [[S0633-sliver|S0633: Sliver]]
- [[S0692-silenttrinity|S0692: SILENTTRINITY]]
- [[S1050-pcshare|S1050: PcShare]]
- [[S1063-brute_ratel_c4|S1063: Brute Ratel C4]]
- [[S1087-asyncrat|S1087: AsyncRAT]]
- [[S1209-quick_assist|S1209: Quick Assist]]

