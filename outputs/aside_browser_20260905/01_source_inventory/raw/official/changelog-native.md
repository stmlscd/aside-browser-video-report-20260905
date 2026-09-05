> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aside.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Aside Browser

> Changelog for Aside Browser

## v1.0.825.1

### Added Mini Popup

* Open Ask Aside from any app using a configurable global shortcut.

### Improved little tab UX

* Tabs can now be dragged between regular tabs, Pinned Tabs, and Bookmarks.
* Added smoother drag previews and animations when moving items between sections.

### Improved Agent Tabs

* Tabs grouped under Agent Tabs are now muted by default.

### Improved Ask Aside and Agent Manager

* Ask Aside now temporarily hides on Agent Manager and New Tab pages, then returns to its previous state when leaving those pages.

### Improved profile switching

* Fixed tabs and Chat state being replaced or lost when switching profiles, particularly when using multiple windows.
* Fixed profile switching occasionally showing or focusing the wrong window.

### Fixes and Improvements

* Updated Chromium to `151.0.7922.171`.
* Fixed restored New Tab pages opening the blank page instead of Agent Manager.
* Fixed the crash recovery prompt reappearing after it had already been dismissed or acknowledged.
* Fixed horizontal tabs becoming invisible after rapid scrolling.
* Fixed the browser opening before Password Manager, Agent Manager, or required background components were ready.
* Fixed extension actions launched from Tab Search opening in the wrong browser window or leaving Tab Search open.
* Removed the duplicated browser import entry from Settings.
* Fixed several crashes involving menus, Task Manager, dialogs, Sync, search suggestions, and extension image handling.
* Fixed macOS crashes involving Dock reopening, task popovers, and AppleScript bookmark insertion.
* Updated the Aside app icon for the macOS Clear appearance

## v1.0.813.1

### Fixes and Improvements

* Added a collapsible Bookmarks section to the vertical sidebar.
  * Go to Settings > Appearance > Customize sidebar > Check bookmarks to enable
* Fixed an issue where pages would sometimes fail to load and remain stuck on a blank white screen indefinitely.
* Fixed numbered tab shortcuts (Ctrl/Command + 1–9) not working while the vertical sidebar was collapsed.
* Fixed the collapsed sidebar preview unexpectedly closing while the pointer was still at the edge of the window.
* Fixed nested extension submenus closing their parent menus when navigating to deeper levels.
* Fixed Split View tabs becoming separated or misplaced when moved to the end of the tab list.
* Improved the reliability of grouped and Split View tabs when moving them between profiles.
* Fixed the address bar's permission indicator disappearing after camera or microphone activity ended while another permission was still active.
* Fixed a crash that could occur when closing the browser while a bookmark item was focused.
* Fixed crashes that could occur while navigating menus and dialogs with the keyboard.
* Improved stability when closing popovers and dialogs.

## v1.0.811.1

### Redesigned the sidebar

* Chats now have their own section above regular tabs and are expanded by default.
* Pinned Tabs and profile controls remain fixed while the tab list scrolls.

### Improved New Chat

* New Chat now appears as a dedicated row with its keyboard shortcut shown on hover.
* Opening it again focuses the existing New Chat tab instead of creating duplicates, and a newly started chat transitions into its own chat row.

### Added permanent chat deletion

* Chats can now be permanently deleted from their context menu.

### Added a Tab Switcher order setting

* Choose whether Ctrl + Tab lists tabs by most recently used order or by their current order in the sidebar.

### Improved profile switching

* Switching profiles with many open tabs is now faster and smoother.
* Swipe previews are also more reliable in both directions, including when using a collapsed floating sidebar.

### Fixes and Improvements

* Updated Chromium to `151.0.7922.109`
* Fixed Ask Aside changing its open or closed state when switching tabs. It now preserves the state selected by the user.
* Default chromium appearance settings are now synchronized across loaded profiles.
* Fixed the Aside Password Manager losing its pinned position or toolbar order after a component update.
* Fixed Picture-in-Picture sessions not returning to their original tab correctly after switching profiles.
* Fixed a crash when using Move Tab to Another Window.
* Fixed several crashes that could occur during browser startup, profile switching, window teardown, and vertical tab cleanup.
* Fixed a crash when opening the bookmark dialog from the focused address-bar button.
* Fixed a crash when using IME input through DevTools on a prerendered page.
* Fixed visual trails and stale highlights when dragging vertical tabs or expanding collapsed tab groups.
* Fixed Saved Tab Groups calculating incorrect tab move destinations when some synced tabs were not open locally.

