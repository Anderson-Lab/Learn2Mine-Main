# This will source the provided code and then
args<-commandArgs(TRUE)
inputFile = args[1]
outputFile = args[2]

f = file(outputFile,"w")

tryCatch (
  {source(inputFile)},
  error=function(e) {
          writeLines('Your code is syntactically incorrect<br>',con=f)
          stop('Your code is syntactically incorrect')
        }
)

sum <- function(my.array) {
  writeLines('You are not supposed to call sum<br>',con=f)
  return(0)
}

#1)
solution.my.sum <- function(my.array) {
  total = 0
  for (i in 1:length(my.array)) {
    total = total + my.array[i]
  }
  return(total)
}

v = rnorm(10)
tryCatch({
  if (solution.my.sum(v) == my.sum(v)) {
    writeLines('my.sum is correct<br>',con=f)
  } else {
    writeLines('my.sum is incorrect<br>',con=f)
  }
}, error=function(e){
   writeLines('my.sum is incorrect, you did not supply a my.sum function<br>', con=f)
})


#2)
solution.my.geometric.mean <- function(my.array) {
  total = 1
  for (i in 1:length(my.array)) {
    total = total*my.array[i]
  }
  return(total^(1/length(my.array)))
}

v = abs(rnorm(10))
tryCatch({
  if (solution.my.geometric.mean(v) == my.geometric.mean(v)) {
    writeLines('my.geometric.mean is correct<br>',con=f)
  } else {
    writeLines('my.geometric.mean is incorrect<br>',con=f)
  }
}, error=function(e){
   writeLines('my.geometric.mean is incorrect, you did not supply a my.geometric.mean function<br>', con=f)
})


close(f)
