import random

# return a dictionary containing grade distribution for a course-specific
def distributeGrades():

  dist = {'P': 0, 'F': 0, 'D': 0, 'C-': 0, 'C': 0, 'C+': 0, 'B-': 0, 'B': 0, 'B+': 0, 'A-': 0, 'A': 0, 'A+': 0}
  # probability 1/3 professor is easy, 1/3 professor is avg, 1/3 professor is harsh
  difficulty = random.randint(0, 2)
  for i in range(0, 100):
    # Pass/D/Fail with probability 0.1 < p < 0.2
    p = random.uniform(0.1, 0.2)
    x = random.random()
    if x < p:
      dist['P'] +=1
    # otherwise, take for a grade
    else:
      # Average difficulty
      if difficulty == 0:
        z = random.normalvariate(0, 1)
        if z < -2.5:
          dist['F'] += 1
        elif z < -2:
          dist['D'] += 1
        elif z < -1.5:
          dist['C-'] += 1
        elif z < -1:
          dist['C'] += 1
        elif z < -0.5:
          dist['C+'] += 1
        elif z < 0:
          dist['B-'] += 1
        elif z < 0.5:
          dist['B'] += 1
        elif z < 1:
          dist['B+'] += 1
        elif z < 1.5:
          dist['A-'] += 1
        elif z < 2:
          dist['A'] += 1
        else:
          dist['A+'] += 1
      # Easy difficulty
      elif difficulty == 1:
        z = 0 - random.expovariate(0.4)
        if z < -10:
          dist['F'] += 1
        elif z < -9:
          dist['D'] += 1
        elif z < -8:
          dist['C-'] += 1
        elif z < -7:
          dist['C'] += 1
        elif z < -6:
          dist['C+'] += 1
        elif z < -5:
          dist['B-'] += 1
        elif z < -4:
          dist['B'] += 1
        elif z < -3:
          dist['B+'] += 1
        elif z < -2:
          dist['A-'] += 1
        elif z < -1:
          dist['A'] += 1
        else:
          dist['A+'] += 1
      # Hard difficulty
      elif difficulty == 2:
        z = random.expovariate(0.4)
        if z > 10:
          dist['A+'] += 1
        elif z > 9:
          dist['A'] += 1
        elif z > 8:
          dist['A-'] += 1
        elif z > 7:
          dist['B+'] += 1
        elif z > 6:
          dist['B'] += 1
        elif z > 5:
          dist['B-'] += 1
        elif z > 4:
          dist['C+'] += 1
        elif z > 3:
          dist['C'] += 1
        elif z > 2:
          dist['C-'] += 1
        elif z > 1:
          dist['D'] += 1
        else:
          dist['F'] += 1

  return dist

def main():
  dist = distributeGrades()
  print dist

main()