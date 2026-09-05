> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aside.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure password autofill

> Configure autofill, import passwords, and control AI access to credentials.

# Configure password autofill

Use this page after you understand how Aside Password Manager works. See [Use Password Manager](/help/password-manager) for the overview.

## Turn on autofill

1. Open `Settings > Passwords`.
2. Choose the default password manager.
   Turn on `Use default password manager` if you want Aside to manage passwords.
3. Enable `Autofill`.
4. Choose URL matching.
5. Add domains to `Excluded domains` if Aside should not fill on those sites.
6. Choose whether Aside can show suggestions on insecure protocols.
7. Choose whether autofill works in incognito windows.

Aside fills credentials into websites. Saved passwords stay local and hidden from AI.

Autofill is on by default, and Aside only fills matching logins according to your password access settings.

Aside also treats common account domains as equivalent by default, such as `google.com`, `youtube.com`, and `gmail.com`.

## Import passwords

Open `Settings > Passwords > Import`.

<Accordion title="Supported import sources" icon="upload">
  * 1Password
  * Apple Passwords
  * Bitwarden
  * Chrome
  * Dashlane
  * Edge
  * Firefox
  * LastPass CSV
  * Generic CSV fallback
</Accordion>

1. Export passwords from the source password manager.
2. Open Aside password settings.
3. Choose `Import`.
4. Choose the source.
5. Choose the export.
   Follow the source-specific flow if the import UI asks for it.
6. Review the result.

After setup, Aside can show login suggestions, save prompts, generated password suggestions, passkey/FIDO2 dialogs, and TOTP autofill prompts.

Generic CSV imports require these columns:

```text theme={null}
name,url,username,password
```

The import UI handles source-specific formats. After import, keep the exported file only if you still need a backup.

## Control AI access to passwords

Open `Settings > Passwords > Access policy for AI agents`.

Use this setting to control how agents may use saved credentials.

Options are:

* `Always allow`
* `While unlocked`
* `Never`

The default is `Always allow`. Imported items can override the global policy per item. Agents cannot use password manager access in incognito sessions. For login items, Aside checks the target URL before building an autofill payload.

Aside checks allowed vault items for matching logins without exposing saved passwords to the agent.

## Vaults and sync

Password settings include vault management, cloud sync, import, export, and clear vault data.

Use export before clearing a vault if you need a backup.

Aside encrypts vault data before sync, and saved password values stay hidden from AI.

`Clear vault data` deletes local items, vault keys, and vaults, creates a fresh Personal vault, and syncs the reset state.

## Related

* [Use Password Manager](/help/password-manager)
* [Set agent permissions](/help/security)
* [Troubleshoot Aside](/help/troubleshooting)
