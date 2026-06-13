**Azure Architecture Consultant** is a **Copilot Studio enterprise pre-sales agent** that analyzes Azure requirements, recommends architecture, retrieves live monthly VM pricing through an Azure Function and the Azure Retail Prices API, and generates proposal-ready outputs aligned to SharePoint templates. The solution is Work IQ–ready by design and uses an MCP-based tool pattern, while unsupported or architecture-dependent scope is explicitly routed to architect validation.

## Architecture Overview

Azure Architecture Consultant combines conversational reasoning, deterministic pricing, and grounded proposal generation across Microsoft 365 and Azure services.

### Components
- **Copilot Studio Agent**  
  Analyzes customer requirements, recommends Azure architecture, and generates proposal-ready outputs.

- **Power Automate Flow**  
  Orchestrates pricing requests from the agent and calls the Azure pricing backend.

- **Azure Function App**  
  Hosted backend service that queries the Azure Retail Prices API and returns normalized monthly pricing for supported components.

- **Azure Retail Prices API**  
  Source of live Microsoft retail pricing data.

- **SharePoint Proposal Template**  
  Grounds proposal structure using a standardized enterprise template stored in SharePoint.

### Hosting
The Azure Function App backend used by the solution is hosted in Azure and deployed from this repository.


## Work IQ and MCP Alignment

This solution is designed to align with Microsoft's **Work IQ MCP** model for enterprise-grounded agents. Microsoft documents Work IQ MCP as the intelligence layer that grounds agents in Microsoft 365 context and business data, and enables secure tools through MCP servers in Copilot Studio. A valid **Microsoft 365 Copilot license** is required to use Work IQ MCP, and activation is governed by tenant-level admin consent and MCP server controls. In this environment, the required Microsoft 365 Copilot licensing was available, but direct Work IQ activation was not possible due to tenant admin restrictions. The solution therefore uses **SharePoint grounding** and standardized SharePoint proposal templates on the exact enterprise content surface that Work IQ is designed to enhance once enabled.

