# Tutorial 02.2 — Self-Describing MCP Requests

**Created by School of AI**

**Module:** Protocol Messages, Requests & Responses

## Objective
Understand and implement **self-describing mcp requests** as part of a production MCP system.

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

For Streamable HTTP, method and name headers make requests routable and enforceable by ordinary gateways without JSON body inspection.

## Engineering checkpoint
Create one protocol artifact, one validation test, one security check and one production note.

---

**Created by School of AI**
