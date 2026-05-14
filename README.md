# Cloud Service Baseline

> **Baseline health validation and configuration verification for cloud service deployments.**

## Overview

A reference implementation for validating that a cloud service meets operational readiness before going live. Includes a Flask health-check API, structured logging, Terraform IAM provisioning, systemd service management, and automated test coverage.

## Structure

```
.
├── app/
│   ├── app.py                      # Flask API with health and readiness endpoints
│   ├── logging_config.json         # Structured JSON logging configuration
│   └── requirements.txt            # Python dependencies
├── scripts/
│   └── health-check.sh             # Bash health-check script for cron or monitoring
├── deploy/
│   └── systemd/
│       └── service-baseline.service # systemd unit file for service management
├── infra/
│   ├── main.tf                     # Terraform infrastructure definition
│   └── iam.tf                      # IAM role and policy provisioning
├── tests/
│   └── test_app.py                 # Pytest test suite
├── docker-compose.yml              # Local development compose
└── Dockerfile                      # Container build
```

## Getting Started

```bash
pip install -r app/requirements.txt
python app/app.py
```

Run tests:
```bash
pytest tests/
```

Docker:
```bash
docker-compose up
```

---
*Maintained by Harrison Vance — Technical Support & Operations*
