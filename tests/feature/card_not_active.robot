*** Settings ***
Documentation       Output a violation when trying to authorize a transaction without an active card
Resource            ./environment.resource
Library             Process
Library             OperatingSystem
Suite Teardown      Terminate All Processes    kill=True

*** Variables ***
${expected_output}      {"account": {"client_id": 1234, "active_card": false, "available_limit": 100.00}, "violations": ["card-not-active"]}

*** Test Cases ***
Check Output
    ${result}           Run Process     ${application} < ${tests_path}/card_not_active.operations  shell=true
    Log                 ${result.stdout}
    Log                 ${result.stderr}
    Should Contain      ${result.stdout}    ${expected_output}
