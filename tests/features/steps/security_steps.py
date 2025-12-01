import requests
from behave import given, when, then

API = "http://127.0.0.1:8000"

@when('I request emails with region "{payload}"')
def step_injection(context, payload):
    context.response = requests.get(f"{API}/emails?region={payload}")

@then("the system should return 0 results")
def step_no_data(context):
    assert context.response.status_code == 200
    assert context.response.json() == []

@when('I call the "/emails?region=North" endpoint')
def step_call_emails(context):
    context.response = requests.get(f"{API}/emails?region=North")

@then("the response should contain security headers")
def step_headers(context):
    headers = context.response.headers
    assert "X-Content-Type-Options" in headers
    assert "X-Frame-Options" in headers
