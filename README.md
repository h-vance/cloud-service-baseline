# Cloud Service Baseline

A reference architecture for a minimal but production-ready cloud service. This repository provides a baseline for deploying, monitoring, and troubleshooting cloud-native applications with a focus on security, observability, and operational excellence.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![systemd](https://img.shields.io/badge/systemd-1A1A1A?style=for-the-badge&logo=linux&logoColor=white)](https://systemd.io/)
[![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)](https://www.terraform.io/)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.linux.org/)
[![DevOps](https://img.shields.io/badge/DevOps-007ACC?style=for-the-badge)](https://en.wikipedia.org/wiki/DevOps)

## System Architecture

- **Application Layer**: Python-based FastAPI application providing secure REST endpoints and integrated health checks.
- **Deployment Models**: Optimized for both containerized (Docker) and bare-metal/VM (systemd) environments.
- **Security Hardening**: Implementation of the Principle of Least Privilege (POLP) at the service and infrastructure levels.
- **Observability**: Structured JSON logging, automated health monitoring, and performance tracking.

## Core Features

- **Hardened Systemd Configuration**: Production-grade unit files with sandboxing and resource limits.
- **Infrastructure as Code**: Terraform modules for automated AWS resource provisioning.
- **Containerization**: Multi-stage Docker builds for minimal image size and reduced attack surface.
- **Health and Readiness**: Dedicated endpoints for integration with load balancers and service meshes.

## Operational Triage Workflow

When a service failure occurs, follow this systematic diagnostic approach:

1. **Connectivity Verification**:
   - Check external reachability: `curl -I http://<host>:<port>/health`
   - Validate local binding: `ss -tulpn | grep <port>`
2. **Process Integrity**:
   - Check service status: `systemctl status cloud-service` or `docker ps`
3. **Resource Inspection**:
   - Analyze Disk (`df -h`), Memory (`free -h`), and CPU (`top`) usage to identify resource exhaustion.
4. **Log Analysis**:
   - Inspect real-time application logs: `journalctl -u cloud-service -f`

## Setup and Installation

### Local Development
1. Install requirements:
   ```bash
   pip install -r app/requirements.txt
   ```
2. Run the application:
   ```bash
   python app/app.py
   ```

### Production Deployment (systemd)
1. Copy the unit file: `cp deploy/systemd/cloud-service.service /etc/systemd/system/`
2. Enable and start the service:
   ```bash
   systemctl daemon-reload
   systemctl enable --now cloud-service
   ```

### Containerized Deployment
```bash
docker-compose up --build -d
```

## Repository Structure

- `app/`: FastAPI application source code and business logic.
- `deploy/`: Production deployment artifacts (systemd, configurations).
- `infra/`: Terraform modules for cloud infrastructure provisioning.
- `scripts/`: Operational scripts for maintenance and deployment automation.
- `tests/`: Comprehensive test suite covering unit and integration tests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
