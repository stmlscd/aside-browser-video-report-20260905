> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aside.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Aside as your browser

> Use Ask AI, split tabs, selection shortcuts, and keyboard shortcuts.

# Browser basics

Use this page when you want to drive Aside as your daily browser: ask from the new tab page, compare pages, save shortcuts, and use common keyboard commands.

## Ask AI

Use `Ask AI` when you want to start a task from the browser UI. The new tab omnibox has `Search` and `Ask AI` modes, and task composers use the placeholder `Ask AI a task, @ for context`.

Ask AI works best when you name the site, the outcome, and any limit the agent should follow.

### Examples

<AccordionGroup>
  <Accordion title="Rippling paystubs" icon="file-down">
    Sign in to Rippling, get my paystubs for this month, and save the PDFs to Downloads. Ask if Rippling needs MFA or a verification code.
  </Accordion>

  <Accordion title="Clay meeting outreach" icon="calendar-plus">
    Find Sales VPs in Clay who are coming to NY Tech Week, check my calendar for open times next week, and draft meeting replies. Stop before sending.
  </Accordion>

  <Accordion title="Receipt expense report" icon="file-spreadsheet">
    Turn the receipt PDFs in Downloads into an expense report spreadsheet with date, merchant, total, and payment method.
  </Accordion>
</AccordionGroup>

Use `@` in the composer to attach available context.

Use `Cmd/Ctrl+E` to start `Ask Aside`.

## Tabs and split tabs

Use split tabs when you need to keep two pages visible while Aside works: source and destination, comparison pages, docs and app, or dashboard and ticket.

Good split-tab use cases:

* Compare two product pages without switching tabs.
* Keep a source document visible while writing into a form.
* Watch a task run while you inspect the target site.
* Put a task transcript next to the page it controls.

Split-tab shortcuts:

| Action              | Shortcut           |
| ------------------- | ------------------ |
| Split tab           | `Cmd/Ctrl+Shift+\` |
| Split tab alternate | `Cmd/Ctrl+Shift+-` |

## Selection and lasso shortcuts

Use selection shortcuts for small page-level questions.

Text selection defaults:

* `Summarize`
* `Translate`

Lasso selection defaults:

* `Copy code`
* `Search image`

Selection shortcuts are on by default. Open `Settings > Lasso` to turn them off, reorder shortcuts, edit shortcuts, delete shortcuts, or add a shortcut.

Shortcut actions can:

* Run a prompt.
* Copy selected content.
* Open a URL.

Templates can use `{text}`. Lasso shortcuts can also use `{code}` and `{image}` where supported.

### Examples

<AccordionGroup>
  <Accordion title="Summarize a policy clause" icon="file-text">
    Summarize this clause in plain English and list the obligations I need to track:

    {text}
  </Accordion>

  <Accordion title="Read a receipt table" icon="scan-search">
    Read this receipt table and return rows with date, merchant, total, and payment method:

    {image}
  </Accordion>
</AccordionGroup>

## Keyboard shortcuts

Use the model menu when a task needs more reasoning.

| Action              | Shortcut           |
| ------------------- | ------------------ |
| Toggle Sidebar      | `Cmd/Ctrl+S`       |
| Ask Aside           | `Cmd/Ctrl+E`       |
| New Task            | `Cmd/Ctrl+Shift+E` |
| Copy URL            | `Cmd/Ctrl+Shift+C` |
| Split tab           | `Cmd/Ctrl+Shift+\` |
| Split tab alternate | `Cmd/Ctrl+Shift+-` |

## Related

* [Use the side panel](/help/side-panel)
* [Run tasks](/help/tasks)
* [Use Password Manager](/help/password-manager)
