import time
from datetime import date

today = date.today()
seconds = time.time()
print(f"Seconds since January 1, 1970: {seconds:,.4f}"
      f" or {seconds:.2e} in scientific notation$")
actualDate = today.strftime("%b %d %Y")
print(actualDate)
