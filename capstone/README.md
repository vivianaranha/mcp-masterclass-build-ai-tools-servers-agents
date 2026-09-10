# Enterprise MCP Platform — Capstone

**Created by School of AI**

Build **Northstar MCP Fabric**, an enterprise tool and knowledge platform used by AI agents.

## Required capabilities
1. stateless MCP server architecture
2. tools/list and tools/call concepts
3. resources/list/read
4. prompts/list/get
5. Mcp-Method/Mcp-Name routing
6. client discovery cache
7. explicit state handles where needed
8. MRTR approval flow
9. Tasks extension for long-running work
10. one custom extension capability
11. OAuth-style issuer/audience/scope validation
12. enterprise-managed authorization design
13. gateway routing/policy/rate limits
14. agent tool permissions
15. human approval for consequential writes
16. MCP-backed knowledge access
17. contract/security regression tests
18. request/audit tracing
19. horizontal deployment plan
20. migration/deprecation/runbook plan

## Demo scenarios
- list/discover tools
- call read tool with valid scope
- reject missing scope
- resource hidden from unauthorized role
- MRTR requests approval
- task moves working → completed
- gateway routes by method/name
- wrong issuer/audience denied
- agent write action denied without permission/approval
- cached catalog reused

## Review
Defend why each capability is a tool/resource/prompt, how the platform scales statelessly, where identity is enforced, when Tasks/MRTR apply, and how third-party MCP servers are governed.

---

**Created by School of AI**
