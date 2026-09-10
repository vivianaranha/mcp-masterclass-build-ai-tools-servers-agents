# Complete Course Syllabus

**Created by School of AI**

## Module 01 — MCP Foundations & 2026 Architecture

- Tutorial 01.1: What MCP Is and Is Not
- Tutorial 01.2: MCP Clients, Servers and Capabilities
- Tutorial 01.3: The 2026-07-28 Stateless Core
- Tutorial 01.4: From Session-Oriented MCP to Stateless Requests
- **Lab:** Map an AI application into MCP clients, servers, tools, resources, prompts and authorization boundaries.

## Module 02 — Protocol Messages, Requests & Responses

- Tutorial 02.1: JSON-RPC Message Anatomy
- Tutorial 02.2: Self-Describing MCP Requests
- Tutorial 02.3: Mcp-Method and Mcp-Name Headers
- Tutorial 02.4: Errors, Result Types and Correlation
- **Lab:** Inspect and construct stateless MCP request/response messages locally.

## Module 03 — Tools: Designing AI Actions

- Tutorial 03.1: Tool Contracts and JSON Schema
- Tutorial 03.2: Read vs Write Tools
- Tutorial 03.3: Tool Errors and Deterministic Validation
- Tutorial 03.4: Tool Catalog Design
- **Lab:** Build a local MCP-style tool registry with schema validation.

## Module 04 — Resources: Exposing AI-Readable Data

- Tutorial 04.1: Resource Concepts and URIs
- Tutorial 04.2: Resource Listing and Reading
- Tutorial 04.3: Resource Metadata and MIME Types
- Tutorial 04.4: Resource Authorization and Caching
- **Lab:** Build a local resource catalog with role-aware reads.

## Module 05 — Prompts: Reusable Interaction Templates

- Tutorial 05.1: Prompt Concepts
- Tutorial 05.2: Prompt Arguments
- Tutorial 05.3: Prompt Discovery and Versioning
- Tutorial 05.4: Prompts vs Application-Level Templates
- **Lab:** Build a reusable prompt catalog and deterministic prompt rendering.

## Module 06 — Streamable HTTP & Stateless Server Design

- Tutorial 06.1: Streamable HTTP Transport
- Tutorial 06.2: Stateless Scaling Behind Load Balancers
- Tutorial 06.3: Explicit Application State Handles
- Tutorial 06.4: Gateway Routing and Caching
- **Lab:** Design a horizontally scalable MCP server topology without protocol sessions.

## Module 07 — MCP Clients & Capability Discovery

- Tutorial 07.1: Client Responsibilities
- Tutorial 07.2: Per-Request Capabilities
- Tutorial 07.3: Discovery vs Direct Calls
- Tutorial 07.4: Caching Tool, Resource and Prompt Lists
- **Lab:** Build a local MCP client simulator with discovery caching.

## Module 08 — Multi Round-Trip Requests (MRTR)

- Tutorial 08.1: Why MRTR Exists
- Tutorial 08.2: Input Required Flows
- Tutorial 08.3: Elicitation and User Confirmation
- Tutorial 08.4: Retrying the Original Request
- **Lab:** Build a local multi-round-trip approval simulation for a write action.

## Module 09 — MCP Tasks Extension

- Tutorial 09.1: Why Tasks Are an Extension
- Tutorial 09.2: Task Handles and Server-Directed Creation
- Tutorial 09.3: tasks/get, tasks/update and tasks/cancel
- Tutorial 09.4: Long-Running Workflows
- **Lab:** Build a durable local task state machine and polling client.

## Module 10 — MCP Extensions Framework

- Tutorial 10.1: Extension Negotiation
- Tutorial 10.2: Namespacing and Capability Signaling
- Tutorial 10.3: MCP Apps and Other Extensions
- Tutorial 10.4: Designing Safe Custom Extensions
- **Lab:** Create a simple namespaced extension capability and compatibility test.

## Module 11 — Authorization Foundations

- Tutorial 11.1: Protected Resources and OAuth Concepts
- Tutorial 11.2: Authorization Server Discovery
- Tutorial 11.3: Scopes and Resource Indicators
- Tutorial 11.4: Token Audience and Credential Isolation
- **Lab:** Design a secure authorization flow for an MCP server.

## Module 12 — MCP Authorization Hardening — 2026

- Tutorial 12.1: Issuer Validation
- Tutorial 12.2: Credential Isolation by Issuer
- Tutorial 12.3: Insufficient Scope and Step-Up
- Tutorial 12.4: Client Metadata Documents vs DCR
- **Lab:** Build local validators for issuer, audience and scope decisions.

## Module 13 — Enterprise-Managed Authorization

- Tutorial 13.1: Centralized Enterprise Identity
- Tutorial 13.2: Enterprise IdP Policy
- Tutorial 13.3: Server Trust and Organization Control
- Tutorial 13.4: User Consent and Managed Access
- **Lab:** Design an enterprise-managed authorization architecture for internal MCP servers.

## Module 14 — MCP Security Best Practices

- Tutorial 14.1: Token Handling and Storage
- Tutorial 14.2: Third-Party MCP Server Risk
- Tutorial 14.3: SSRF, Confused Deputy and Redirect Risks
- Tutorial 14.4: Rate Limits, Audit and Revocation
- **Lab:** Perform a defensive security review of a synthetic MCP deployment.

## Module 15 — MCP Gateways, Routing & Policy Enforcement

- Tutorial 15.1: Why Use an MCP Gateway
- Tutorial 15.2: Routing on Headers
- Tutorial 15.3: Centralized Policy and Rate Limiting
- Tutorial 15.4: Observability and Tool-Level Metering
- **Lab:** Build a local MCP gateway simulator that routes and authorizes by method/tool name.

## Module 16 — MCP + AI Agents

- Tutorial 16.1: Agents as MCP Clients
- Tutorial 16.2: Tool Selection and Bounded Autonomy
- Tutorial 16.3: Identity Propagation
- Tutorial 16.4: Human Approval and Consequential Actions
- **Lab:** Connect a bounded local agent to MCP-style tools with approval-gated writes.

## Module 17 — MCP + RAG & Enterprise Knowledge

- Tutorial 17.1: Resources for Knowledge Access
- Tutorial 17.2: Tools vs Resources for Retrieval
- Tutorial 17.3: Permission-Aware RAG Through MCP
- Tutorial 17.4: Citations, Lineage and Source Trust
- **Lab:** Build an MCP-backed enterprise knowledge workflow with permission filters.

## Module 18 — Testing, Evaluation & Observability

- Tutorial 18.1: Contract Testing
- Tutorial 18.2: Tool and Authorization Regression Tests
- Tutorial 18.3: Tracing and Correlation
- Tutorial 18.4: Latency, Usage and Failure Metrics
- **Lab:** Build a local MCP conformance and regression harness.

## Module 19 — Deploying & Operating MCP Servers

- Tutorial 19.1: Environment and Configuration
- Tutorial 19.2: Horizontal Scaling
- Tutorial 19.3: Caching and Rate Limits
- Tutorial 19.4: Runbooks, Rollback and Deprecation Planning
- **Lab:** Create a production-readiness pack for a stateless MCP server.

## Module 20 — MCP Masterclass Capstone

- Tutorial 20.1: Capstone Server and Tool Fabric
- Tutorial 20.2: Capstone Authorization and Gateway
- Tutorial 20.3: Capstone Tasks, Agents and Knowledge
- Tutorial 20.4: Capstone Security Review and Demo
- **Lab:** Build a complete enterprise MCP tool fabric used by agents and knowledge workflows.