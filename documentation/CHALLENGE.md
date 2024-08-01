# Summer Camp Challenge

## Contents

- [Goal](#goal)
- [Requirements](#requirements)
- [Examples](#examples)
- [System Context](#system-context)
- [References](#references)

## [Goal](#contents)

Develop an application which fullfil the requirements following some of the best-practices on Software Engineering.

## [Requirements](#contents)

- RQ01: The code **must** be under version control [following this guide](../CONTRZIBUTING.md)​.

- RQ02: Python (>= 3.12), Pytest and Robot framework **must** be used​.

- RQ03: The application **must** run using Docker containers.

- RQ04: Docker Compose​ **should** be used to orchestrate the containers.

- RQ05: Multiple Docker runtime environments for development, tests and production **could** be provided.

- RQ06: To address observability, the application output from the events processed **must** be saved to an external log file outside the container.

- RQ07: Tests execution **must** be automated.

- RQ08: Each test execution **must** generate a report with coverage.

- RQ09: There **must** be a coverage >= 95% for unit tests.

- RQ10: There **must** be a coverage == 100% for functional tests.

- RQ11: The application **must** receive and process incoming operations as streams of events from STDIN​, according to the pre-defined set of rules.

- RQ12: For each received event, the application **must** provide one output, including the current state of the account and all business rules violations.

- RQ13: The state of the transactions **must** be kept in-memory and not on external database.

- RQ14: The state of the application **must** restart with the application.

- RQ15: The application **must** handle only one account, so all the transactions refers to the same account.

- RQ16: The application **must** support two types of operations: account creation and debit authorization.

- RQ17: For the account creation operation, the application **must** expect to receive an event with the following format: `{"account": {"client_id": 1234, "active_card": true, "available_limit": 100.00}}`.

- RQ18: For the account creation operation, the application **must** output a message with the following format: `{"account": {"client_id": 1234, "active_card": true, "available_limit": 100.00}, "violations": []}`.

- RQ19: For the debit authorization operation, the application **must** expect to receive an event with the following format: `{"debit": {"client_id": 1234, "merchant": "Burger King", "amount": 20.00, "time": "2023-07-31T10:00:00.000Z"}}`.

- RQ20: For the debit authorization operation, the application **must** output a message with the following format: `{"account": {"client_id": 1234, "active_card": true, "available_limit": 80.00}, "violations": []}`.

- RQ21: Operations **must** be implemented as part of an interface, to allow support others operations in the future.

- RQ22: The application **must** support only positive floating point numbers.

- RQ23: The application **must** process events by using FIFO.

- RQ24: The application **must** be resilient to malformed events.

- RQ25: The application **must** authorize an operation based on the current account's state considering the last authorized operations.

- RQ26: The application **must** reject a debit operation against a non-initialized account, while reports the violation: `account-not-initialized`.

- RQ27: The application **must** reject a debit operation against an account without an active card, while reports the violation:  `card-not-active`.

- RQ28: The application **must** reject a debit operation if the amount exceeds the available limit on the account, while reports the violation: `insufficient-limit`.

- RQ29: The application **must** reject more than three debit operations in a two-minutes interval, while reports the violation: `high-frequency-small-interval`.

- RQ30: The application **must** reject a debit operations with the same amount and merchant in a two-minutes interval, while reports the violation: `doubled-transaction`.

## [Examples](#contents)

**Given** the following text file containing multiple bank account operations:

```bash
$ cat operations
{"account": {"client_id": 1234, "active_card": true, "available_limit": 100.00}}
{"debit": {"client_id": 1234, "merchant": "Burger King", "amount": 20.00, "time": "2023-07-31T10:00:00.000Z"}}
```

**When** the file is provided as the input to the application, **then** the following output will be produced:

```bash
$ financial-operation-processor.py < operations
{"account": {"client_id": 1234, "active_card": true, "available_limit": 100.00}, "violations": []}
{"account": {"client_id": 1234, "active_card": true, "available_limit": 80.00}, "violations": []}
```

## [System Context](#contents)

The following C4 diagram presents the system context:

![Context](System%20Context.png)

## [References](#contents)

- [Using V Models for Testing](https://insights.sei.cmu.edu/blog/using-v-models-for-testing)
- [MoSCoW Prioritization Categories](https://www.productplan.com/glossary/moscow-prioritization)
- [The Twelve-Factor App](https://12factor.net)
- [Semantic Versioning 2.0.0](https://semver.org)
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/#summary)
- [C4 Diagrams](https://c4model.com/#SystemContextDiagram)
- [Introduction to C4-PlantUML with Examples](https://purrgramming.life/cs/c4-plantuml)
- [Robot Framework in Python](https://www.geeksforgeeks.org/robot-framework-in-python)
