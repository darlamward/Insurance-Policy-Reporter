'''
# program for payment date

import datetime

PolicyDate = datetime.datetime.today()

if PolicyDate.day > 25:
    NextPaymentMonth = PolicyDate.month + 2
    if NextPaymentMonth == 13:
        NextPaymentMonth = 1
        NextPaymentYear = PolicyDate.year + 1
    elif NextPaymentMonth == 14:
        NextPaymentMonth = 2
        NextPaymentYear = PolicyDate.year + 1
    else:
        NextPaymentYear = PolicyDate.year
if PolicyDate.day < 25:
    NextPaymentMonth = PolicyDate.month + 1
    if NextPaymentMonth == 13:
        NextPaymentMonth = 1
        NextPaymentYear = PolicyDate.year + 1
    elif NextPaymentMonth == 14:
        NextPaymentMonth = 2
        NextPaymentYear = PolicyDate.year + 1
    else:
        NextPaymentYear = PolicyDate.year

PaymentDate = PolicyDate.strftime("%m/%d/%Y")
# format 1 digit month with leading zeros.
NextPaymentMonthDsp = "{:02d}".format(NextPaymentMonth)
PaymentDate = PolicyDate.strftime(f"{NextPaymentMonthDsp}/01/{NextPaymentYear}")

print(PaymentDate)


# write on the same line
f = open('Experimental.dat', 'r')
one = int(f.readline())
two = int(f.readline())
three = int(f.readline())
four = int(f.readline())
f.close()

one = one + 1

f = open('Experimental.dat', 'w')
f.write("{},".format(one))
f.write("{},".format(two))
f.write("{},".format(three))
f.write("{}".format(four))
f.close()



# overwriting text
f = open('Experimental.dat', 'r')
one = int(f.readline())
two = int(f.readline())
three = int(f.readline())
four = int(f.readline())
f.close()

one = one + 1

f = open('Experimental.dat', 'w')
f.write("{}\n".format(one))
f.write("{}\n".format(two))
f.write("{}\n".format(three))
f.write("{}\n".format(four))
f.close()

'''

# write on a new line
f = open('Experimental.dat', 'r')
one = int(f.readline())
two = int(f.readline())
three = int(f.readline())
four = int(f.readline())
f.close()

one = one + 1

f = open('ExperimentalTxt.dat', 'a')
f.write("{},".format(one))
f.write("{},".format(two))
f.write("{},".format(three))
f.write("{}\n".format(four))
f.close()