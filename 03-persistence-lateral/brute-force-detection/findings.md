# Chapter 2: Brute Force Detection

## Attack Summary
Tool Used: Hydra v9.5
Target: Windows Server 2025
Account: Administrator
Protocol: SSH (Port 22)
Attempts: 12 failed logins
Time: 5/28/2026 01:26:08 AM

## Detection Method
- Windows Event ID 4625
- Splunk correlation search
- PowerShell log analysis

## Evidence
- screenshot-event-viewer.png
- screenshot-powershell.png
- screenshot-splunk.png

## MITRE ATT&CK
T1110.001 - Brute Force: Password Guessing

## Recommendation
Block IP after 5 failed attempts
Enable account lockout policy