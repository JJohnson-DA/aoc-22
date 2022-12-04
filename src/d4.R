# Load lines of text file
data <- readLines("../data/d4.txt")

# Counters
p1_total <- 0
p2_total <- 0

for (line in data){
  e1 <- unlist(strsplit(unlist(strsplit(line, ','))[1], '-'))
  e2 <- unlist(strsplit(unlist(strsplit(line, ','))[2], '-'))
  z1 <- seq(e1[1], e1[2])
  z2 <- seq(e2[1], e2[2])
  if (length(intersect(z1, z2)) %in% c(length(z1), length(z2))){
    p1_total <- p1_total + 1
  }
  if (length(intersect(z1, z2)) > 0){
    p2_total <- p2_total + 1
  }
}
print(paste0('Part 1: ', p1_total, ', Part 2: ', p2_total))