## v1.0.728.1

### Local Profiles

New profiles are now created as local profiles without taking you through onboarding.

* You can sign in later from the New Tab Page.
* Signing in is required if you want to use AI through the Aside Provider on that profile.

### Custom Profile Names

You can now customize your profile name. Aside will display the Chromium profile name instead of your Aside account name.

### Fixes and Improvements

* Fixed websites that use a large amount of storage or cookies at once, such as `chess.com`, failing to load.
* Fixed multi-selected tabs not showing their selected state in the UI.
* Fixed an occasional crash after completing onboarding.
* Fixed an occasional crash when closing the browser.
* Fixed the address bar occasionally showing an internal extension URL instead of the search field when opening Agent Manager directly in a new tab.
* Fixed some browser shortcuts not working while the Tab Switcher was open.
* Fixed `Command + C` and `Command + V` not working in the Aside Password Manager popup and Tab Search window on macOS.
* Updated Chromium from `150.0.7871.129` to `150.0.7871.183`.

Thanks as always for all the feedback and bug reports!

## v1.0.724.1

### Smoother Profile Switching

* Fixed lag and crashes when switching profiles by swiping left or right.
* Profile switching is now smoother and uses fewer system resources.
* Fixed Chats and new tasks opening under the wrong Aside account when the browser profile order did not match the order of signed-in Aside accounts.
* Fixed extension buttons and macOS Bookmarks/History menus retaining the previous profile's state after switching profiles.

### Toolbar and Address bar

* Fixed toolbar icon customization not working through Chromium's **Appearance > Customize toolbar** settings.
* Fixed customized toolbar buttons becoming invisible or unclickable while still occupying space.
* The **Ask Aside** button will now always remain on the far right of the toolbar.
* Fixed the address bar changing height or losing its border when Autofill results appeared.

### Tabs and Sidebar

* Fixed the vertical tab sidebar width resetting after restarting the browser.
* Fixed vertical scrolling not working in the vertical tab sidebar.
* Fixed a crash when the active tab changed while the Tab Switcher was closing.
* Fixed Split Tabs activating the wrong tab or the previously active tab when focus changed.
* Fixed visual artifacts remaining when another tab became active during a tab drag.
* Fixed an occasional crash when dragging bookmark items in the vertical tab sidebar.

### Sync and Session Reliability

* Fixed a crash when restoring a session that contained no valid restorable tabs.
* Fixed tab group cloud sync failing to preserve the correct tab URLs, titles, and icons.

### Other crash fixes

* Fixed a crash when resetting browser settings in Incognito mode.
* Fixed an occasional crash while loading extensions.
* Fixed an occasional crash when JavaScript dialogs such as `window.alert` appeared.
* Fixed an occasional crash when using Auto PiP.
* Fixed a crash during Aside Password Manager Autofill when Chromium's password manager database was corrupted.

Thanks for continuing to send us your reports. They help us track down the difficult edge cases and make Aside more stable with every release.

## v1.0.720.1

### Fixes and improvements

* Fixed several crashes that could occur during startup, profile switching, window closing, and browser shutdown.
* Fixed the History menu on macOS showing items from the previous profile after switching profiles, or regular browsing history in Incognito mode.
* Fixed the Bookmarks bar—including in Split View—continuing to show the previous profile's bookmarks after switching profiles. Also fixed a crash in the bookmarks overflow menu after its contents changed.
* Fixed a crash that could occur when the last tab in a synced Tab Group was removed on another device.
* Fixed Split View sometimes activating the wrong pane after rapid focus changes or reversing the pane order.
* Fixed camera and microphone previews in permission prompts failing before device detection completed.
* Fixed profile pictures sometimes failing to load during startup.
* Fixed crashes involving the **Ask Aside** button in Split View and extension buttons during shutdown or immediately after being unpinned.
* Fixed a crash that could occur when closing a page while an AI request was still running.
* Fixed a crash when certain controls were activated with assistive technologies.

