# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_amount_per_month = 1000
extra_amount_start_month = 61
extra_amount_end_month = 108
current_month = 0

while principal > 0:
	amount_paid_per_month = 0
	total_amount_due = principal * (1+rate/12)
	if((current_month >= extra_amount_start_month) & (current_month<= extra_amount_end_month)):
		amount_paid_per_month = (payment + extra_amount_per_month)
		if (amount_paid_per_month < total_amount_due):
			principal = principal * (1+rate/12) - amount_paid_per_month
			total_paid = total_paid + amount_paid_per_month
		else:
			principal = principal * (1+rate/12) - total_amount_due
			total_paid = total_paid + total_amount_due
			amount_paid_per_month = total_amount_due
	else:
		amount_paid_per_month = payment
		if (amount_paid_per_month < total_amount_due):
			principal = principal * (1+rate/12) - amount_paid_per_month
			total_paid = total_paid + amount_paid_per_month
		else:
			principal = principal * (1+rate/12) - total_amount_due
			total_paid = total_paid + total_amount_due
			amount_paid_per_month = total_amount_due
	current_month += 1
	print(f'{current_month} Month(s) {amount_paid_per_month: 0.2f} Installment {total_paid: 0.2f} Paid {principal: 0.2f} Due')
	# print("Month:\t", current_month, sep="\t")
	# print("Installment:", amount_paid_per_month, sep="\t")
	# print("Paid:\t", total_paid, sep="\t")
	# print("Due:\t", principal, sep="\t")
	# print("---")
print("End of Statement")