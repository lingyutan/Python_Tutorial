# import re
#
# handle = open("regex_sum_1459665.txt")
# numbers = re.findall('[0-9]+', handle.read())
#
# total = 0
#
# for number in numbers:
#     number = int(number)
#     total += number
# print(total)


# import re
#
# numbers = re.findall('[0-9]+', open("regex_sum_1459665.txt").read())
#
# print(numbers)

### Simplified Version
import re

print( sum( [ int(n) for n in re.findall('[0-9]+', open("regex_sum_1459665.txt").read()) ] ) )