No new features in this version. This one's all about stability improvements.

## v1.0.719.1

### New: Tab Switcher

* Available when you have two or more tabs open.
* Press `Ctrl + Tab` to open the switcher.
* Keep holding `Ctrl` and press `Tab` to preview and switch between your open tabs.

### New: Pinned Tab cloud sync

* Your Pinned Tabs can now sync through the cloud.

### New: New tabs now open at the top

* New tabs in the vertical tab sidebar now appear at the top of the tab list instead of the bottom.

### Fixes and improvements

* Fixed several crashes in Incognito mode.
* Fixed **Ask Aside** continuing to reference the previous profile after switching profiles.
* Fixed an out-of-memory crash that could occur when the browser was left running for a long time.
* Fixed redirects from a Pinned Tab repeatedly creating new tabs.
* Added a close button to approval dialogs in the Chat section. These dialogs will also dismiss automatically when they lose focus.
* Fixed the active tab in the Bookmarks section jumping into the regular tab list when switching profiles.
* Updated Chromium from `150.0.7871.115` to `150.0.7871.129`.

Thanks as always for all the reports and feedback!

## v1.0.714.1

### New and improved

* Added profile switching with Ctrl (^) + 1 through Ctrl (^) + 9.
  * You can now switch profiles by profile order using shortcuts like Ctrl + 1, Ctrl + 2, and so on.

* Duplicating a pinned tab now clearly opens the duplicate as a new tab.
  * Fixed the previous behavior where duplicated pinned tabs could appear inside the pinned tab area.
  * Fixed weird UI states that could happen after duplicating pinned tabs.

### Fixes and improvements

* Fixed a crash that could happen when the cookie controls modal closes.
* Fixed pinned tabs being duplicated abnormally after updating.
* Fixed an occasional crash when changing tab modes.
* Fixed tab mode changes from the context menu not syncing with the tab mode state in Aside Settings.
* Fixed macOS menu bar items for bookmarks, tabs, and profiles still being matched to the previous profile after switching profiles.
* Fixed tooltips not disappearing properly.
* Fixed Aside Components occasionally failing to download.

## v1.0.713.3

### New: Profile Switcher

You can now switch profiles inside a single window.

* In vertical tabs, swipe left/right on a macOS trackpad to smoothly switch profiles.
* In horizontal tabs, click the profile icon to switch to another profile.

### Hidden option: disable window background transparency

We added a hidden option to remove background transparency at the system level.

Disable window background vibrancy:

```
defaults write at.studio.AsideBrowser windowBackgroundVibrancyDisabled -bool true
```

Restore default behavior:

```
defaults delete at.studio.AsideBrowser windowBackgroundVibrancyDisabled
```

### Bookmark drag UX improvements

* Replaced the old blue-line bookmark drag UX with the same drag experience used for tabs.
* Fixed a crash that could happen while dragging bookmark items.

### Fixes and improvements

* Fixed agents using only the first profile instead of the requested profile in multi-profile environments.
* Fixed tabs occasionally detaching into a new window while dragging.
* Fixed the horizontal tab Shrink Tab option not being saved in the UI.
* Fixed the close button in the horizontal tab Agent Tabs popup showing up in red.
* Fixed tabs not rendering after entering and exiting fullscreen while using horizontal tabs.
* Fixed tabs not merging into another window properly.
* Fixed the onboarding window being resizable.
* Fixed a crash when focusing in/out of split tabs.
* Fixed layout artifacts remaining in the vertical sidebar when Agent Tabs appear.
* Fixed existing tab groups disappearing after restarting the browser or switching profiles.
* Fixed pinned tabs becoming inaccessible “ghost tabs” in certain cases.
* Fixed Aside Updater crashing periodically.
* Updated Chromium from 150.0.7871.47 to 150.0.7871.115.

## v1.0.706.1

### Major fixes

* Fixed the issue where Aside could cause CPU spikes and keep triggering the GPU / macOS WindowServer.
  * Your laptop should no longer heat up just from using Aside. Depending on what you’re doing, it can still get warm, but it should be much better than before.

