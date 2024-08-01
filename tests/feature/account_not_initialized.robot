*** Settings ***
Documentation       Output a violation when trying to authorize a transaction without initialize an account
Resource            ./environment.resource
Library             Process
Library             OperatingSystem
Suite Teardown      Terminate All Processes    kill=True

*** Variables ***
${expected_output}      {"account": {"client_id": 0, "active_card": "false", "available_limit": 0.00}, "violations": ["account-not-initialized"]}

*** Test Cases ***
Check Output
    ${result}           Run Process     ${application} < ${tests_path}/account_not_initialized.operations  shell=true
    Log                 ${result.stdout}
    Log                 ${result.stderr}
    Should Contain      ${result.stdout}    ${expected_output}
