> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aside.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run tasks

> Use Aside for longer browser work, permissions, active page context, and follow-ups.

# Run tasks with Aside

Use Aside for work that needs more than one browser action, search, file step, credential autofill, or approval.

## Task controls

A new task has controls for mode, permissions, working folder, and model.

| Control          | Use                                                                          |
| ---------------- | ---------------------------------------------------------------------------- |
| `Default` mode   | Run the task in the normal browser profile.                                  |
| `Incognito` mode | Run the task without normal browser profile state.                           |
| `Read only`      | Let Aside inspect browser and file context without changing your files.      |
| `Guard`          | Let Aside work in approved folders and ask before it accesses other folders. |
| `Full access`    | Let Aside read and write anywhere on the computer.                           |
| Working folder   | Choose where Aside can work for this task.                                   |
| Model            | Choose the model and speed for the task.                                     |

See [Set agent permissions](/help/security) for permission rules and defaults.

## Longer tasks

During a task, Aside can browse sites, search the web, use files, search history, request approvals, and sign in with allowed autofill.

A task can keep working through multiple steps, pause for input, ask for approval, or resume after a wait.

The task detail page shows files the task creates or changes. Aside can preview supported images, PDFs, HTML, text files, and file metadata from the task.

Aside stores regular task transcripts in the task folder. Incognito tasks do not keep normal browser profile state. Generated files remain until you delete the task or its folder.

Aside can wait for a notification before continuing a task. When a task is waiting, open the task to review the current status and any instructions from Aside.

## Write a good task

Give Aside the result you want and the sites or files it should use.

<Accordion title="Rippling paystub download" icon="file-down">
  Sign in to Rippling, get my paystubs for this month, and save the PDFs to Downloads. Ask if Rippling needs MFA or a verification code.
</Accordion>

<Warning>
  `Handle my billing.` is too vague. Name the account, artifact, destination, and any action Aside should avoid.
</Warning>

Add constraints if the task touches money, customer data, credentials, or files.

## Use follow-ups

Open `Settings > Agents > Chat` to choose follow-up behavior.

* `Queue`: Aside saves your new message and applies it after the current run finishes.
* `Steer`: Aside sends your new message into the active run so the agent can adjust.

Use `Queue` when the task should finish its current path. Use `Steer` when the agent needs a correction now, such as using a different site or stopping an action.

## Active tab context

The side panel can attach the current page to a new task. See [Use the side panel](/help/side-panel).

## Related

* [Get started](/help/get-started)
* [Use the side panel](/help/side-panel)
* [Use routines](/help/automation)
* [Troubleshoot Aside](/help/troubleshooting)