* Fixed Google OAuth2 sign-in getting logged out too often.
  * We know many of you reported this, and we’ve patched the area we suspected.
  * At least on my machine, Google sign-in has stayed logged in for over 2 days now.

### New features

* Added Auto PiP.
  * When a video is playing and you switch to another tab, the video can automatically pop out into Picture-in-Picture.
  * Off by default. You can enable it in Settings > General.

* Added non-scroll mode for horizontal tabs.
  * Like stock Chrome, tab widths will shrink to fit the window instead of requiring horizontal scrolling.
  * Off by default. You can enable it in Settings > General.

* Pinned Tab v2
  * ⚠️ Warning: This is not compatible with the previous pinned tab system. Sorry for the hassle, but please unpin your existing pinned tabs and pin them again.
  * Pinned tabs will no longer automatically open in the background.
  * This fixes the issue where pinned tabs could use too much memory.
  * After we launched pinned tabs, Aside could use abnormal memory because Chromium’s pinned tab behavior keeps them alive in the background. We changed that behavior.
  * You can now drag bookmarks into the pinned tab area to turn them into pinned tabs.
  * Pinned tabs no longer disappear after restarting the browser.
  * Fixed pinned tab dragging not working when the vertical tab sidebar is in floating mode.

### Other changes

* Aside Password Manager can now be unpinned and pinned again.
* Aside now restores your previous session when launching the browser.
* It no longer opens as a fresh new window by default.
* Fixed tab order getting mixed up when switching tabs with Command + 1 through Command + 9.
* Updated Chromium from 149.0.7827.197 to 150.0.7871.47.

## v1.0.630.1

### New features

* Added Pinned Tabs.
  * You asked for it a lot, so it’s here.
  * Right-click a tab and choose pin, or if you use vertical tabs, drag the tab to the very top.
  * Tab dragging in vertical tabs is available when you have 2 or more tabs.
  * Horizontal tabs support pinned tabs too, but for now just right-click the tab and pin it from there.
* The floating vertical tab sidebar now appears when you hover near the left edge of the browser.
  * Previously, you had to hover the “Expand sidebar” button.
  * Now it works more like Arc: move your cursor near the left edge and the sidebar will appear.

### Fixes and improvements

* Fixed the bookmark bar not showing on the New Tab page.
* Fixed extension submenus disappearing immediately when hovering over them.
* Fixed broken tab rendering when using Split View with horizontal tabs.
* Fixed an occasional crash when importing data from Chromium-based browsers.
* Fixed a tooltip overlapping other components when dragging a tab into the bookmarks section.
* Fixed tab shadows not disappearing properly while scrolling in horizontal tab mode.

## v1.0.626.1

June 26, 2026

### Fixes and improvements

* Fixed an issue where the profile area and buttons overlapped in the vertical tab sidebar.
* Fixed installed extensions being cut off when there are many extensions. The list is now scrollable.
* Clicking an extension in the installed extensions list now opens it directly.
* Fixed incorrect web content corner rendering in fullscreen mode.
* Fixed broken rendering of the first tab item when using horizontal tabs in fullscreen mode.
* Fixed a light-blue color appearing in the corner area when using horizontal tabs in fullscreen mode. (in Light mode)
* Fixed the floating vertical tab sidebar view covering the “Expand sidebar” button in fullscreen mode.
* Fixed Chromium-based browser bookmark imports not preserving folder depth. Bookmark structure is now preserved.
* Added support for showing the full URL in the address bar.
* Fixed key color sampling issues on webpages that use backdrop blur or transparency.
* Increased the maximum width of the sidebar and side panel to around 520px.
* Updated Chromium from 149.0.7827.156 to 149.0.7827.197.
* Fixed onboarding not working on Intel Macs.

## 1.0.624.1

June 24, 2026

* \[Improvement] **Browser engine**: Updates the Chromium base from 149.0.7827.156 to 149.0.7827.197.
* \[Improvement] **Bundled Aside components**: Updates the bundled agent, password manager, and local service components to the latest release.

## 1.0.623.1

June 23, 2026

