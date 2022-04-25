from math import pow
from math import log
from math import ceil
from math import floor
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=float)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=float)

args = parser.parse_args()

type_calc = args.type
interest = args.interest
periods = args.periods
principal = args.principal
annuity = args.payment
diff = args.payment


if type_calc == "annuity" and None not in (periods, annuity, interest):
    loan_interest = float(interest) / (12 * 100)
    a = loan_interest * pow(1 + loan_interest, periods)
    b = pow(1 + loan_interest, periods) - 1
    principal = floor(annuity / (a / b))
    overpayment = ceil(periods * annuity - principal)
    print(f"Your loan principal = {principal}!\nOverpayment = {overpayment}")
elif type_calc == "annuity" and None not in (principal, annuity, interest):
    loan_interest = float(interest) / (12 * 100)
    n = ceil(log((annuity / (annuity - loan_interest * principal)), 1 + loan_interest))
    overpayment = ceil(n * annuity - principal)
    if n > 11:
        years = n // 12
        months = n % 12
        if months % 12 == 0:
            print(f"It will take {years} years to repay this loan!")
            print(f"Overpayment = {overpayment}")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
            print(f"Overpayment = {overpayment}")
    else:
        print(f"It will take {n} months to repay this loan!")
        print(f"Overpayment = {overpayment}")
elif type_calc == "annuity" and None not in (periods, principal, interest):
    loan_interest = interest / (12 * 100)
    a = loan_interest * pow(1 + loan_interest, periods)
    b = pow(1 + loan_interest, periods) - 1
    monthly_payment = ceil(principal * a / b)
    overpayment = ceil((monthly_payment * periods) - principal)
    print(f"Your annuity payment = {monthly_payment}!\nOverpayment = {overpayment}")

elif type_calc == "diff" and None not in (principal, periods, interest):
    list_payment = []
    for m in range(1, int(periods) + 1):
        i = interest / (12 * 100)
        d = ceil(principal / periods + i * (principal - (principal * (m - 1)) / periods))
        list_payment.append(d)
        print(f"Month {m}: payment is {d}")
    sum_diff = sum(list_payment)
    overpayment = sum_diff - principal
    print()
    print(f"Overpayment = {overpayment}")
else:
    print("Incorrect parameters.")
