> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aside.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set agent permissions

> Set agent permissions, session permission modes, sandbox settings, and file access.

# Set agent permissions

Agent permissions control what an agent can read, write, browse, fetch, and run.

## Agent permissions

Open `Settings > Agents` and scroll to the permission sections.

Permission areas include:

* `Sandbox` controls whether commands run with OS-level isolation.
* `File permissions` lists folders agents can view or edit.
* `Tool permissions` groups tool rules under `Allow`, `Ask`, and `Deny`.

## Rule values

| Value   | Behavior                                         |
| ------- | ------------------------------------------------ |
| `Allow` | Let the agent use the capability without asking. |
| `Ask`   | Ask before the agent proceeds.                   |
| `Deny`  | Block the action.                                |

Deny takes precedence over ask and allow.

## Session permission modes

New tasks also have a permission mode:

| Mode          | Use                                                                          |
| ------------- | ---------------------------------------------------------------------------- |
| `Read only`   | Let Aside inspect browser and file context without changing your files.      |
| `Guard`       | Let Aside work in approved folders and ask before it accesses other folders. |
| `Full access` | Let Aside read and write anywhere on the computer.                           |

`Guard` is the default for new tasks. `Full access` expands file access; it does not expose saved password values.

## Password boundaries

Aside can sign in through autofill with its password manager. Saved password values stay hidden from the AI agent.
Aside checks password access policy and the target URL before it builds an autofill payload. See [Use Password Manager](/help/password-manager).

## Agent-level and session-level rules

Agent-level permissions live under `Settings > Agents`. Session-level permissions live on each task.

When a task has its own permission settings, Aside applies those task settings on top of the agent defaults.

## Related

* [Manage privacy](/help/privacy)
* [Use Password Manager](/help/password-manager)
* [Run tasks](/help/tasks)