* \[Feature] **Tab search**: Adds tab search from the sidebar, with a floating bubble and quick actions.
* \[Feature] **Aside extensions menu**: Adds a toolbar extensions menu with pin controls and live submenu updates.
* \[Improvement] **Windows menus**: Improves browser menus on Windows.
* \[Improvement] **Account password gate**: Polishes the account password popup.
* \[Fix] **New tab reload**: Disables Reload on Aside new tab pages.
* \[Fix] **Cold-start URLs**: Prevents macOS cold-start URL opens from leaving an extra new tab window.

## 1.0.619.1

June 20, 2026

* \[Feature] **Browser settings**: Adds language and search engine settings controls.
* \[Feature] **Browser import**: Adds bookmarks-only import and Safari import support.
* \[Feature] **Task popovers**: Adds recent task popovers in the sidebar.
* \[Feature] **Password manager popup**: Opens the password manager in a macOS popover.
* \[Fix] **Apple Passwords**: Improves Apple Passwords support.
* \[Fix] **Horizontal tabs**: Keeps tab dragging working through trailing tab strip space.

## 1.0.615.1

June 15, 2026

* \[Improvement] **Toolbar colors**: Improves toolbar contrast and color sampling.
* \[Improvement] **Split view**: Refines split view rounding.
* \[Improvement] **Vertical tabs**: Makes vertical tab animations smoother.

## 1.0.611.1

June 12, 2026

* \[Feature] **Bookmark tab menu**: Adds bookmark actions to the tab menu.
* \[Fix] **Inactive tabs**: Restores close buttons on hovered inactive tabs.
* \[Fix] **macOS tooltips**: Hides tooltips when the window deactivates.

## 1.0.609.2

June 9, 2026

* \[Feature] **Chats sidebar actions**: Adds actions for bulk read, archive, and show all.
* \[Feature] **Horizontal Agent Tabs**: Adds the horizontal Agent Tabs chip and bubble.
* \[Fix] **Extensions menu**: Cleans up the profile menu extension list.

## 1.0.605.1

June 5, 2026

* \[Feature] **Profile menu**: Adds an Aside profile menu bubble.
* \[Improvement] **Toolbar dragging**: Expands toolbar drag hit areas.
* \[Fix] **Background updates**: Improves shutdown behavior during background updates.

## 1.0.603.1

June 3, 2026

* \[Feature] **Agent Tabs**: Renames AI tab groups to Agent Tabs.
* \[Feature] **Floating vertical tabs**: Adds collapsed vertical tab hover previews over page content.
* \[Feature] **Notification sync**: Keeps notification permission changes in sync.

## 1.0.531.1

June 1, 2026

* \[Feature] **Aside shortcuts**: Adds Ask Aside, New Task, split tab, and copy URL shortcuts.
* \[Feature] **Windows imports**: Adds Windows import support for Chrome, Edge, Arc, and Comet.
* \[Fix] **AI Tabs boundaries**: Keeps Aside extension pages and New Task tabs outside AI Tabs groups.

## 1.0.526.1

May 27, 2026

* \[Feature] **AI Tabs takeover**: Adds a Take over action that releases a tab from AI Tabs control.
* \[Improvement] **Browser chrome**: Refreshes browser frame, omnibox, capture, permission, profile, and common control styling.
* \[Fix] **Vertical tabs**: Prevents a vertical tab crash after switching tab modes.

## 1.0.522.1

May 22, 2026

* \[Feature] **Tasks in vertical tabs**: Adds task rows, statuses, polling, and singleton task tabs.
* \[Fix] **New tab override**: Preserves the Aside new tab page during extension reloads.
* \[Fix] **Profile menu state**: Resets the profile menu button after menus close.

## 1.0.520.1

May 20, 2026

* \[Feature] **macOS menus**: Preserves menu shortcuts and saved tab group submenus in macOS menus.
* \[Fix] **Password gate menu state**: Disables Settings while the Aside password gate is active.
* \[Fix] **Bookmark placeholder**: Keeps the empty bookmark placeholder responsive while the sidebar shrinks.

## 1.0.519.1

May 19, 2026

* \[Feature] **macOS profile menu**: Adds a profile menu for the vertical tab sidebar.
* \[Fix] **AI Tabs input**: Fixes input positioning under AI Tabs viewport scaling.

## 1.0.518.1

May 18, 2026

