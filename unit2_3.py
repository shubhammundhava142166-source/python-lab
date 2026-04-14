try:
 a=int(input());b=int(input());print(a/b)
except ZeroDivisionError as e:print(e)