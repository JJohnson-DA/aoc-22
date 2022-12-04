# Load lines of text file
data <- readLines("../data/d2.txt")

# ---- Part 1 Setup----
score_dict <- c(
  "ax" = 4,
  "ay" = 8,
  "az" = 3,
  "bx" = 1,
  "by" = 5,
  "bz" = 9,
  "cx" = 7,
  "cy" = 2,
  "cz" = 6
)

# ---- Part 2 Setup ----
choice_scores <- c("x" = 1, "y" = 2, "z" = 3)
outcome_scores <- c("x" = 0, "y" = 3, "z" = 6)
strategy <- c(
  "a" = c("x" = "z", "y" = "x", "z" = "y"),
  "b" = c("x" = "x", "y" = "y", "z" = "z"),
  "c" = c("x" = "y", "y" = "z", "z" = "x")
)

# object to hold total score
p1_total <- 0
p2_total <- 0
# Iterate over rounds and append corresponding score
for (line in data) {
  trimmed <- tolower(gsub(pattern = " ", replacement = "", line))
  p1_total <- p1_total + score_dict[trimmed]
  choice <- strategy[
    paste0(substr(trimmed, 1, 1), '.', substr(trimmed, 2, 2))
    ]
  temp_score <- {
    choice_scores[choice] + outcome_scores[substr(trimmed, 2, 2)]
  }
  p2_total <- p2_total + temp_score
}
print(paste0('Part 1: ', p1_total, ', Part 2: ', p2_total))