* \[Feature] **Media controls**: Places global media controls before Ask Aside and keeps them visible.
* \[Feature] **Bookmark accordion**: Remembers whether the bookmark section is expanded.
* \[Fix] **Import stability**: Improves imported cookie handling.

## 1.0.516.1

May 16, 2026

* \[Improvement] **Dark mode**: Applies forced dark mode earlier and reports it through settings.
* \[Fix] **Password gate downloads**: Keeps password gate downloads out of normal download UI.
* \[Fix] **Aside startup**: Waits to activate Aside surfaces while the account password gate is open.

## 1.0.515.1

May 15, 2026

* \[Feature] **Browser import**: Adds import paths for Firefox, Safari, Chromium, Dia, Atlas, and Comet.
* \[Feature] **Browser preferences**: Exposes sync status, dock, keep-tasks-running, and import controls.
* \[Feature] **Account password gate**: Adds dedicated password gate windows.

## 1.0.514.1

May 14, 2026

* \[Improvement] **Startup readiness**: Waits for Aside readiness before first browser launch.
* \[Feature] **AI Tabs viewport**: Keeps AI Tabs viewport behavior stable across tab changes.

## 1.0.512.1

May 12, 2026

* \[Feature] **Bundled Aside extensions**: Includes Aside extensions in macOS and Windows browser packages.
* \[Feature] **Aside updates**: Adds support for updating bundled Aside extensions.
* \[Feature] **Windows styling**: Improves vertical tab styling on Windows.

## 1.0.510.1

May 11, 2026

* \[Fix] **AI Tabs preview**: Stabilizes AI Tabs previews and iframe interactions.

## 1.0.507.1

May 7, 2026

* \[Feature] **Page Info**: Adds the redesigned Page Info bubble and subpages.
* \[Fix] **Incognito new tab**: Loads Aside new tab resources in incognito without a reload.

## 1.0.415.1

April 16, 2026

* \[Feature] **Aside account auth**: Adds Aside account authentication and sync.

## 1.0.401.1

April 1, 2026

* \[Feature] **Tab clear and tidy**: Adds tab clear and tidy actions.

## 1.0.331.1

March 31, 2026

* \[Feature] **AI Tabs group design**: Adds the new tab group design and AI Tabs behavior.

## 1.0.330.1

March 30, 2026

* \[Feature] **Omnibox integration**: Adds Aside integration in the browser address bar.

## 1.0.327.1

March 27, 2026

* \[Feature] **Permission bubbles**: Redesigns permission bubbles.

## 1.0.323.2

March 23, 2026

* \[Feature] **AI notification permissions**: Adds notification permission prompts for AI features.

## 1.0.322.1

March 22, 2026

* \[Feature] **Toolbar and sidebar redesign**: Redesigns toolbar and sidebar areas.

## 1.0.319.1

March 19, 2026

* \[Feature] **Browser UI refresh**: Updates the browser frame and controls.

## 1.0.317.1

March 17, 2026

* \[Feature] **Toolbar redesign**: Ships the first toolbar redesign.

## 1.0.314.1

March 14, 2026

* \[Feature] **Browser data import**: Adds data import from Chrome, Safari, and Arc.

## 1.0.312.1

March 12, 2026

* \[Feature] **Side panel resizing**: Adds side panel resizing.

## 1.0.311.1

March 11, 2026

* \[Feature] **Fullscreen agent sidebar**: Expands the agent sidebar to full height and adds key color transitions.

## 1.0.308.1

March 8, 2026

* \[Feature] **Split view redesign**: Applies the new split view design.

## 1.0.304.1

March 4, 2026

* \[Fix] **Backdrop filters**: Supports backdrop filter rendering on transparent backgrounds.

## 1.0.303.1

March 3, 2026

* \[Feature] **App updater**: Adds updater self-update support.
* \[Feature] **Side panel agent**: Moves the browser agent into the side panel.

## 1.0.301.1

March 1, 2026

* \[Feature] **Vertical tab bookmarks**: Adds bookmark support in vertical tabs.
* \[Feature] **Liquid Glass**: Applies Liquid Glass on macOS Tahoe and newer.

## 1.0.225.1

February 25, 2026

* \[Feature] **Initial Aside Browser release**: Adds the macOS toolbar, address entry, search engine controls, tab support, dark-mode browser theming, and updates.
