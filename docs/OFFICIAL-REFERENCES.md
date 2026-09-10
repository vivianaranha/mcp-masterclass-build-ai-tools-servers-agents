# Official References

**Created by School of AI**

## MCP 2026-07-28 release
https://blog.modelcontextprotocol.io/posts/2026-07-28/

Key changes include a stateless protocol core, self-describing requests, `Mcp-Method` / `Mcp-Name` routing headers, cache hints for list/read results, Multi Round-Trip Requests, formal extensions, authorization hardening and a formal deprecation policy.

## Tasks extension
https://tasks.extensions.modelcontextprotocol.io/specification/draft/tasks

The Tasks extension supports server-directed asynchronous task creation and lifecycle methods such as `tasks/get`, `tasks/update` and `tasks/cancel`.

## TypeScript SDK migration guidance
https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28

The current SDK guidance documents the authorization hardening and per-revision wire behavior required for 2026-07-28 support.

## Security guidance
Use the current MCP documentation for authorization and security implementation details:
- https://modelcontextprotocol.io/specification/2026-07-28
- https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization
- https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices

## Course position
The core code in this repository is a dependency-light educational simulator. For production implementation, use the current official MCP SDK for your language and verify the latest specification/extension documents.

---

**Created by School of AI**
