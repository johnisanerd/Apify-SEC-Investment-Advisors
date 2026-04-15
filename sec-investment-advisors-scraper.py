"""
SEC Investment Advisors Scraper: A Quick Start Example
See more at: https://apify.com/johnvc/ApifySECInvestmentAdvisors?fpr=9n7kx3
Input schema: https://apify.com/johnvc/ApifySECInvestmentAdvisors/input-schema?fpr=9n7kx3

This script demonstrates how to scrape SEC investment advisor and financial
professional data using the Investment Finance Professionals scraper on Apify.
Access 250,000+ investment professionals and 15,000+ financial firms from
SEC IAPD records with filtering by name, location, CRD numbers, and more.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "query_type": "contacts",
    "firm_state": "CA",
    "firm_city": "San Francisco",
    "contacts_limit": 25,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/ApifySECInvestmentAdvisors").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
