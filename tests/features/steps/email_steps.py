import requests
from behave import given, when, then

BASE_URL = "http://127.0.0.1:8000"

@given("the API is running")
def step_impl(context):
    r = requests.get(BASE_URL)
    assert r.status_code in [200, 404]

@when("I trigger email ingestion")
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/ingest")

@then("the system should return a success response")
def step_impl(context):
    assert context.response.status_code == 200
    print("Ingestion Response:", context.response.json())

@given("the API has stored emails")
def step_impl(context):
    # Call ingestion endpoint first
    requests.get(f"{BASE_URL}/ingest")

@when('I request emails for region "{region}"')
def step_impl(context, region):
    context.response = requests.get(f"{BASE_URL}/emails?region={region}")

@then('I should receive a list of emails for "{region}"')
def step_impl(context, region):
    assert context.response.status_code == 200
    data = context.response.json()
    assert isinstance(data, list)
    print(f"Emails for region {region}: {data}")
