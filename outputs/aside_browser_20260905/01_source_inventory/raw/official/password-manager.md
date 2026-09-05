> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aside.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Password Manager

> Understand Aside Password Manager and how agents use saved credentials.

# Use Aside Password Manager

Aside Password Manager stores logins for you and lets Aside sign in through autofill. The agent can use the login action, but it does not receive the raw password.

Use it when you want Aside to work past login screens in payroll tools, dashboards, email, CRMs, billing pages, and internal tools.

## What it does

* Saves website logins in Aside.
* Suggests matching credentials on sign-in pages.
* Fills passwords into websites without showing them to the agent.
* Supports passkey, FIDO2, and TOTP prompts where the site asks for them.
* Lets you control when agents may use saved credentials.

## How agent sign-in works

When a task reaches a login page, Aside checks the target URL and your password access settings. If a matching credential is allowed, Aside can autofill it into the page.

Some sites still require a human step. If the site asks for MFA, passkey approval, CAPTCHA, or identity verification, complete the visible step and let the task continue.

<Note>
  Aside can use saved credentials to sign in. Sensitive actions such as payments, posts, and messages should still wait for your confirmation when the task asks for approval.
</Note>

## Common uses

<AccordionGroup>
  <Accordion title="Get files behind a login" icon="file-down">
    Sign in to Rippling, get my paystubs for this month, and save the PDFs to Downloads. Ask if Rippling needs MFA or a verification code.
  </Accordion>

  <Accordion title="Work across an internal dashboard" icon="layout-dashboard">
    Sign in to the support dashboard, review the customer account, and draft a reply for the open thread. Stop before posting it.
  </Accordion>

  <Accordion title="Collect billing records" icon="receipt">
    Sign in to the vendor portal, download last quarter's invoices, and save them with the invoice date and vendor name.
  </Accordion>
</AccordionGroup>

## Unlock with Touch ID

On a Mac with Touch ID, Aside Password Manager prompts you to enroll your fingerprint as a way to unlock the vault. The prompt shows up the first time you unlock the vault on a supported device, and only if you have not enrolled yet.

From the prompt:

* Choose `Enable` to enroll Touch ID. Next time the vault is locked, unlock it with your fingerprint instead of your master password.
* Choose `Not now` to dismiss the prompt. Aside remembers your choice and won't ask again. You can still turn on Touch ID later from `Settings > Passwords`.

Touch ID changes how you unlock the vault, not what agents can do once it's open. The `While unlocked` [access policy](#control-agent-access) still applies: agents can use saved credentials only while the vault is unlocked, no matter how you unlocked it.

## Control agent access

Open `Settings > Passwords > Access policy for AI agents`.

Choose one of these policies:

* `Always allow`
* `While unlocked`
* `Never`

Imported items can override the global policy per item. Agents cannot use password manager access in incognito sessions.

## Related

* [Configure password autofill](/help/passwords)
* [Set agent permissions](/help/security)
* [Troubleshoot Aside](/help/troubleshooting)
