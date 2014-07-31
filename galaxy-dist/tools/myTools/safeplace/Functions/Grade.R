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

mean <- function(my.array) {
  writeLines('You are not supposed to call mean<br>',con=f)
  return(0)
}

#1)
solution.average3 <- function(v1,v2,v3) {
  return((v1+v2+v3)/3)
}

tryCatch (
{if (solution.average3(1,3.5,-8.6) == average3(1,3.5,-8.6)) {
  writeLines('average3 is correct<br>',con=f)
} else {
  writeLines('average3 is incorrect<br>',con=f)
}}, error=function(e) {
	writeLines('average3 is incorrect, you did not supply an average3 function<br>', con=f)
  }
)

#2)
solution.quadratic <- function(a,b,c) {
  root1 = (-b + sqrt(b^2-4*a*c))/(2*a)
  root2 = (-b - sqrt(b^2-4*a*c))/(2*a)
  return (c(root1,root2))
}

tryCatch({
  if (all(solution.quadratic(1,3.5,-8.6) %in% quadratic(1,3.5,-8.6))) {
    writeLines('quadratic is correct<br>',con=f)
  } else {
    writeLines('quadratic is incorrect<br>',con=f)
}}, error=function(e) {
         writeLines('quadratic is incorrect, you did not supply an quadratic function<br>', con=f)
      }
)


#3)
solution.area <- function(height,width) {
  return(height*width/2)
}

tryCatch({
  if (solution.area(1,3.5) == area(1,3.5)) {
    writeLines('area is correct<br>',con=f)
  } else {
    writeLines('area is incorrect<br>',con=f)
  }
}, error=function(e){
    writeLines('area is incorrect, you did not supply an area function<br>', con=f)
  }
)

close(f)
