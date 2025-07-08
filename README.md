# Honeypot Repository Example

**This repository is a honeypot for educational and demonstration purposes only.**

## Tracking & Alerts

- **Stars:** When someone stars this repository, a GitHub Action triggers an alert (see `.github/workflows/star-alert.yml`).
- **Webhooks:** This repository uses webhooks to track stars, forks, and other public events for monitoring and educational purposes.
- **Cloning:** Direct clone events are not tracked, but interaction with included scripts (like `honeypot_logger.py`) will be logged locally.

> All tracking is for demonstration and security research purposes only. No sensitive data is collected.

---
