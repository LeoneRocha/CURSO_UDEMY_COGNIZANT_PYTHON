# Tcusto por hora.
cost_per_hour = 0.51
quantity_Server  =int(input("entre com a quantidade de servidor: "))
# custo de  servidor .
cost_per_day =   (24  * cost_per_hour)*quantity_Server
cost_per_month = 30 * cost_per_day
# Compute the costs for twenty serverss
cost_per_day_twenty = 20 * cost_per_day
cost_per_month_twenty = 20 * cost_per_month

# orcamento dolar 918
budget = float(input("entre com o valor alvo: "))
operational_days = (budget / cost_per_day )  
# Display the results.
print('Cost to operate number(s):{1} of server per day is ${0:.2f}.'.format(cost_per_day, quantity_Server))
print('Cost to operate number(s):{1} of server per month is ${0:.2f}.'.format(cost_per_month, quantity_Server))
#print('Cost to operate twenty servers per day is ${:.2f}.'.format(cost_per_day_twenty))
#print('Cost to operate twenty servers per month is ${:.2f}.'.format(cost_per_month_twenty))
print('A number(s):{0} of server(s) can operate on a ${1:.2f} budget for {2:.0f} days.'.format(quantity_Server,budget, operational_days))
