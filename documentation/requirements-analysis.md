# Main takeways from REQ analysis

## Input

- MUST be done through STDIN
- All operations MUST be processed as being from the same account
- Each operation MUST be processed in FIFO order
- Each operation is a JSON object
- Each operation MUST be in a single line
- Numbers MUST represented as floats

### Format of Input

```json
{
    "account": 
    {
        "client_id": int,
        "active_card": boolean,
        "available_limit": float
    }
}

{
    "debit": 
    {
        "merchant": string, 
        "amount": float, 
        "time": datetime
    }
}
```

## Output

- MUST be done through STDOUT to a output file
- Output file MUST be out of the container
- Each output is a JSON object
- Each output MUST be in a single line
- Numbers MUST represented as floats
- The output MUST be the result of the operation processed
- MUST be in the same order as the input

### Format of Output

```json
{
    "account": 
    {
        "client_id": int,
        "active_card": boolean, 
        "available_limit": float
    },
    
    "violations": ["string"]
}
```

## Operations

- Create account
- Deposit

Interface MUST be implemented as a class in order to allow for easy extension of operations in the future

### Possible Handled Violations

- #### Account not initialized (aka account-not-initialized)

When trying to debit from an account that was not initialized in the output file

- #### Insufficient limit (aka insufficient-limit)

When the account does not have enough limit to debit

- #### High frequency small interval (aka high-frequency-small-interval)

When the account has more than 3 transactions in a 2 minutes interval

- #### Doubled transaction (aka doubled-transaction)

When the transaction is a duplicate of a previous transaction in the span of 2 minutes
