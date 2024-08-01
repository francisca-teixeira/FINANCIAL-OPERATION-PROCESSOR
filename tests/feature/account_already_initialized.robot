*** Settings ***
Documentation       Output a violation when trying to recreate an account
Resource            ./environment.resource
Library             Process
Library             OperatingSystem
Suite Teardown      Terminate All Processes    kill=True

*** Variables ***
${expected_output}      {"account": {"client_id": 1234, "active_card": true, "available_limit": 100.00}, "violations": ["account-already-initialized"]}

*** Test Cases ***
Check Output
    ${result}           Run Process     ${application} < ${tests_path}/account_already_initialized.operations  shell=true
    Log                 ${result.stdout}
    Log                 ${result.stderr}
    Should Contain      ${result.stdout}    ${expected_output}
