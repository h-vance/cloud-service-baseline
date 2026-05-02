# Cloud Service Baseline

A reference architecture for a minimal but production-ready cloud service. This repository provides a baseline for deploying, monitoring, and troubleshooting cloud-native applications with a focus on security, observability, and operational excellence.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBpZD0iYTAiPjx0aXRsZT5BbWF6b24gQVdTPC90aXRsZT48cGF0aCBkPSJNNi43NjMgMTAuMDM2YzAgLjI5Ni4wMzIuNTM1LjA4OC43MS4wNjQuMTc2LjE0NC4zNjguMjU2LjU3Ni4wNC4wNjMuMDU2LjEyNy4wNTYuMTgzIDAgLjA4LS4wNDguMTYtLjE1Mi4yNGwtLjUwMy4zMzVhLjM4My4zODMgMCAwIDEtLjIwOC4wNzJjLS4wOCAwLS4xNi0uMDQtLjIzOS0uMTEyYTIuNDcgMi40NyAwIDAgMS0uMjg3LS4zNzUgNi4xOCA2LjE4IDAgMCAxLS4yNDgtLjQ3MWMtLjYyMi43MzQtMS40MDUgMS4xMDEtMi4zNDcgMS4xMDEtLjY3IDAtMS4yMDUtLjE5MS0xLjU5Ni0uNTc0LS4zOTEtLjM4NC0uNTktLjg5NC0uNTktMS41MzMgMC0uNjc4LjIzOS0xLjIzLjcyNi0xLjY0NC40ODctLjQxNSAxLjEzMy0uNjIzIDEuOTU1LS42MjMuMjcyIDAgLjU1MS4wMjQuODQ2LjA2NC4yOTYuMDQuNi4xMDQuOTE4LjE3NnYtLjU4M2MwLS42MDctLjEyNy0xLjAzLS4zNzUtMS4yNzctLjI1NS0uMjQ4LS42ODYtLjM2Ny0xLjMtLjM2Ny0uMjggMC0uNTY4LjAzMS0uODYzLjEwMy0uMjk1LjA3Mi0uNTgzLjE2LS44NjIuMjcyYTIuMjg3IDIuMjg3IDAgMCAxLS4yOC4xMDQuNDg4LjQ4OCAwIDAgMS0uMTI3LjAyM2MtLjExMiAwLS4xNjgtLjA4LS4xNjgtLjI0N3YtLjM5MWMwLS4xMjguMDE2LS4yMjQuMDU2LS4yOGEuNTk3LjU5NyAwIDAgMSAuMjI0LS4xNjdjLjI3OS0uMTQ0LjYxNC0uMjY0IDEuMDA1LS4zNmE0Ljg0IDQuODQgMCAwIDEgMS4yNDYtLjE1MWMuOTUgMCAxLjY0NC4yMTYgMi4wOTEuNjQ3LjQzOS40My42NjIgMS4wODUuNjYyIDEuOTYzdjIuNTg2em0tMy4yNCAxLjIxNGMuMjYzIDAgLjUzNC0uMDQ4LjgyMi0uMTQ0LjI4Ny0uMDk2LjU0My0uMjcxLjc1OC0uNTEuMTI4LS4xNTIuMjI0LS4zMi4yNzItLjUxMi4wNDctLjE5MS4wOC0uNDIzLjA4LS42OTR2LS4zMzVhNi42NiA2LjY2IDAgMCAwLS43MzUtLjEzNiA2LjAyIDYuMDIgMCAwIDAtLjc1LS4wNDhjLS41MzUgMC0uOTI2LjEwNC0xLjE5LjMyLS4yNjMuMjE1LS4zOS41MTgtLjM5LjkxNyAwIC4zNzUuMDk1LjY1NS4yOTUuODQ2LjE5MS4yLjQ3LjI5Ni44MzguMjk2em02LjQxLjg2MmMtLjE0NCAwLS4yNC0uMDI0LS4zMDQtLjA4LS4wNjQtLjA0OC0uMTItLjE2LS4xNjgtLjMxMUw3LjU4NiA1LjU1YTEuMzk4IDEuMzk4IDAgMCAxLS4wNzItLjMyYzAtLjEyOC4wNjQtLjIuMTkxLS4yaC43ODNjLjE1MSAwIC4yNTUuMDI1LjMxLjA4LjA2NS4wNDguMTEzLjE2LjE2LjMxMmwxLjM0MiA1LjI4NCAxLjI0NS01LjI4NGMuMDQtLjE2LjA4OC0uMjY0LjE1MS0uMzEyYS41NDkuNTQ5IDAgMCAxIC4zMi0uMDhoLjYzOGMuMTUyIDAgLjI1Ni4wMjUuMzIuMDguMDYzLjA0OC4xMi4xNi4xNTEuMzEybDEuMjYxIDUuMzQ4IDEuMzgxLTUuMzQ4Yy4wNDgtLjE2LjEwNC0uMjY0LjE2LS4zMTJhLjUyLjUyIDAgMCAxIC4zMTEtLjA4aC43NDNjLjEyNyAwIC4yLjA2NS4yLjIgMCAuMDQtLjAwOS4wOC0uMDE3LjEyOGExLjEzNyAxLjEzNyAwIDAgMS0uMDU2LjJsLTEuOTIzIDYuMTdjLS4wNDguMTYtLjEwNC4yNjMtLjE2OC4zMTFhLjUxLjUxIDAgMCAxLS4zMDMuMDhoLS42ODdjLS4xNTEgMC0uMjU1LS4wMjQtLjMyLS4wOC0uMDYzLS4wNTYtLjExOS0uMTYtLjE1LS4zMmwtMS4yMzgtNS4xNDgtMS4yMyA1LjE0Yy0uMDQuMTYtLjA4Ny4yNjQtLjE1LjMyLS4wNjUuMDU2LS4xNzcuMDgtLjMyLjA4em0xMC4yNTYuMjE1Yy0uNDE1IDAtLjgzLS4wNDgtMS4yMjktLjE0My0uMzk5LS4wOTYtLjcxLS4yLS45MTgtLjMyLS4xMjgtLjA3MS0uMjE1LS4xNTEtLjI0Ny0uMjIzYS41NjMuNTYzIDAgMCAxLS4wNDgtLjIyNHYtLjQwN2MwLS4xNjcuMDY0LS4yNDcuMTgzLS4yNDcuMDQ4IDAgLjA5Ni4wMDguMTQ0LjAyNC4wNDguMDE2LjEyLjA0OC4yLjA4LjI3MS4xMi41NjYuMjE1Ljg3OC4yNzkuMzE5LjA2NC42My4wOTYuOTUuMDk2LjUwMiAwIC44OTQtLjA4OCAxLjE2NS0uMjY0YS44Ni44NiAwIDAgMCAuNDE1LS43NTguNzc3Ljc3NyAwIDAgMC0uMjE1LS41NTljLS4xNDQtLjE1MS0uNDE2LS4yODctLjgwNy0uNDE1bC0xLjE1Ny0uMzZjLS41ODMtLjE4My0xLjAxNC0uNDU0LTEuMjc3LS44MTNhMS45MDIgMS45MDIgMCAwIDEtLjQtMS4xNThjMC0uMzM1LjA3My0uNjMuMjE2LS44ODYuMTQ0LS4yNTUuMzM1LS40NzkuNTc1LS42NTQuMjQtLjE4NC41MS0uMzIuODMtLjQxNS4zMi0uMDk2LjY1NS0uMTM2IDEuMDA2LS4xMzYuMTc1IDAgLjM1OS4wMDguNTM1LjAzMi4xODMuMDI0LjM1LjA1Ni41MTguMDg4LjE2LjA0LjMxMi4wOC40NTUuMTI3LjE0NC4wNDguMjU2LjA5Ni4zMzYuMTQ0YS42OS42OSAwIDAgMSAuMjQuMi40My40MyAwIDAgMSAuMDcxLjI2M3YuMzc1YzAgLjE2OC0uMDY0LjI1Ni0uMTg0LjI1NmEuODMuODMgMCAwIDEtLjMwMy0uMDk2IDMuNjUyIDMuNjUyIDAgMCAwLTEuNTMyLS4zMTFjLS40NTUgMC0uODE1LjA3MS0xLjA2Mi4yMjMtLjI0OC4xNTItLjM3NS4zODMtLjM3NS43MSAwIC4yMjQuMDguNDE2LjI0LjU2Ny4xNTkuMTUyLjQ1NC4zMDQuODc3LjQ0bDEuMTM0LjM1OGMuNTc0LjE4NC45OS40NCAxLjIzNy43NjcuMjQ3LjMyNy4zNjcuNzAyLjM2NyAxLjExNyAwIC4zNDMtLjA3Mi42NTUtLjIwNy45MjYtLjE0NC4yNzItLjMzNi41MTEtLjU4My43MDMtLjI0OC4yLS41NDMuMzQzLS44ODYuNDQ3LS4zNi4xMTEtLjczNC4xNjctMS4xNDIuMTY3ek0yMS42OTggMTYuMjA3Yy0yLjYyNiAxLjk0LTYuNDQyIDIuOTY5LTkuNzIyIDIuOTY5LTQuNTk4IDAtOC43NC0xLjctMTEuODctNC41MjYtLjI0Ny0uMjIzLS4wMjQtLjUyNy4yNzItLjM1MSAzLjM4NCAxLjk2MyA3LjU1OSAzLjE1MyAxMS44NzcgMy4xNTMgMi45MTQgMCA2LjExNC0uNjA3IDkuMDYtMS44NTIuNDM5LS4yLjgxNC4yODcuMzgzLjYwN3pNMjIuNzkyIDE0Ljk2MWMtLjMzNi0uNDMtMi4yMi0uMjA3LTMuMDc0LS4xMDMtLjI1NS4wMzItLjI5NS0uMTkyLS4wNjMtLjM2IDEuNS0xLjA1MyAzLjk2Ny0uNzUgNC4yNTQtLjM5OS4yODcuMzYtLjA4IDIuODI2LTEuNDg1IDQuMDA3LS4yMTUuMTg0LS40MjMuMDg4LS4zMjctLjE1MS4zMi0uNzkgMS4wMy0yLjU3LjY5NS0yLjk5NHoiLz48L3N2Zz4=&logoColor=white)](https://aws.amazon.com/)
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
