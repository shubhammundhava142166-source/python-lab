class E(Exception):pass
try:
 raise E('error')
except E as e:print(e)