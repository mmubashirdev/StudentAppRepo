class NegativeMarkError(Exception):
  pass
class AboveRangeError(Exception):
  pass

try:
  studentMarks = int(input("Enter your marks:"))
  if studentMarks < 0:
    raise NegativeMarkError("Marks cannot be negative")
  if studentMarks > 100:
    raise AboveRangeError("Marks cannot be greater than 100")
  else:
    print("Marks Accepted")
    
except ValueError:
  print("Enter number not string")
except NegativeMarkError as err:
  print(err)
except AboveRangeError as err:
  print(err)
finally:
  print("Program finished")