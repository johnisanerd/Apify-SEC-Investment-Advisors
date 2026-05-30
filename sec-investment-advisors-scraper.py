"""
Example: call the SEC Investment Advisors API Apify Actor from Python.

Get a free Apify API key at: https://apify.com?fpr=9n7kx3
Set it in a .env file (see .env.example) or export APIFY_API_TOKEN.

This example queries both firms and contacts, scoped to a single firm name
with small limits, so the first run stays inexpensive. The Actor bills per
contact returned, so raise contacts_limit only when you are ready to pay for
more records.
"""

import os

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
if not APIFY_API_TOKEN:
    raise SystemExit(
        "APIFY_API_TOKEN is not set. Copy .env.example to .env and add your key, "
        "or run: export APIFY_API_TOKEN=your_api_key_here"
    )

client = ApifyClient(APIFY_API_TOKEN)

# Inputs are kept small so the first run is inexpensive. Each contact returned
# is billed, so contacts_limit is set low here.
run_input = {
    "query_type": "both",
    "firm_name": "Vanguard",
    "firms_limit": 3,
    "contacts_limit": 3,
}

print(f"Querying SEC investment advisors for firm name: {run_input['firm_name']}")
run = client.actor("johnvc/SECInvestmentAdvisorContacts").call(run_input=run_input)

if run is None:
    raise SystemExit("The Actor run did not start. Check your API token and inputs.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    firms = item.get("firms", {}).get("results", {}).get("firms", [])
    contacts = item.get("contacts", {}).get("results", {}).get("contacts", [])

    print(f"\nFirms returned: {len(firms)}")
    for firm in firms:
        print(f"  - {firm.get('primary_business_name', '')} (CRD {firm.get('organization_crd', '')})")
        print(f"    {firm.get('main_office_city', '')}, {firm.get('main_office_state', '')} {firm.get('main_office_country', '')}")

    print(f"\nContacts returned: {len(contacts)}")
    for contact in contacts:
        name = f"{contact.get('first_name', '')} {contact.get('last_name', '')}".strip()
        print(f"  - {name} | {contact.get('firm_name', '')} (CRD {contact.get('organization_crd', '')})")
        # Each contact record also carries email, phone, and linkedin_url fields.
