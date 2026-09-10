# Final Exam Answer Key

**Created by School of AI**

1. A standard protocol for exposing tools, resources and prompts to AI clients/agents.

2. The protocol core became stateless and self-describing rather than depending on the earlier session/handshake model.

3. An HTTP header identifying the MCP method for routing/policy.

4. An HTTP header identifying the named tool/prompt/resource operation when applicable.

5. They can land on any compatible server instance behind ordinary load balancing.

6. Use explicit application handles/task IDs passed in request arguments.

7. A callable action/computation exposed by an MCP server.

8. Readable data/context exposed through a resource URI.

9. A reusable prompt/template capability exposed by the server.

10. The model/client can provide missing or invalid values and should not bypass deterministic validation.

11. Write tools create side effects and usually require stronger authorization/approval.

12. A multi-round-trip request mechanism for obtaining required client/user input during an active request.

13. A response state indicating additional input is needed before retrying/completing the original call.

14. A durable asynchronous task handle from the Tasks extension for long-running work.

15. The server, when the client has advertised support for the extension.

16. tasks/get, tasks/update and tasks/cancel.

17. To avoid collisions and make optional capabilities explicit.

18. To prevent authorization-server mix-up and credential confusion.

19. A token should only be accepted by the protected resource it was issued for.

20. Requesting additional authorization when a call requires scopes the client does not currently hold.

21. Credentials from one issuer/resource context should not be reused improperly with another.

22. An enterprise pattern/extension for centralizing MCP access policy through organizational identity infrastructure.

23. To centralize routing, authorization, rate limits, metering and observability across multiple servers.

24. They can enforce method/tool policy without parsing the full JSON body.

25. The server can provide cache hints so clients avoid unnecessary rediscovery.

26. An LLM choosing a tool does not prove the user/client is permitted to execute it.

27. Downstream actions need accountability and least-privilege decisions tied to the real actor.

28. They are supply-chain dependencies with access to data, tools or credentials.

29. Identity, method/name, server, authorization outcome, latency/result/error and relevant task/correlation IDs.

30. Protocol and SDK changes can break legacy transports/capabilities and create security/operational debt.

31. A standard protocol for exposing tools, resources and prompts to AI clients/agents.

32. The protocol core became stateless and self-describing rather than depending on the earlier session/handshake model.

33. An HTTP header identifying the MCP method for routing/policy.

34. An HTTP header identifying the named tool/prompt/resource operation when applicable.

35. They can land on any compatible server instance behind ordinary load balancing.

36. Use explicit application handles/task IDs passed in request arguments.

37. A callable action/computation exposed by an MCP server.

38. Readable data/context exposed through a resource URI.

39. A reusable prompt/template capability exposed by the server.

40. The model/client can provide missing or invalid values and should not bypass deterministic validation.

41. Write tools create side effects and usually require stronger authorization/approval.

42. A multi-round-trip request mechanism for obtaining required client/user input during an active request.

43. A response state indicating additional input is needed before retrying/completing the original call.

44. A durable asynchronous task handle from the Tasks extension for long-running work.

45. The server, when the client has advertised support for the extension.

46. tasks/get, tasks/update and tasks/cancel.

47. To avoid collisions and make optional capabilities explicit.

48. To prevent authorization-server mix-up and credential confusion.

49. A token should only be accepted by the protected resource it was issued for.

50. Requesting additional authorization when a call requires scopes the client does not currently hold.

51. Credentials from one issuer/resource context should not be reused improperly with another.

52. An enterprise pattern/extension for centralizing MCP access policy through organizational identity infrastructure.

53. To centralize routing, authorization, rate limits, metering and observability across multiple servers.

54. They can enforce method/tool policy without parsing the full JSON body.

55. The server can provide cache hints so clients avoid unnecessary rediscovery.

56. An LLM choosing a tool does not prove the user/client is permitted to execute it.

57. Downstream actions need accountability and least-privilege decisions tied to the real actor.

58. They are supply-chain dependencies with access to data, tools or credentials.

59. Identity, method/name, server, authorization outcome, latency/result/error and relevant task/correlation IDs.

60. Protocol and SDK changes can break legacy transports/capabilities and create security/operational debt.