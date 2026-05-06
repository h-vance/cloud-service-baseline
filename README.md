# Cloud Service Baseline

A reference architecture for a minimal but production-ready cloud service. This repository provides a baseline for deploying, monitoring, and troubleshooting cloud-native applications with a focus on security, observability, and operational excellence.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9IiNmZmYiIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZD0iTTYuNzYzIDEwLjAzNnEuMDAyLjQ0Ni4wODguNzFjLjA2NC4xNzYuMTQ0LjM2OC4yNTYuNTc2LjA0LjA2My4wNTYuMTI3LjA1Ni4xODNxLjAwMi4xMi0uMTUyLjI0bC0uNTAzLjMzNWEuNC40IDAgMCAxLS4yMDguMDcycS0uMTItLjAwMi0uMjM5LS4xMTJhMi41IDIuNSAwIDAgMS0uMjg3LS4zNzUgNiA2IDAgMCAxLS4yNDgtLjQ3MXEtLjkzNCAxLjEwMS0yLjM0NyAxLjEwMWMtLjY3IDAtMS4yMDUtLjE5MS0xLjU5Ni0uNTc0cS0uNTg4LS41NzUtLjU5LTEuNTMzYzAtLjY3OC4yMzktMS4yMy43MjYtMS42NDQuNDg3LS40MTUgMS4xMzMtLjYyMyAxLjk1NS0uNjIzLjI3MiAwIC41NTEuMDI0Ljg0Ni4wNjQuMjk2LjA0LjYuMTA0LjkxOC4xNzZ2LS41ODNxLS4wMDEtLjkwOS0uMzc1LTEuMjc3Yy0uMjU1LS4yNDgtLjY4Ni0uMzY3LTEuMy0uMzY3LS4yOCAwLS41NjguMDMxLS44NjMuMTAzcS0uNDQzLjEwNi0uODYyLjI3MmEyIDIgMCAwIDEtLjI4LjEwNC41LjUgMCAwIDEtLjEyNy4wMjNxLS4xNjguMDAyLS4xNjgtLjI0N3YtLjM5MWMwLS4xMjguMDE2LS4yMjQuMDU2LS4yOGEuNi42IDAgMCAxIC4yMjQtLjE2NyA0LjYgNC42IDAgMCAxIDEuMDA1LS4zNiA0LjggNC44IDAgMCAxIDEuMjQ2LS4xNTFjLjk1IDAgMS42NDQuMjE2IDIuMDkxLjY0N3EuNjYuNjQ1LjY2MiAxLjk2M3YyLjU4NnptLTMuMjQgMS4yMTRjLjI2MyAwIC41MzQtLjA0OC44MjItLjE0NGExLjggMS44IDAgMCAwIC43NTgtLjUxIDEuMyAxLjMgMCAwIDAgLjI3Mi0uNTEyYy4wNDctLjE5MS4wOC0uNDIzLjA4LS42OTR2LS4zMzVhNyA3IDAgMCAwLS43MzUtLjEzNiA2IDYgMCAwIDAtLjc1LS4wNDhjLS41MzUgMC0uOTI2LjEwNC0xLjE5LjMyLS4yNjMuMjE1LS4zOS41MTgtLjM5LjkxNyAwIC4zNzUuMDk1LjY1NS4yOTUuODQ2LjE5MS4yLjQ3LjI5Ni44MzguMjk2bTYuNDEuODYyYy0uMTQ0IDAtLjI0LS4wMjQtLjMwNC0uMDgtLjA2NC0uMDQ4LS4xMi0uMTYtLjE2OC0uMzExTDcuNTg2IDUuNTVhMS40IDEuNCAwIDAgMS0uMDcyLS4zMmMwLS4xMjguMDY0LS4yLjE5MS0uMmguNzgzcS4yMjctLjAwMS4zMS4wOGMuMDY1LjA0OC4xMTMuMTYuMTYuMzEybDEuMzQyIDUuMjg0IDEuMjQ1LTUuMjg0cS4wNTgtLjI0LjE1MS0uMzEyYS41NS41NSAwIDAgMSAuMzItLjA4aC42MzhjLjE1MiAwIC4yNTYuMDI1LjMyLjA4LjA2My4wNDguMTIuMTYuMTUxLjMxMmwxLjI2MSA1LjM0OCAxLjM4MS01LjM0OHEuMDc0LS4yNC4xNi0uMzEyYS41Mi41MiAwIDAgMSAuMzExLS4wOGguNzQzYy4xMjcgMCAuMi4wNjUuMi4yIDAgLjA0LS4wMDkuMDgtLjAxNy4xMjhhMSAxIDAgMCAxLS4wNTYuMmwtMS45MjMgNi4xN3EtLjA3Mi4yNC0uMTY4LjMxMWEuNS41IDAgMCAxLS4zMDMuMDhoLS42ODdjLS4xNTEgMC0uMjU1LS4wMjQtLjMyLS4wOC0uMDYzLS4wNTYtLjExOS0uMTYtLjE1LS4zMmwtMS4yMzgtNS4xNDgtMS4yMyA1LjE0Yy0uMDQuMTYtLjA4Ny4yNjQtLjE1LjMyLS4wNjUuMDU2LS4xNzcuMDgtLjMyLjA4em0xMC4yNTYuMjE1Yy0uNDE1IDAtLjgzLS4wNDgtMS4yMjktLjE0My0uMzk5LS4wOTYtLjcxLS4yLS45MTgtLjMyLS4xMjgtLjA3MS0uMjE1LS4xNTEtLjI0Ny0uMjIzYS42LjYgMCAwIDEtLjA0OC0uMjI0di0uNDA3YzAtLjE2Ny4wNjQtLjI0Ny4xODMtLjI0N3EuMDcyIDAgLjE0NC4wMjRjLjA0OC4wMTYuMTIuMDQ4LjIuMDhxLjQwOC4xODEuODc4LjI3OWMuMzE5LjA2NC42My4wOTYuOTUuMDk2LjUwMiAwIC44OTQtLjA4OCAxLjE2NS0uMjY0YS44Ni44NiAwIDAgMCAuNDE1LS43NTguNzguNzggMCAwIDAtLjIxNS0uNTU5Yy0uMTQ0LS4xNTEtLjQxNi0uMjg3LS44MDctLjQxNWwtMS4xNTctLjM2Yy0uNTgzLS4xODMtMS4wMTQtLjQ1NC0xLjI3Ny0uODEzYTEuOSAxLjkgMCAwIDEtLjQtMS4xNThxMC0uNTAyLjIxNi0uODg2Yy4xNDQtLjI1NS4zMzUtLjQ3OS41NzUtLjY1NC4yNC0uMTg0LjUxLS4zMi44My0uNDE1LjMyLS4wOTYuNjU1LS4xMzYgMS4wMDYtLjEzNi4xNzUgMCAuMzU5LjAwOC41MzUuMDMyLjE4My4wMjQuMzUuMDU2LjUxOC4wODhxLjI0LjA1OC40NTUuMTI3LjIxNi4wNzIuMzM2LjE0NGEuNy43IDAgMCAxIC4yNC4yLjQzLjQzIDAgMCAxIC4wNzEuMjYzdi4zNzVxLS4wMDIuMjU0LS4xODQuMjU2YS44LjggMCAwIDEtLjMwMy0uMDk2IDMuNjUgMy42NSAwIDAgMC0xLjUzMi0uMzExYy0uNDU1IDAtLjgxNS4wNzEtMS4wNjIuMjIzcy0uMzc1LjM4My0uMzc1LjcxYzAgLjIyNC4wOC40MTYuMjQuNTY3LjE1OS4xNTIuNDU0LjMwNC44NzcuNDRsMS4xMzQuMzU4Yy41NzQuMTg0Ljk5LjQ0IDEuMjM3Ljc2N3MuMzY3LjcwMi4zNjcgMS4xMTdjMCAuMzQzLS4wNzIuNjU1LS4yMDcuOTI2YTIuMiAyLjIgMCAwIDEtLjU4My43MDNjLS4yNDguMi0uNTQzLjM0My0uODg2LjQ0Ny0uMzYuMTExLS43MzQuMTY3LTEuMTQyLjE2N20xLjUwOSAzLjg4Yy0yLjYyNiAxLjk0LTYuNDQyIDIuOTY5LTkuNzIyIDIuOTY5LTQuNTk4IDAtOC43NC0xLjctMTEuODctNC41MjYtLjI0Ny0uMjIzLS4wMjQtLjUyNy4yNzItLjM1MSAzLjM4NCAxLjk2MyA3LjU1OSAzLjE1MyAxMS44NzcgMy4xNTMgMi45MTQgMCA2LjExNC0uNjA3IDkuMDYtMS44NTIuNDM5LS4yLjgxNC4yODcuMzgzLjYwN20xLjA5NC0xLjI0NmMtLjMzNi0uNDMtMi4yMi0uMjA3LTMuMDc0LS4xMDMtLjI1NS4wMzItLjI5NS0uMTkyLS4wNjMtLjM2IDEuNS0xLjA1MyAzLjk2Ny0uNzUgNC4yNTQtLjM5OS4yODcuMzYtLjA4IDIuODI2LTEuNDg1IDQuMDA3LS4yMTUuMTg0LS40MjMuMDg4LS4zMjctLjE1MS4zMi0uNzkgMS4wMy0yLjU3LjY5NS0yLjk5NCIvPjwvc3ZnPg==&logoColor=white)](https://aws.amazon.com/)
[![systemd](https://img.shields.io/badge/systemd-1A1A1A?style=for-the-badge&logo=linux&logoColor=white)](https://systemd.io/)
[![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)](https://www.terraform.io/)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=white)](https://www.linux.org/)
[![DevOps](https://img.shields.io/badge/DevOps-007ACC?style=for-the-badge&logo=azuredevops&logoColor=white)](https://en.wikipedia.org/wiki/DevOps)

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
