class NegativeValue(Exception):
  pass
class OutOfRange(Exception):
  pass

def calculate_grade(studentMarks):
  
  if not isinstance(studentMarks,(int,float)):
    raise ValueError("Enter number not words")
  if studentMarks < 0:
    raise NegativeValue("Marks cannot be less than 0")
  if studentMarks > 100:
    raise OutOfRange("Marks cannot be greater than 100")
  
  
  if 90<= studentMarks <= 100:
    return "A grade"
  elif 80<= studentMarks <= 89:
    return "B grade"
  elif 70<= studentMarks <= 79:
    return "C grade"
  elif 60<= studentMarks <= 69:
    return "D grade"
  else:
    return "F grade"
  
if __name__ == "__main__":  
  try:
    StudentMarks = int(input("Enter your marks: "))
    print(calculate_grade(StudentMarks))
  except (ValueError,NegativeValue,OutOfRange) as err:
    print(err)

  