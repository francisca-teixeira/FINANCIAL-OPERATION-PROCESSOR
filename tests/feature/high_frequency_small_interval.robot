*** Settings ***
Documentation       Output a violation when trying to authorize more than 3 transactions in a time window of 2 minutes
Resource            ./environment.resource
Library             Process
Library             OperatingSystem
Suite Teardown      Terminate All Processes    kill=True

*** Variables ***
${expected_output}      {"account": {"client_id": 1234, "active_card": true, "available_limit": 40.00}, "violations": ["high-frequency-small-interval"]}

*** Test Cases ***
Check Output
    ${result}           Run Process     ${application} < ${tests_path}/high_frequency_small_interval.operations  shell=true
    Log                 ${result.stdout}
    Log                 ${result.stderr}
    Should Contain      ${result.stdout}    ${expected_output}
