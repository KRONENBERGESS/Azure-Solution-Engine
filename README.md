**Azure Architecture Consultant** is a **Copilot Studio enterprise pre-sales agent** that analyzes Azure requirements, recommends architecture, retrieves live monthly VM pricing through an Azure Function and the Azure Retail Prices API, and generates proposal-ready outputs aligned to SharePoint templates. The solution is Work IQ–ready by design and uses an MCP-based tool pattern, while unsupported or architecture-dependent scope is explicitly routed to architect validation.


## Work IQ and MCP Alignment

This solution is designed to align with Microsoft's **Work IQ MCP** model for enterprise-grounded agents. Microsoft documents Work IQ MCP as the intelligence layer that grounds agents in Microsoft 365 context and business data, and enables secure tools through MCP servers in Copilot Studio. A valid **Microsoft 365 Copilot license** is required to use Work IQ MCP, and activation is governed by tenant-level admin consent and MCP server controls. In this environment, the required Microsoft 365 Copilot licensing was available, but direct Work IQ activation was not possible due to tenant admin restrictions. The solution therefore uses **SharePoint grounding** and standardized SharePoint proposal templates on the exact enterprise content surface that Work IQ is designed to enhance once enabled.

