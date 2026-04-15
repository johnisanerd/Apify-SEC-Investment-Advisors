# 📊 SEC Investment Advisors Scraper: Scrape SEC IAPD Financial Professional Data with Python

> **The most efficient, reliable, and developer-friendly SEC investment advisor data scraper**

**Actor page:** [apify.com/johnvc/ApifySECInvestmentAdvisors](https://apify.com/johnvc/ApifySECInvestmentAdvisors?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/ApifySECInvestmentAdvisors/input-schema](https://apify.com/johnvc/ApifySECInvestmentAdvisors/input-schema?fpr=9n7kx3)

Scrape SEC investment advisor and financial professional data with Python using the [Investment Finance Professionals scraper on Apify](https://apify.com/johnvc/ApifySECInvestmentAdvisors?fpr=9n7kx3). Access 250,000+ investment professionals and 15,000+ registered financial firms from SEC IAPD records - with filtering by name, location, CRD numbers, and contact IDs.

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-SEC-Investment-Advisors.git
   cd Apify-SEC-Investment-Advisors
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you don't have it:
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

### Alternative: Set API Key Directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python sec-investment-advisors-scraper.py
```

## 🌟 Why Use This SEC Investment Advisors Scraper?

The [SEC Investment Advisors scraper on Apify](https://apify.com/johnvc/ApifySECInvestmentAdvisors?fpr=9n7kx3) delivers structured data from the SEC's Investment Adviser Public Disclosure (IAPD) database - the official federal registry of registered investment advisors, financial firms, and licensed investment professionals in the United States.

**Official Federal Data, Programmatically Accessible**: The SEC IAPD database is the authoritative public record for registered investment advisors in the US. This scraper makes that data available as clean, structured JSON - no manual searching, no copying from web forms, no pagination through the SEC's own interface.

**250,000+ Contacts, 15,000+ Firms**: The database covers the full scope of SEC-registered investment professionals and advisory firms. Filter by state, city, firm name, or CRD number to surface exactly the subset of contacts or firms relevant to your research, sales, or compliance workflow.

**Dual Query Modes - Contacts and Firms**: Use `query_type: "contacts"` to retrieve individual investment professionals, or `query_type: "firms"` to retrieve registered advisory firms. Each mode returns the fields most relevant to its record type, and both support geographic and identifier-based filtering.

**CRD Number Filtering**: CRD (Central Registration Depository) numbers are the unique identifiers for registered investment advisors and firms in US financial regulation. Filter by `organization_crds` to pull specific firms, or use `exclude_organization_crds` to remove known entities from your results - useful for building clean prospecting lists.

**Pay-Per-Event Pricing**: Pricing is $0.02 per run plus $0.02 per contact returned. You pay only for the records you retrieve - making it cost-effective for targeted lookups as well as large dataset builds.

**Built for Finance and Compliance Workflows**: SEC advisor data powers financial services sales prospecting, regulatory compliance research, advisor network mapping, and due diligence workflows. The [Investment Finance Professionals scraper](https://apify.com/johnvc/ApifySECInvestmentAdvisors?fpr=9n7kx3) returns data structured for direct integration into CRMs, compliance tools, and research pipelines.

## 🎯 Common Use Cases for SEC Investment Advisor Data

**Financial Services Prospecting**: Build targeted lists of registered investment advisors and firms for financial product sales outreach - filtered by geography, firm size, or CRD status.

**Regulatory Compliance Research**: Verify advisor registration status, identify affiliated firms, and cross-reference CRD numbers against the official SEC registry for due diligence workflows.

**Advisor Network Mapping**: Map the relationships between investment professionals and firms in specific markets or regions to understand competitive dynamics and referral networks.

**Market Research**: Analyze the geographic distribution, concentration, and characteristics of registered investment advisors across US cities and states.

**Data Enrichment**: Enrich an existing contact database with SEC registration details, CRD numbers, and firm affiliations sourced directly from the federal registry.

**Academic and Policy Research**: Build datasets of registered financial professionals for academic research on financial regulation, advisor demographics, or market structure.

## ⚡ Features

### Core Capabilities
- **SEC IAPD Database**: Accesses the official federal registry of US registered investment advisors and firms
- **Dual Query Modes**: Retrieve individual contacts or registered firms with a single parameter switch
- **Geographic Filtering**: Filter by state, city, and country to target specific markets
- **CRD Number Lookup**: Filter or exclude records by CRD number for precise identifier-based queries
- **Contact ID Filtering**: Retrieve or exclude specific contacts by contact ID
- **Date Filtering**: Filter records by last update date to surface recently changed registrations

### Data Quality
- **Official Source Data**: Records sourced directly from the SEC IAPD public database
- **Consistent JSON Schema**: Contacts and firms each return predictable, structured field sets
- **Firm Affiliation Data**: Contact records include affiliated firm information
- **CRD Numbers Included**: Every record includes the official CRD identifier for cross-referencing
- **Per-Contact Billing**: Charged per contact returned for accurate, predictable cost control

## 📖 Usage Examples

### Basic Search: Scrape Investment Advisor Contacts by State

```json
{
  "query_type": "contacts",
  "firm_state": "NY",
  "contacts_limit": 50
}
```

### Advanced Search: Firm Query with City and Limit

Retrieve registered investment advisory firms in San Francisco with a limit of 25 results.

```json
{
  "query_type": "firms",
  "firm_city": "San Francisco",
  "firm_state": "CA",
  "firms_limit": 25
}
```

### Lookup by CRD Number

Retrieve contacts associated with specific firm CRD numbers.

```json
{
  "query_type": "contacts",
  "organization_crds": "123456,789012",
  "contacts_limit": 100
}
```

## 🔍 Input Parameters

Full input schema reference: [apify.com/johnvc/ApifySECInvestmentAdvisors/input-schema](https://apify.com/johnvc/ApifySECInvestmentAdvisors/input-schema?fpr=9n7kx3)

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query_type` | `str` | no | `"contacts"` | Data type: `"contacts"` or `"firms"` |
| `firm_name` | `str` | no | - | Filter by firm name |
| `firm_city` | `str` | no | - | Filter by city |
| `firm_state` | `str` | no | - | Filter by state code (e.g. `"CA"`) |
| `firm_country` | `str` | no | - | Filter by country |
| `firms_limit` | `int` | no | `100` | Max firms to return |
| `contact_ids` | `str` | no | - | Comma-separated contact IDs to include |
| `exclude_contact_ids` | `str` | no | - | Comma-separated contact IDs to exclude |
| `contact_firm_name` | `str` | no | - | Filter contacts by firm name |
| `organization_crds` | `str` | no | - | Comma-separated CRD numbers to include |
| `exclude_organization_crds` | `str` | no | - | Comma-separated CRD numbers to exclude |
| `date_updated` | `str` | no | - | Filter by last update date |
| `contacts_limit` | `int` | no | `10` | Max contacts to return |
| `output_file` | `str` | no | - | Optional output filename |

## 📊 Output Format

Each run returns a dataset of structured JSON objects. Sample output for contacts:

```json
{
  "query_type": "contacts",
  "firm_state": "CA",
  "firm_city": "San Francisco",
  "contacts_returned": 25,
  "contacts": [
    {
      "contact_id": "1234567",
      "first_name": "Jane",
      "last_name": "Smith",
      "crd_number": "7654321",
      "firm_name": "Pacific Wealth Advisors LLC",
      "firm_crd": "123456",
      "city": "San Francisco",
      "state": "CA",
      "country": "United States",
      "registration_status": "Approved",
      "last_updated": "2025-01-15"
    },
    {
      "contact_id": "2345678",
      "first_name": "Robert",
      "last_name": "Chen",
      "crd_number": "8765432",
      "firm_name": "Bay Area Capital Management",
      "firm_crd": "234567",
      "city": "San Francisco",
      "state": "CA",
      "country": "United States",
      "registration_status": "Approved",
      "last_updated": "2025-02-03"
    }
  ]
}
```

---

[**Made with love**](https://apify.com/johnvc?fpr=9n7kx3)

*Transform your data collection with the most reliable and efficient scraper on the market.*

Last Updated: 2026.04.15
