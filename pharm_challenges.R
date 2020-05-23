# Declare vector with daily drug dosage readings
DINR <- c(1.6, 2.0, 3.2, 1.9, 2.0, 1.9, 2.5, 2.2, 1.8, 2.0, 2.5, 2.2, 1.8, 2.0, 2.5, 2.2)

# challenge 4
found_INR = FALSE
for (val in INR) {
  if ((val > 1.7) & (val < 3.0)) {
    print(val)
    found_INR = TRUE
    break}
  }
if (found_INR == FALSE) {print(-1)}

# challenge 5 (not an elegant solution, its brute force, but I address this issue in more complex case in number 8)
# I could come back and rewrite this but I already solved the core of the generalization problem in challnege 8
found_range = FALSE
for (vals in 3:length(INR)) {
  if ((INR[vals] >= 2.0 & INR[vals-1] >= 2.0) & (INR[vals] <= 3.0 & INR[vals-1] <= 3.0)) {
    print(vals)
    found_range = TRUE
    break}
  else if ((INR[vals] >= 2.0 & INR[vals-2] >= 2.0) & (INR[vals] <= 3.0 & INR[vals-2] <= 3.0)) {
    print(vals)
    found_range = TRUE
    break}
  else if ((INR[vals-1] >= 2.0 & INR[vals-2] >= 2.0) & (INR[vals-1] <= 3.0 & INR[vals-2] <= 3.0)) {
    print(vals)
    found_range = TRUE
    break}
  else if ((INR[vals] >= 2.0 & INR[vals-1] >= 2.0 & INR[vals-2] >= 2.0) & (INR[vals] <= 3.0 & INR[vals-1] <= 3.0 & INR[vals-2] <= 3.0)) {
    print(vals)
    found_range = TRUE
    break}
}
if (found_range == FALSE) {print(-1)}

# challenge 7
found_avg = FALSE
for (days in 14:length(INR)) { 
    
    # sum all elements in the vector INR at index (days-13) up to (days)
    twoweekavg = sum(INR[(days-13):(days)]) / 14
    if (twoweekavg >= 2.0 & twoweekavg <= 3.5) {
      print(days)
      found_avg =TRUE
      break
    }
}
if (found_avg == FALSE) {print(-1)}

# challenge 8 (the boss fight)
DINR2 <- c(2.0, NA, NA, 2.0, NA, NA, NA, NA, 2.0, 2.5, 2.1, 2.2)

found_cons = FALSE
breaker = FALSE

for (x in 5:length(INR2)) {
  for (y in 1:length(INR2)) {
    if (!is.na(INR2[y]) & !is.na(INR2[x])) {
      if ((x-y >= 3) & (x-y < 8)) {
        if ((INR2[x] & INR2[y] >= 2) & (INR2[x] & INR2[y] <= 3.5)) {
          print(x)
          found_cons = TRUE
          breaker=TRUE
          break}
      }
    }
  }
if (breaker == TRUE) {break}}

if (found_cons == FALSE) {print(-1)}
