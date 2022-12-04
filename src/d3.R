# Load lines of text file
data <- readLines("../data/d3.txt")

# Create look up vector for letter priorities
all_letters <- c(letters, LETTERS)

# Counters
p1_total <- 0
p2_total <- 0

# ---- Part 1 ----
for (line in data){
  # Split off first compartment
  c1 <- unlist(strsplit(substr(line, 1, (nchar(line)/2)), ''))
  # Split off second compartment
  c2 <- unlist(strsplit(substr(line, (nchar(line)/2)+1, nchar(line)), ''))
  # Find intersection of lists and add score to counter
  p1_total <- p1_total + which(all_letters == intersect(c1, c2))
}

# ---- Part 2 ----
lb <- 1
ub <- 3
for (i in seq(1, length(data)/3)){
  group <- data[lb:ub]
  e1 <- unlist(strsplit(group[1], ''))
  e2 <- unlist(strsplit(group[2], ''))
  e3 <- unlist(strsplit(group[3], ''))
  p2_total <- p2_total + which(all_letters == intersect(e1, intersect(e2, e3)))
  lb <- lb + 3
  ub <- ub + 3
}
print(paste0('Part 1: ', p1_total, ', Part 2: ', p2_total))