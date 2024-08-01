*** Settings ***
Documentation       A set of regular transactions without violations
Resource            ./environment.resource
Library             Process
Library             OperatingSystem
Suite Teardown      Terminate All Processes    kill=True

*** Variables ***
${expected_output}      {"account": {"client_id": 1234, "active_card": true, "available_limit": 55.00}, "violations": []}

*** Test Cases ***
Check Output
    ${result}           Run Process     ${application} < ${tests_path}/regular_transaction.operations  shell=true
    Log                 ${result.stdout}
    Log                 ${result.stderr}
    Should Contain      ${result.stdout}    ${expected_output}
