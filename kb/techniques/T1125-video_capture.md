---
mitre_id: "T1125"
mitre_name: "Video Capture"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--6faf650d-bf31-4eb4-802d-1000cf38efaf"
mitre_created: "2017-05-31T21:31:37.917Z"
mitre_modified: "2025-10-24T17:48:56.077Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1125/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "macOS"
  - "Linux"
mitre_tactic_ids:
  - "TA0009"
---

# T1125: Video Capture

An adversary can leverage a computer's peripheral devices (e.g., integrated cameras or webcams) or applications (e.g., video call services) to capture video recordings for the purpose of gathering information. Images may also be captured from devices or applications, potentially in specified intervals, in lieu of video files.

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture video or images. Video or image files may be written to disk and exfiltrated later. This technique differs from [[T1113-screen_capture|T1113: Screen Capture]] due to use of specific devices or applications for video recording rather than capturing the victim's screen.

In macOS, there are a few different malware samples that record the user's webcam such as FruitFly and Proton. (Citation: objective-see 2017 review)

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## Tools

- [[pupy|Pupy]]
- [[quasarrat|QuasarRAT]]
- [[remcos|Remcos]]
- [[empire|Empire]]
- [[imminent_monitor|Imminent Monitor]]
- [[connectwise|ConnectWise]]
- [[pcshare|PcShare]]
- [[asyncrat|AsyncRAT]]
- [[quick_assist|Quick Assist]]

## Platforms

- Windows
- macOS
- Linux

