import datetime
import calendar

credit_balance = 5000
interest_rate = 0.50 / 12
duration_months = 6
monthly_payment = round(
    credit_balance * interest_rate * pow(
        (1 + interest_rate), duration_months) / (pow(
            (1 + interest_rate), duration_months) - 1), 2)

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_until_start_payment = days_in_current_month - today.day + 1

start_payment_day = today + datetime.timedelta(days=days_until_start_payment)
end_payment_day = start_payment_day

interest = []
principle = []

while credit_balance > 0:
    current_month_interest = credit_balance * interest_rate
    paid_principle = monthly_payment - current_month_interest
    interest.append(current_month_interest)
    principle.append(paid_principle)

    print('Date:{}, Payment={}, Interest={}, Principle={}'.format(
        end_payment_day, monthly_payment, round(current_month_interest, 2),
        round(paid_principle, 2)))

    if credit_balance - monthly_payment > 0.00:
        credit_balance = round(credit_balance - monthly_payment, 2)
    else:
        credit_balance = 0.00

    end_payment_day = end_payment_day + datetime.timedelta(
        days=calendar.monthrange(end_payment_day.year,
                                 end_payment_day.month)[1])
