FastOrder API Outage Postmortem
Table of Contents
Issue Summary
Timeline
Root Cause and Resolution
Corrective and Preventative Measures
Issue Summary
Duration:
2 hours and 15 minutes (10:30 AM - 12:45 PM UTC) on August 22, 2024.

Impact:
The "FastOrder" API service, integral to the "QuickEats" food delivery app, experienced severe slowness. This affected approximately 75% of users, leading to delayed or failed order processing, significantly impacting user satisfaction.

Root Cause:
A misconfigured API gateway routing policy caused an unexpected surge in server load, overwhelming the database connection pool and creating a processing bottleneck.

Timeline
10:30 AM
Monitoring alert triggered by excessive API response times.

10:32 AM
Engineers on call confirmed high latency in the order processing API.

10:40 AM
Initial investigation focused on database performance, suspecting potential overload due to high traffic.

10:55 AM
Database queries optimized and cache cleared, but no improvement was noticed.

11:15 AM
Further investigation revealed no issues with the database, prompting a review of the API gateway logs.

11:30 AM
Misleading path taken when engineers suspected a memory leak in the API server.

11:50 AM
Escalated to the DevOps team; deeper analysis of API gateway and server metrics initiated.

12:10 PM
Root cause identified as a misconfigured API gateway routing policy causing traffic overload on a single instance.

12:30 PM
Configuration fixed, traffic balanced across all instances; service recovery observed.

12:45 PM
Full service restored; API response times returned to normal.

Root Cause and Resolution
Root Cause
The root cause was an incorrect routing policy in the API gateway configuration. A recent update led to a load-balancing rule being misconfigured, which funneled 90% of incoming traffic to a single server instance. This server became overwhelmed, leading to saturation of the database connection pool and a subsequent bottleneck in order processing.

Resolution
The issue was resolved by updating the API gateway configuration to correctly distribute traffic across all server instances. Additionally, the database connection pool size was temporarily increased to handle the backlog of requests until the system stabilized.

Corrective and Preventative Measures
Improvements
API Gateway Configuration Validation: Implemented stricter validation checks for API gateway configuration changes to prevent similar misconfigurations in the future.
Enhanced Monitoring: Introduced more granular monitoring metrics for server load distribution and database connection pool usage.
Incident Response Protocol: Improved protocol to escalate API gateway-related issues earlier in the investigation process.
TODO List
Update API Gateway Configuration: Review and patch the configuration rules to ensure balanced traffic distribution across all instances.
Add Load Balancing Monitoring: Integrate monitoring tools that track real-time traffic distribution across server instances.
Expand Incident Playbook: Document this incident and update the incident response playbook to include checks on API gateway configurations.
Increase Connection Pool Alerts: Set up alerts for unusual spikes in database connection pool usage to preempt future issues.
This README file serves as documentation for the "FastOrder" API service outage that occurred on August 22, 2024. The outlined corrective and preventative measures are intended to prevent similar issues from recurring and to improve the resilience of the service in the future. 
