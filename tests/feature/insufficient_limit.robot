*** Settings ***
Documentation       Output a violation when trying to authorize a transaction without available limit
Resource            ./environment.resource
Library             Process
Library             OperatingSystem
Suite Teardown      Terminate All Processes    kill=True

*** Variables ***
${expected_output}      {"account": {"client_id": 1234, "active_card": true, "available_limit": 50.00}, "violations": ["insufficient-limit"]}

*** Test Cases ***
Check Output
    ${result}           Run Process     ${application} < ${tests_path}/insufficient_limit.operations  shell=true
    Log                 ${result.stdout}
    Log                 ${result.stderr}
    Should Contain      ${result.stdout}    ${expected_output}
