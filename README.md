# Azure Architecture Consultant

**Azure Architecture Consultant** is a Copilot Studio enterprise pre-sales agent that transforms unstructured customer requirements into Azure architecture recommendations, deterministic monthly pricing for supported components, and proposal-ready outputs.

The solution uses Power Automate and an Azure Function App backend hosted in Azure to retrieve live pricing from the Azure Retail Prices API, while grounding proposal structure in a standardized SharePoint template.

---

## Architecture Overview

Azure Architecture Consultant combines conversational reasoning, deterministic pricing, and enterprise grounding across Microsoft 365 and Azure services.

### Components

- **Copilot Studio Agent**  
  Analyzes customer requirements, recommends Azure architecture, and generates proposal-ready outputs.

- **Power Automate Flow**  
  Orchestrates pricing requests from the agent and invokes the backend pricing service.

- **Azure Function App**  
  Hosted backend service that queries the Azure Retail Prices API and returns normalized monthly pricing for supported components.

- **Azure Retail Prices API**  
  Provides live Microsoft retail pricing data used for cost estimation.

- **SharePoint Proposal Template**  
  Grounds proposal structure using a standardized enterprise template stored in SharePoint.

---

## Deployment

This repository includes a GitHub Actions workflow (`.github/workflows/deploy-function.yml`) that deploys the Azure Function App code for the pricing backend.

The workflow:
- triggers on pushes to the `main` branch
- installs Python dependencies for Azure Functions
- packages the contents of the `function` directory
- deploys updated code to the Azure Function App

This ensures that the pricing backend remains version-controlled and can be updated directly from the repository.

---

## Deterministic Pricing Backend

This solution retrieves VM pricing only at this time and pricing is retrieved through:
1. Power Automate orchestration  
2. Azure Function App backend  
3. Azure Retail Prices API  

This ensures cost estimates are based on **live Microsoft retail pricing data** and remain consistent and reliable for supported scenarios.

---

## Hosting

The Azure Function App backend used by the solution is hosted in Azure and deployed from this repository.

The Function App:
- receives normalized pricing parameters
- queries the Azure Retail Prices API
- returns monthly pricing results for supported Azure components

This backend is a core part of the solution and not an external dependency.

---

## Work IQ and MCP Alignment

This solution is designed to align with Microsoft's **Work IQ MCP model** for enterprise-grounded agents.

Work IQ provides the intelligence layer that grounds Copilot Studio agents in Microsoft 365 context and enterprise data. It requires a **Microsoft 365 Copilot license** and tenant-level admin enablement.

In this environment:
- A Microsoft 365 Copilot license was available ✅
- Direct Work IQ activation was blocked by tenant admin controls ❌

To maintain alignment, the solution uses:
- SharePoint knowledge grounding  
- Standardized enterprise proposal templates
- Tenant graph grounding with semantic search is enabled for the agent


This leverages the same Microsoft 365 content surface that Work IQ enhances once enabled, making the solution **Work IQ–ready by design**.

---

## Human-in-the-Loop Design

A key differentiator of this solution is its **human-in-the-loop approach**.

The agent automatically handles:
- Requirement analysis
- Architecture recommendation
- Proposal draft generation
- Supported VM pricing

For complex or uncertain scenarios, it explicitly flags items for:
- Architect validation  
- Advanced sizing  
- Networking design  
- Security and compliance  
- Disaster recovery planning  

This ensures outputs are:
- Transparent  
- Governed  
- Suitable for real enterprise workflows  

---

## Current Scope

### Supported
- Azure architecture recommendation from natural language input  
- Proposal-ready output aligned to SharePoint template  
- Live monthly pricing for Azure Virtual Machines  

### Not Automated
- Multi-SKU pricing
- Bulk inventory pricing

These scenarios are intentionally routed to **Architect Review** rather than being inferred.

---

## Summary

Azure Architecture Consultant bridges the gap between conversational AI and enterprise pre-sales workflows by combining:
- Copilot Studio reasoning  
- Deterministic Azure pricing  
- SharePoint-grounded proposal generation  
- MCP-aligned architecture  

The result is a **production-realistic pre-sales assistant** that accelerates proposal creation while maintaining trust, accuracy, and governance.

