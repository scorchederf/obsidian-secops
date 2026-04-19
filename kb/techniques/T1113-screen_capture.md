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


## Platforms

- Linux
- Windows
- macOS

## Tools

- [[asyncrat|AsyncRAT]]
- [[brute_ratel_c4|Brute Ratel C4]]
- [[connectwise|ConnectWise]]
- [[empire|Empire]]
- [[pcshare|PcShare]]
- [[powersploit|PowerSploit]]
- [[pupy|Pupy]]
- [[quick_assist|Quick Assist]]
- [[remcos|Remcos]]
- [[remoteutilities|RemoteUtilities]]
- [[silenttrinity|SILENTTRINITY]]
- [[sliver|Sliver]]

