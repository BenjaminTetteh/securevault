# SecureVault Monitoring

## CloudWatch Alarms

| Alarm | Metric | Threshold | Action |
|---|---|---|---|
| SecureVault-Environment-Health | EnvironmentHealth | >= 20 (Degraded) | Email via SNS |
| SecureVault-5xx-Errors | ApplicationRequests5xx | >= 5 in 5 mins | Email via SNS |

## Alert Response Runbook

### Environment Health Alarm
1. Check EB environment logs: `eb logs`
2. Check running Docker container
3. Redeploy last known good version if needed

### 5xx Error Alarm
1. Check application logs for stack traces
2. Identify which endpoint is failing
3. Roll back recent deployment if correlated