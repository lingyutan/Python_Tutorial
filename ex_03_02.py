"""
Rewrite ex_03_01
"""

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print("Error: Please enter numberic input")
    quit()

if hrs <= 40.0:
    pay = hrs * rate
else:
    pay = 40 * rate + (hrs - 40) * rate * 1.5
print("Pay:", pay)
