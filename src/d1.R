# Load lines of text file
data <- readLines("../data/d1.txt")
# Set vector to store totals, and intermediate counter object
totals <- c()
current <- 0
# Iterate over lines in file
for (line in data){
  # check if we reached the end of one group of lines
  if (line != ''){
    # add value to current if value is not empty
    current <- current + as.numeric(line)
  } else {
    # Add current value to totals vector
    totals <- append(totals, current)
    # Reset current counter
    current <- 0
  }
}
# Sort list descending
totals <- sort(totals, decreasing = TRUE)
# Print off answers to questions
print(paste0('Part 1: ', totals[1], ', Part 2:', sum(totals[1:3])))