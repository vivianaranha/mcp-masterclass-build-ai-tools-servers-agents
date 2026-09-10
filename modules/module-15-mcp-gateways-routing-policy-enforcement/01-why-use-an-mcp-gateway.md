# Tutorial 15.1 — Why Use an MCP Gateway

**Created by School of AI**

**Module:** MCP Gateways, Routing & Policy Enforcement

## Objective
Understand and implement **why use an mcp gateway** as part of a production MCP system.

## 1. Define the protocol contract
Record the method, optional name, arguments, expected result, error behavior and required capabilities.

## 2. Separate protocol from application state
The protocol request should be self-describing. If the business workflow needs state, use explicit identifiers or task handles that can be passed between calls.

## 3. Treat tools, resources and prompts differently
- **Tools** perform actions or computations.
- **Resources** expose readable context/data.
- **Prompts** expose reusable interaction templates.

## 4. Add security outside the model
Use deterministic identity, authorization, scope, rate-limit and validation checks. An LLM selecting a tool must never be treated as authorization.

## 5. Make the call observable
Capture request ID, identity, method, name, outcome, latency, scope decision and relevant error.

MCP gateways can route and meter using method/tool headers, making tool-level policy much easier to centralize.

## Engineering checkpoint
Create one protocol artifact, one validation test, one security check and one production note.

---

**Created by School of AI**
