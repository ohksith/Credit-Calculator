import math
import argparse


# Line 6-104 - Defining functions
def typeChoicesCheck(a):
    if a != 'annuity' and a != 'diff':
        print('Incorrect parameters!')
        exit()


def noneCheck(a, b, c, d):
    counter = int()
    if a is None:
        counter += 1
    if b is None:
        counter += 1
    if c is None:
        counter += 1
    if d is None:
        counter += 1
    if counter > 1:
        print('Incorrect parameters!')
        exit()


def typeCheck(a):
    if a is None:
        print('Incorrect parameters!')
        exit()


def negativeCheck(a, b, c, d):
    if a is not None:
        if a < 0:
            print('Incorrect parameters!')
            exit()
    if b is not None:
        if b < 0:
            print('Incorrect parameters!')
            exit()
    if c is not None:
        if c < 0:
            print('Incorrect parameters!')
            exit()
    if d is not None:
        if d < 0:
            print('Incorrect parameters!')
            exit()


def monthly_payment(p, n, i):  # p - principal, n - periods, i - interest
    Overpayment = int()

    i = i / 100 * 1 / 12

    print(f'Your annuity payment = {math.ceil(p * i * (1 + i) ** n / ((1 + i) ** n - 1))}!')
    Overpayment = int(abs(math.ceil(p * i * (1 + i) ** n / ((1 + i) ** n - 1)) * n - p))
    print(f'Overpayment = {Overpayment}')


def loan_principal(p, i, n):  # p - payment, i - interest, n - periods
    i = i / 12 * 1 / 100
    overpayment = int()

    principal = (math.floor(p / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))))
    overpayment = int(abs(principal - (p * n)))
    print(f'Your loan principal = {principal}!')
    print(f'Overpayment = {overpayment}')


def number_of_payments(a, i, p):  # a - principal, i - interest, p - payment
    i = i / 12 * 1 / 100
    monthsRounded = 0
    monthsRounded = math.ceil(math.log((p / (p - i * a)), 1 + i))

    if monthsRounded % 12 == 0:
        years = monthsRounded // 12
        if years == 1:
            print(f'It will take {years} year to repay this loan!')
        if years > 1:
            print(f'It will take {years} years to repay this loan!')
    else:
        months = monthsRounded % 12
        years = monthsRounded // 12
        if years == 1:
            print(f'It will take {years} year and {months} months to repay this loan!')
        if years > 1:
            print(f'It will take {years} years and {months} months to repay this loan!')

    overpayment = int(abs(p * monthsRounded - a))
    print(f'Overpayment = {overpayment}')


def differentiated_payment(a, i, n, m):  # a - principal, i - interest, n - periods, m - payment month
    m = 0
    i = i / 12 * 1 / 100
    monthC = int()
    total = int()
    overpayment = int()

    for m in range(1, n + 1):
        monthC = math.ceil(a / n + i * (a - a * (m - 1) / n))
        print(f'Month {m}: payment is {monthC}')
        total += math.ceil(a / n + i * (a - a * (m - 1) / n))
        overpayment = int(abs(a - total))
    print()
    print(f'Overpayment = {overpayment}')


# Calling parser:
parser = argparse.ArgumentParser()
parser.add_argument('--payment', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--principal', type=float)
parser.add_argument('--interest', type=float)
parser.add_argument('--type', type=str)
args = parser.parse_args()

# Line 120-124 - Checking parameters
typeCheck(args.type)
negativeCheck(args.payment, args.periods, args.principal, args.interest)
noneCheck(args.payment, args.periods, args.principal, args.interest)
typeChoicesCheck(args.type)

# Line 126-150 - Calculator
if args.type == 'diff':
    if args.payment is not None:
        print('Incorrect parameters')
    elif args.interest is None:
        print('Incorrect parameters')
    elif args.periods is None:
        print('Incorrect parameters')
    elif args.principal is None:
        print('Incorrect parameters')
    else:
        differentiated_payment(args.principal, args.interest, args.periods, 0)

elif args.type == 'annuity':
    if args.interest is None:
        print('Incorrect parameters')

    elif args.payment is None:
        monthly_payment(args.principal, args.periods, args.interest)

    elif args.principal is None:
        loan_principal(args.payment, args.interest, args.periods)

    elif args.periods is None:
        number_of_payments(args.principal, args.interest, args.payment)
