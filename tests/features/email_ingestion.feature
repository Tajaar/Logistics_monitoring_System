Feature: Email ingestion into the system
  As a healthcare admin
  I want incoming emails from Zoho to be fetched
  So that the system stores them based on region

  Scenario: Ingest emails manually using /ingest endpoint
    Given the API is running
    When I trigger email ingestion
    Then the system should return a success response

  Scenario: Fetch emails for a specific region
    Given the API has stored emails
    When I request emails for region "North"
    Then I should receive a list of emails for "North"
