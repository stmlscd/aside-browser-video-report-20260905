> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aside.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure AI providers

> Use Aside models, connect existing AI subscriptions, or bring your own API key.

# Configure AI providers

Use `Settings > Models` to choose which model providers Aside can use.

## Provider types

Aside supports three provider types.

<Columns cols={3}>
  <Card title="Aside" icon="sparkles">
    Use models included with your Aside plan.
  </Card>

  <Card title="Subscription" icon="badge-check">
    Reuse a supported AI subscription you already pay for.
  </Card>

  <Card title="API" icon="key-round">
    Bring your own provider API key.
  </Card>
</Columns>

Connected providers appear under `Settings > Models > Providers`. Aside labels built-in plan models with your current Aside plan, subscription providers as `Subscription`, and API-key providers as `API`.

## Use Aside plan models

The `Aside` provider uses the models included with your Aside plan. Sign in to an Aside cloud account to use built-in Aside models.

Free users can use the free Aside model set. Pro and Max plans include more Aside model access, including priority models where the current plan allows them.

## Connect an existing AI subscription

Open `Settings > Models > Providers`, choose `Connect`, then choose a provider under `Subscription`.

Current subscription providers include:

* `ChatGPT Subscription`: reuse your ChatGPT Plus or Pro subscription.
* `Claude Subscription`: reuse your Claude Pro or Max subscription.
* `GitHub Copilot`: reuse your GitHub Copilot subscription.

Aside opens an OAuth sign-in flow for these providers. Finish the sign-in in the popup, then return to Aside. Aside can show usage indicators for supported subscription providers.

## Bring your own API key

Open `Settings > Models > Providers`, choose `Connect`, then choose a provider under `API`.

Current API-key providers include:

* Anthropic
* OpenAI
* OpenRouter
* Google
* xAI
* Vercel AI Gateway
* Cloudflare AI Gateway

API-key providers are useful when you want Aside to route model calls through your own provider account. After you connect a key, you can edit it or disconnect the provider from the provider action menu.

## Choose models

Open `Settings > Models > Task models` to choose the default model and review available model categories. Open `Settings > Agents > Chat` to choose follow-up behavior. See [Use follow-ups](/help/tasks#use-follow-ups) for task behavior while a run is active.

## Related

* [Manage subscription](/help/subscription)
* [Use Ultrabrowse](/help/ultrabrowse)
* [Run tasks](/help/tasks)
