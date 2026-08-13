# Cloud Service Baseline

> **Baseline health validation and configuration verification for cloud service deployments.**

[![Python](https://www.shieldcn.dev/badge/Python-3776AB.svg?variant=default&logo=Python&logoColor=FFFFFF&size=xs)](https://python.org)&nbsp;[![Docker](https://www.shieldcn.dev/badge/Docker-2496ED.svg?variant=default&logo=Docker&logoColor=FFFFFF&size=xs)](https://docker.com)&nbsp;[![Terraform](https://www.shieldcn.dev/badge/Terraform-844FBA.svg?variant=default&logo=Terraform&logoColor=FFFFFF&size=xs)](https://terraform.io)&nbsp;[![GNU Bash](https://www.shieldcn.dev/badge/GNU%20Bash-4EAA25.svg?variant=default&logo=GNU+Bash&logoColor=FFFFFF&size=xs)](https://www.gnu.org/software/bash/)&nbsp;[![Linux](https://www.shieldcn.dev/badge/Linux-222222.svg?variant=default&logo=Linux&logoColor=FCC624&size=xs)](https://kernel.org)

---

## The Problem

**The Symptom:** Teams deployed cloud services without a consistent readiness checklist. Health endpoints were an afterthought, IAM permissions were overly permissive, and there was no standard way to validate that a service was actually operational before routing traffic to it.

**The Investigation:** Every service had a different idea of what "healthy" meant. Some had no health endpoint at all. Logging was inconsistent. Infrastructure was provisioned manually without security hardening. Onboarding a new service meant reverse-engineering its operational model from scratch.

**The Resolution:** A reference implementation that codifies operational readiness into a single deployable unit: a FastAPI health-check API with structured logging, Terraform-provisioned IAM with least-privilege access, Docker multi-stage builds with a non-root user, systemd integration with security hardening, and a health-check script for monitoring integration.

---

## API Endpoints

| Method | Path | Purpose |
| ------- | ------ | --------- |
| GET | `/health` | Load balancer and K8s probe endpoint, returns status, uptime, and version |
| GET | `/api/v1/data` | Sample data endpoint with structured request tracing |
| POST | `/admin/toggle-health` | Test-only, simulates healthy/unhealthy state |
| GET | `/api/v1/simulate-timeout` | Test-only, simulates slow responses for timeout testing (default 40s) |

### Health Check Response

```json
GET /health

{
  "status": "healthy",
  "uptime_seconds": 8472.31,
  "version": "1.0.0"
}
```

When toggled unhealthy, the endpoint returns `503 Service Unavailable`, allowing load balancers and orchestrators to test their health check failure handling.

---

## Infrastructure

### Terraform (`infra/`)

| Resource | Detail |
| ---------- | -------- |
| EC2 Instance | `t3.micro`, Amazon Linux 2, IMDSv2 enforced |
| Root Volume | Encrypted |
| IAM Role | EC2 assume-role with least-privilege S3 read-only policy |
| Security Group | Managed separately for service access control |

```bash
cd infra
terraform init
terraform apply
```

### IAM Policy

The instance role grants only `s3:GetObject` and `s3:ListBucket`, with no write or delete permissions. Expand the policy in `iam.tf` as the service's data access requirements grow.

---

## Containerization

### Docker (Multi-Stage Build)

```dockerfile
# Builder stage: install dependencies into a virtual environment
FROM python:3.11-slim AS builder
# Runtime stage: non-root user, distroless-style
FROM python:3.11-slim
```

- Dependencies installed in a virtual environment in the builder stage
- Runtime image is a clean `python:3.11-slim` with no build tools
- Runs as `serviceuser` (non-root) with owned application files
- Exposes port 8000

```bash
# Build and run
docker build -t service-baseline .
docker run -p 8000:8000 service-baseline
```

### Docker Compose

```bash
docker-compose up
```

The compose configuration includes:
- Health check configured against `/health` with 30s interval
- `LOG_LEVEL` environment variable passthrough
- Automatic restart on failure

---

## Deployment

### systemd Service

The `deploy/systemd/service-baseline.service` unit includes production hardening:

```ini
[Service]
User=service-user
Restart=on-failure
RestartSec=5s
LimitNOFILE=65535
MemoryLimit=512M
PrivateTmp=true
ProtectSystem=full
NoNewPrivileges=true
```

Deploy to the target server:

```bash
sudo cp deploy/systemd/service-baseline.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl enable --now service-baseline
```

### Health Check Script

The `scripts/health-check.sh` script performs up to 5 retries against the `/health` endpoint with 5-second intervals. Useful for monitoring integration or CI/CD gates:

```bash
./scripts/health-check.sh http://localhost:8000/health
```

Returns exit code 0 on success, 1 on failure.

---

## Development

```bash
# Install dependencies
pip install -r app/requirements.txt

# Run the API
uvicorn app.app:app --reload --port 8000

# Run tests
pytest tests/ -v
```

The test suite covers:
- Health check returns 200 and correct status
- Toggle unhealthy returns 503
- Data endpoint returns expected payload shape
- Logging handles missing `request_id` gracefully (no Logging errors)

---

## Prerequisites

- **Python 3.11+**
- **Docker** and Docker Compose (for containerized deployment)
- **Terraform** 1.x (for AWS infrastructure)
- **AWS CLI** configured (for Terraform apply)
- **curl** (for health-check script)

---

## Repository Structure

```text
.
├── app/
│   ├── app.py                      # FastAPI application with health/data/timeout endpoints
│   ├── logging_config.json         # Structured JSON logging configuration
│   └── requirements.txt            # Python dependencies (FastAPI, uvicorn, pytest)
├── scripts/
│   └── health-check.sh             # Retry-based health check for monitoring integration
├── deploy/
│   └── systemd/
│       └── service-baseline.service # Production systemd unit with security hardening
├── infra/
│   ├── main.tf                     # EC2 instance with IMDSv2 and encrypted volumes
│   └── iam.tf                      # Least-privilege IAM role (S3 read-only)
├── tests/
│   └── test_app.py                 # Pytest test suite
├── docker-compose.yml              # Local development with health check
└── Dockerfile                      # Multi-stage container build
```

---

## Related Repositories

| Repository | Description |
| ---------- | ----------- |
| [**self-healing-microservices-cluster**](https://github.com/h-vance/self-healing-microservices-cluster) | Automated infrastructure recovery and observability for containerized microservices |
| [**ops-diagnostics**](https://github.com/h-vance/ops-diagnostics) | Python & Bash diagnostic scripts for automated health verification, log analysis, and system profiling |
| [**cloud-operations-runbook**](https://github.com/h-vance/cloud-operations-runbook) | Structured triage checklists and SOPs for network, system, and application fault isolation |
| [**incident-postmortems**](https://github.com/h-vance/incident-postmortems) | Blameless RCAs documenting how baseline failures were diagnosed and resolved |

---

Maintained by Harrison Vance, Technical Support Engineer
