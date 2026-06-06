# 📊 SEC Investment Advisors API: RIA Firm and Advisor Data in Clean JSON

> The efficient, reliable, and developer-friendly way to use the SEC Investment Advisors API.

**Actor page:** [apify.com/johnvc/SECInvestmentAdvisorContacts](https://apify.com/johnvc/SECInvestmentAdvisorContacts?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/SECInvestmentAdvisorContacts/input-schema](https://apify.com/johnvc/SECInvestmentAdvisorContacts/input-schema?fpr=9n7kx3)

The SEC Investment Advisors API returns structured data from the SEC's Investment Adviser Public Disclosure (IAPD) records, the official federal registry of registered investment advisors, advisory firms, and licensed investment professionals in the United States. Choose firms, contacts, or both, then filter by name, location, organization CRD numbers, contact IDs, or update date. Results come back as clean JSON, ready for a CRM, compliance tool, or research pipeline.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-SEC-Investment-Advisors.git
   cd Apify-SEC-Investment-Advisors
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python sec-investment-advisors-scraper.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python sec-investment-advisors-scraper.py
```

## Why Use This SEC Investment Advisors API?

**Official federal data, programmatically accessible.** The SEC IAPD database is the authoritative public record for registered investment advisors in the US. This API returns it as clean, structured JSON, with no manual searching and no paging through web forms.

**Dual query modes.** Use `query_type: "contacts"` for individual investment advisor representatives, `query_type: "firms"` for registered advisory firms, or `"both"` to get each in a single run.

**CRD number filtering.** CRD (Central Registration Depository) numbers uniquely identify registered advisors and firms. Include specific firms with `organization_crds`, or remove known entities with `exclude_organization_crds` to build clean lists.

**Incremental sync.** Use `date_updated` to return only records changed on or after a given date, so you can keep a downstream dataset fresh without refetching everything.

**Predictable, pay-per-use pricing.** Billing is per contact returned, with a small per-run setup fee and no subscription. You pay only for the records you retrieve.

**Built for finance and compliance workflows.** The data fits prospecting, compliance research, advisor network mapping, and due diligence pipelines.

## Features

### Core Capabilities
- **SEC IAPD records** for US registered investment advisors and firms
- **Dual query modes** for contacts, firms, or both
- **Geographic filtering** by city, state, and country
- **CRD number lookup** to include or exclude specific firms
- **Contact ID filtering** to include or exclude specific contacts
- **Date filtering** with `date_updated` for incremental syncs

### Data Quality
- **Official source data** drawn from the SEC IAPD public records
- **Consistent JSON schema** for both contacts and firms
- **Firm affiliation** included on contact records
- **CRD numbers** on every record for cross-referencing
- **Per-contact billing** for predictable cost control

## Usage Examples

### Firms by name
```json
{
  "query_type": "firms",
  "firm_name": "Vanguard",
  "firms_limit": 5
}
```

### Contacts at specific firms (by CRD), small limit
```json
{
  "query_type": "contacts",
  "organization_crds": "7691,250",
  "contacts_limit": 10
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query_type` | `string` | No | `contacts` | Data to return: `firms`, `contacts`, or `both`. |
| `firm_name` | `string` | No | - | Filter firms by primary business name (partial, case-insensitive). |
| `firm_city` | `string` | No | - | Filter firms by main office city. |
| `firm_state` | `string` | No | - | Filter firms by state (2-letter code, e.g. `CA`). |
| `firm_country` | `string` | No | - | Filter firms by country (ISO 3166-1 alpha-2, e.g. `US`). |
| `firms_limit` | `integer` | No | `100` | Maximum firms to return. |
| `contact_ids` | `string` | No | - | Include only these contact IDs (comma-separated or JSON array). |
| `exclude_contact_ids` | `string` | No | - | Exclude these contact IDs. |
| `contact_firm_name` | `string` | No | - | Filter contacts by their firm's name. |
| `organization_crds` | `string` | No | - | Include only contacts from these organization CRD numbers. |
| `exclude_organization_crds` | `string` | No | - | Exclude contacts from these organization CRD numbers. |
| `date_updated` | `string` | No | - | Return only contacts updated on or after this date (`YYYY-MM-DD`). |
| `contacts_limit` | `integer` | No | `10` | Maximum contacts to return. Each contact returned is billed. |
| `output_file` | `string` | No | - | Optional filename to save results. |

## Output Format

A `query_type: "both"` run returns a single item that nests a firms block and a contacts block. The firm record below is real (Vanguard Group Inc); the contact record uses placeholder values because contact records carry personal data (name, email, phone), and your own run returns the real values.

```json
{
  "query_type": "both",
  "query_timestamp": "2026-05-29T11:33:13Z",
  "firms": {
    "search_metadata": { "firms_count": 3, "pages_processed": 1, "limit_reached": true },
    "results": {
      "firms": [
        {
          "organization_crd": "105958",
          "primary_business_name": "VANGUARD GROUP INC",
          "main_office_street_address_1": "100 VANGUARD BLVD",
          "main_office_city": "MALVERN",
          "main_office_state": "PA",
          "main_office_country": "United States",
          "main_office_postal_code": "19355",
          "updated_at": "2025-12-05T08:17:44Z",
          "created_at": "2025-12-04T15:11:49Z"
        }
      ]
    }
  },
  "contacts": {
    "results": {
      "contacts": [
        {
          "contact_id": 1,
          "organization_crd": "70",
          "first_name": "Jane (placeholder)",
          "last_name": "Doe (placeholder)",
          "email": "jane.doe@example.com (placeholder)",
          "phone": "+1-555-0100 (placeholder)",
          "linkedin_url": null,
          "firm_name": "Example Advisors, Inc.",
          "updated_at": "2025-12-05T08:18:32Z",
          "created_at": "2025-12-04T15:12:02Z"
        }
      ]
    }
  },
  "partial_failure": false
}
```

Firm records also include a `website_address` field. Contact records include `email_verified` alongside the contact's name, email, phone, and firm affiliation. When you query a single mode (`firms` or `contacts`), the item holds just that block.

---

## Use as an MCP tool

You can load the SEC Investment Advisors API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/SECInvestmentAdvisorContacts
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the SEC Investment Advisors API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/SECInvestmentAdvisorContacts"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the SEC Investment Advisors API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/SECInvestmentAdvisorContacts"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/SECInvestmentAdvisorContacts" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the SEC Investment Advisors API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/SECInvestmentAdvisorContacts`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/SECInvestmentAdvisorContacts`, using OAuth when prompted.
5. Ask Claude to run the SEC Investment Advisors API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/SECInvestmentAdvisorContacts"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/SECInvestmentAdvisorContacts",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the SEC Investment Advisors API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/SECInvestmentAdvisorContacts`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the SEC Investment Advisors API to power prospecting, compliance research, and due diligence with reliable, structured data.*

Last Updated: 2026.06.07
