import datetime
import calendar
from matplotlib import pyplot as plt

credit_balance = 10000
interest_rate = 0.30 / 12
monthly_principle = 1200

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_until_start_day = days_in_current_month - today.day + 1

start_day = today + datetime.timedelta(days=days_until_start_day)
end_day = start_day

current_month_interest = round(
    credit_balance * interest_rate * (days_in_current_month - today.day) /
    days_in_current_month, 2)

months = 0
installment = []
interest = []

while credit_balance > 0.00:
    months += 1
    if credit_balance >= monthly_principle:
        credit_balance -= monthly_principle
        credit_balance = 0.00 if credit_balance < 0.00 else round(
            credit_balance, 2)

        monthly_installment = monthly_principle + current_month_interest
        installment.append(round(monthly_installment, 2))
        interest.append(round(current_month_interest, 2))

        print('{} {:8} {:8}'.format(end_day, credit_balance,
                                    monthly_installment))

        days_in_current_month = calendar.monthrange(end_day.year,
                                                    end_day.month)[1]
        end_day += datetime.timedelta(days=days_in_current_month)
        current_month_interest = credit_balance * interest_rate
    else:
        monthly_installment = credit_balance + current_month_interest
        installment.append(round(monthly_installment, 2))
        interest.append(round(current_month_interest, 2))

        credit_balance = 0.00
        print('{} {:8} {:8}'.format(end_day, credit_balance,
                                    monthly_installment))
'''-----------------------------------------------------'''
plt.style.use('fivethirtyeight')
x_values = [index for index in range(1, 10)]
y_principle = [monthly_principle for _ in range(1, 10)]

print(x_values)
print(installment)
print(interest)

labels = ['equal_principle', 'interest']
colors = ['blue', 'red']

plt.stackplot(x_values, y_principle, interest, colors=colors, labels=labels)
plt.legend(loc='lower right')
plt.title('Installment Of Equal Principle')
plt.xlabel('Time')
plt.ylabel('USD')
plt.tight_layout()
plt.show()
