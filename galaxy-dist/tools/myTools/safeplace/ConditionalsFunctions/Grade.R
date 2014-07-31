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

min <- function(my.array) {
  writeLines('You are not supposed to call min<br>',con=f)
  return(0)
}

#1)
solution.minimum3 <- function(v1,v2,v3) {
  smallest = v1
  if (v2 < smallest)
    smallest = v2
  if (v3 < smallest)
    smallest = v3
  return(smallest)
}

tryCatch({
  if (solution.minimum3(1,3.5,-8.6) == minimum3(1,3.5,-8.6)) {
    writeLines('minimum3 is correct<br>',con=f)
  } else {
    writeLines('minimum3 is incorrect<br>',con=f)
  }
}, error=function(e){
   writeLines('minimum3 is incorrect, you did not supply a minimum3 function<br>', con=f)
})

#2)
solution.minimum <- function(my.array) {
  smallest = my.array[1]
  for (i in 2:length(my.array)) {
    if (my.array[i] < smallest)
      smallest = my.array[i]
  }
  return(smallest)
}

v = rnorm(10)
tryCatch({
  if (solution.minimum(v) == minimum(v)) {
    writeLines('minimum is correct<br>',con=f)
  } else {
    writeLines('minimum is incorrect<br>',con=f)
  }
}, error=function(e){
   writeLines('minimum is incorrect, you did not supply a minimum function<br>', con=f)
})


close(f)
