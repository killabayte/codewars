def nb_year(p0, percent, aug, p):
  years_counter = 0
  
  while True:
      if p0 >= p:
          return years_counter
      else:
          print(p0)
          p0 = int(p0 + (p0 * (float(percent) / 100)) + aug)
          years_counter += 1
