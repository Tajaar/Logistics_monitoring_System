Feature: OWASP Security Validation

  Scenario: API should not allow SQL injection through region parameter
    When I request emails with region "' OR 1=1 --"
    Then the system should return 0 results
    
  Scenario: API must return secure headers
    When I call the "/emails?region=North" endpoint
    Then the response should contain security headers
