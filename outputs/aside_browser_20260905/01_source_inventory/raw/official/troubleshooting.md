> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aside.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot Aside

> Fix waiting tasks, stuck tasks, password autofill issues, and import problems.

# Troubleshoot Aside

Use this page when Aside needs input, a task stalls, password autofill does not appear, browser import fails, or you need to report a bug.

## Task is waiting for you

1. Open the task.
2. Find the input or approval request.
3. Review the requested action.
4. Approve, reject, or answer.
5. Resume the task if the UI shows a resume action.

If Aside reaches a sign-in screen, it can use allowed saved credentials through autofill. If the site asks for MFA, passkey approval, CAPTCHA, or identity verification, complete the visible step or answer Aside's request, then resume the task.

Aside may show visible task states such as waiting for approval, waiting for an answer, errored, or finished. Approve or deny approval popovers directly from the browser surface. Questions and draft reviews open the task detail page.

## Task is going the wrong way

Use a follow-up.

* Use `Steer` if the agent needs correction during the current run.
* Use `Queue` if the instruction can wait until the current run finishes.

Example: `Stop using the billing page. Use the invoices page instead, and do not send any emails.`

## Task waits for a notification

Aside can pause a task while it waits for a notification. Open the task to see whether Aside needs a reply, approval, or a connected app event.

## Password autofill does not appear

Check these settings:

1. Open `Settings > Passwords`.
2. Confirm `Use default password manager` is enabled if you want Aside to manage passwords.
3. Confirm `Enable Autofill` is on.
4. Check `Disable in incognito` if you are in an incognito window.
5. Check `Excluded domains`.
6. Check whether insecure-site autofill is allowed for the current site.

If the site uses a passkey, MFA, or a multi-step login, Aside can fill the saved credential first. Complete the visible verification step and wait for the next prompt.

## 1Password extension does not work

1. Open the 1Password app.
2. Go to `Settings > Browser > Connect to additional browsers`, then click `Add browser`.
3. Select `Aside`.
4. Copy `~/Library/Application Support/Google/Chrome/NativeMessagingHosts/com.1password.1password.json` to `~/Library/Application Support/Aside/NativeMessagingHosts/com.1password.1password.json`.

<Note>
  1Password should copy its native messaging host file into the browser profile when you add a custom browser. It does not recognize Aside as a Chromium-based browser, so you need to copy the file yourself.
</Note>

## Apple Passwords extension does not work

Enter this prompt in Aside:

```text theme={null}
Use the Apple Passwords skill and check whether Apple Passwords is connected properly.
```

After Aside finishes the check, open the Apple Passwords extension again. You should now be able to use it.

## Browser import fails

Try these checks:

1. Confirm the source browser profile still exists.
2. Close the source browser if the import needs exclusive access.
3. Use file import for sources that require it.
4. Retry import.

Aside can show these import errors:

* `Browser import is unavailable in this version of Aside.`
* `Browser import failed.`
* `Please upload a ZIP file` for Safari ZIP import.
* `Failed to read the ZIP file` for unreadable Safari ZIP import.

## Streaming sites show "unsupported browser" or fail to play

Streaming sites like Amazon Prime Video, YouTube, and Netflix may show `You are running an unsupported version of this browser` (for example Prime Video error code `7132`) or fail to play protected content when the Widevine DRM module is outdated or has not finished downloading.

1. Open `aside://components`.
2. Find `Widevine Content Decryption Module`.
3. Click `Check for update`.
4. Wait for the status to change to `Up-to-date`.
5. Reload the streaming tab.

## Report a bug

You can contact support at [support@aside.com](mailto:support@aside.com).

Include:

* Task URL or task ID
* Approximate time
* Website or app involved
* Expected result
* Actual result
* Screenshot or artifact path, if available
* Any visible error message

You can also send feedback in the app:

* Open `Settings`, then choose `Send feedback`.
* Open a task detail page, open the more actions menu, then choose `Send feedback`.

General feedback can include screenshots. Task feedback can include the task transcript and diagnostics.

## Related

* [Run tasks](/help/tasks)
* [Use routines](/help/automation)
* [Use Password Manager](/help/password-manager)
