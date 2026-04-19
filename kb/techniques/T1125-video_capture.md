---
id: T1125
name: Video Capture
created: 2017-05-31 21:31:37.917000+00:00
modified: 2025-10-24 17:48:56.077000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[collection|Collection]]

An adversary can leverage a computer's peripheral devices (e.g., integrated cameras or webcams) or applications (e.g., video call services) to capture video recordings for the purpose of gathering information. Images may also be captured from devices or applications, potentially in specified intervals, in lieu of video files.

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture video or images. Video or image files may be written to disk and exfiltrated later. This technique differs from [Screen Capture](https://attack.mitre.org/techniques/T1113) due to use of specific devices or applications for video recording rather than capturing the victim's screen.

In macOS, there are a few different malware samples that record the user's webcam such as FruitFly and Proton. (Citation: objective-see 2017 review)

## Properties

- id: T1125
- name: Video Capture
- created: 2017-05-31 21:31:37.917000+00:00
- modified: 2025-10-24 17:48:56.077000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Platforms

- Windows
- macOS
- Linux

## Tools

- [[S0192-pupy|S0192: Pupy]]
- [[S0262-quasarrat|S0262: QuasarRAT]]
- [[S0332-remcos|S0332: Remcos]]
- [[S0363-empire|S0363: Empire]]
- [[S0434-imminent_monitor|S0434: Imminent Monitor]]
- [[S0591-connectwise|S0591: ConnectWise]]
- [[S1050-pcshare|S1050: PcShare]]
- [[S1087-asyncrat|S1087: AsyncRAT]]
- [[S1209-quick_assist|S1209: Quick Assist]]

