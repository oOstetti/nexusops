# NexusOps

AI-powered IT Operations Platform

NexusOps is an evolving IT operations platform designed to centralize infrastructure management, incident investigation, intelligent automation, and AI-powered decision support.

## Project Status

**Version:** 0.1.0

**Current stage:** Backend Foundation

## Implemented Features

- REST API with FastAPI
- Device inventory management
- Complete CRUD operations
- Online and offline device filtering
- Infrastructure summary and availability metrics
- Data validation with Pydantic
- HTTP exception handling
- Interactive API documentation with Swagger UI
- Application health check endpoint

## Current Technology Stack

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Git

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Application information |
| GET | /health | Health check |
| GET | /devices | List devices |
| GET | /devices/online | List online devices |
| GET | /devices/offline | List offline devices |
| GET | /devices/summary | Infrastructure summary |
| GET | /devices/{device_id} | Get device details |
| POST | /devices | Create a device |
| PUT | /devices/{device_id} | Replace device data |
| PATCH | /devices/{device_id} | Partially update a device |
| DELETE | /devices/{device_id} | Delete a device |

## Getting Started

Create a Python virtual environment, activate it, and install the dependencies using:

`pip install -r requirements.txt`

Start the application:

`uvicorn backend.main:app --reload`

API documentation:

http://localhost:8000/docs

## Development Roadmap

- [x] FastAPI foundation
- [x] Device management CRUD
- [x] Pydantic validation
- [ ] PostgreSQL and SQLAlchemy
- [ ] Modular backend architecture
- [ ] Authentication and authorization
- [ ] Automated testing
- [ ] Docker and Docker Compose
- [ ] CI/CD with GitHub Actions
- [ ] Web dashboard
- [ ] LLM integration
- [ ] Function Calling
- [ ] Model Context Protocol (MCP)
- [ ] AI agent orchestration
- [ ] RAG and knowledge base
- [ ] Zabbix integration
- [ ] Webhooks and workflow automation
- [ ] AI guardrails and evaluation
- [ ] AWS deployment
- [ ] Terraform and infrastructure as code
- [ ] Monitoring and observability

## Current Limitations

Device data is currently stored in memory and is reset when the application restarts. Persistent storage will be implemented in the next development stage.

## Project Purpose

This project explores the intersection of Backend Engineering, DevOps, Cloud Computing, Applied AI, and Forward Deployed Engineering.

## Author

Felipe Ostetti Ferri

Portfolio: https://felipeostettiferri.com