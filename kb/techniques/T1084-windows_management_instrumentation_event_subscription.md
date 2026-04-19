---
id: T1084
name: Windows Management Instrumentation Event Subscription
created: 2017-05-31 21:31:05.140000+00:00
modified: 2025-10-24 17:49:33.155000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[persistence|Persistence]]

Windows Management Instrumentation (WMI) can be used to install event filters, providers, consumers, and bindings that execute code when a defined event occurs. Adversaries may use the capabilities of WMI to subscribe to an event and execute arbitrary code when that event occurs, providing persistence on a system. Adversaries may attempt to evade detection of this technique by compiling WMI scripts into Windows Management Object (MOF) files (.mof extension). (Citation: Dell WMI Persistence) Examples of events that may be subscribed to are the wall clock time or the computer's uptime. (Citation: Kazanciyan 2014) Several threat groups have reportedly used this technique to maintain persistence. (Citation: Mandiant M-Trends 2015)

## Properties

- id: T1084
- name: Windows Management Instrumentation Event Subscription
- created: 2017-05-31 21:31:05.140000+00:00
- modified: 2025-10-24 17:49:33.155000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Platforms

- Windows

