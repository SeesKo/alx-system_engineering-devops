# Postmortem Report: Apache Docker Container Outage #

### Incident Date: March 25, 2024


## Issue Summary

**Duration of Outage:** The outage lasted for approximately 45 minutes, starting at 3:00 PM and ending at 3:45 PM (UTC).

**Impact:** The web service running on Apache inside a Docker container was inaccessible, affecting all users attempting to access the service. Approximately 100% of users were unable to access the site during the outage.
**Root Cause:** The root cause was that the Apache service inside the Docker container was not started due to a misconfiguration in the Docker container setup process.


##Timeline

- **3:00 PM UTC:** The outage was detected when the system monitoring dashboard showed that the web server was not responding to requests.
- **3:05 PM UTC:** The on-call engineer received an alert indicating that the service was unavailable.
- **3:10 PM UTC:** The on-call engineer logged into the Docker container to investigate. Initial checks indicated that the Apache service was not running.
- **3:15 PM UTC:** The engineer attempted to restart the Docker container, assuming that it was a transient issue, but the issue persisted.
- **3:25 PM UTC:** The incident was escalated to the DevOps team for further analysis.
- **3:30 PM UTC:** The DevOps team identified that the Apache service was not starting automatically inside the Docker container.
- **3:35 PM UTC:** The DevOps team manually started the Apache service, restoring access to the web server.
- **3:45 PM UTC:** The web service was fully operational, and the outage was resolved.


## Root Cause and Resolution

The root cause of the outage was a misconfiguration in the Docker container setup. The Apache service was not configured to start automatically when the container launched. This led to a situation where the container was running, but the web server was not.  

To resolve the issue, the DevOps team manually started the Apache service using the command service apache2 start. This restored access to the web server, resolving the outage.


##Corrective and Preventative Measures

To prevent this issue from happening again, the following corrective and preventative measures were identified:

1. **Update Docker Configuration:** Ensure that the Docker container setup includes a script or configuration to automatically start the Apache service when the container is launched.
2. **Automate Service Checks:** Implement automated checks to confirm that critical services, such as Apache, are running after a container is started.
3. **Improve Monitoring and Alerts:** Add monitoring to detect if a critical service is not running and create alerts to notify engineers immediately.
4. **Review Deployment Process:** Conduct a review of the Docker container deployment process to identify and correct any other potential misconfigurations.
5. **Training for On-Call Engineers:** Provide additional training for on-call engineers to handle similar issues in the future, ensuring they can quickly diagnose and resolve problems.

By implementing these corrective and preventative measures, the team aims to minimize the risk of similar outages and ensure a more reliable web service.
