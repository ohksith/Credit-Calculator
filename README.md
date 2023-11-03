# Credit-Calculator
This Git project is a loan calculator designed to handle differentiated and annuity payments. It allows users to calculate loan payments based on parameters such as principal, interest rate, and the number of monthly payments. 
In this stage, we focus on calculating differentiated payments, where the loan principal is reduced by a constant amount each month. 
The rest of the monthly payment goes towards interest repayment and gradually decreases over the loan's term. Users can specify the type of payment and provide relevant input parameters via command-line arguments.

## Features

- Calculation of differentiated payments based on user-provided parameters (principal, interest rate, number of monthly payments).
- Ability to calculate annuity payments, including principal, number of monthly payments, and monthly payment amount.
- Handling of invalid parameters with informative error messages to guide the user.
- Computation of overpayment, which represents the total interest paid over the loan's term.

## Command-Line Usage

To use the loan calculator, users can provide command-line arguments, including:

**python creditcalc.py --type=<payment_type> --principal=<principal> --periods=<num_of_months> --interest=<annual_interest_rate>**


- `--type` specifies the payment type, which can be "diff" (differentiated) or "annuity" (annuity).
- `--principal` is the loan principal amount.
- `--periods` is the number of monthly payments.
- `--interest` represents the annual interest rate (provided as a float value).

## Error Handling

The program performs error handling for various scenarios, such as:

- Incorrect or missing `--type` argument.
- Invalid combinations of input parameters.
- Insufficient input parameters (fewer than four).
- Negative values provided for principal, periods, or interest.

## Examples

Here are some examples of how to use the loan calculator:

- Calculating differentiated payments:

>python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
```
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834
Overpayment = 45837
```


- Calculating the annuity payment:

>python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
```
Your annuity payment = 21248!
Overpayment = 274880
```
- Handling incorrect input:

>python creditcalc.py --type=diff --principal=1000000 --payment=104000
```
Incorrect parameters.
```
