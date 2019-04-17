grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# Display all grades to the screen in one line
def print_grades(grades_input):
  for grade in grades_input:
    print grade,

# Add all scores together
def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total

# Average of all grades    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

# Variance of the grades
def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  return variance / float(len(scores)) 

# Standard Deviation of all grades
def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

# Outputs
print "**********************************************"
print "* Grades:", print_grades(grades)
print "* Total sum:", grades_sum(grades)
print "* Average of all grades:", grades_average(grades)
print "* Variance:", grades_variance(grades)
print "* Standard Deviation:", grades_std_deviation(variance)
print "**********************************************"

