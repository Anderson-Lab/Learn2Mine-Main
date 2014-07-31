# This will source the provided code and then
args<-commandArgs(TRUE)
inputFile = args[1]
outputFile = args[2]

f = file(outputFile,"w")

tryCatch (
  {source(inputFile)},
  error=function(e) {
          writeLines('Your code is syntactically incorrect<br>',con=f)
          writeLines(as.character(e))
          stop('Your code is syntactically incorrect')
        }
)

#sum <- function(my.array) {
#  writeLines('You are not supposed to call sum<br>',con=f)
#  return(0)
#}

solution.sens <- function(pred.labels,correct.labels,tp.label) {
  # First change all things that are no tp.label to 'not tp.label'
  num.tp = sum(pred.labels == correct.labels & correct.labels == tp.label)
  num.fn = sum(pred.labels != correct.labels & correct.labels == tp.label)

  return(num.tp/(num.tp + num.fn))
}

solution.spec <- function(pred.labels,correct.labels,tp.label) {
  num.tn = sum(pred.labels == correct.labels & correct.labels != tp.label)
  num.fp = sum(pred.labels != correct.labels & correct.labels != tp.label)

  return(num.tn/(num.tn + num.fp))
}

solution.accuracy <- function(pred.labels,correct.labels) {
  num.correct = sum(pred.labels == correct.labels)

  return(num.correct/length(correct.labels))
}

#1)
correct.labels = c(rep("apple",10),rep("pear",8),rep("orange",15))
pred.labels = sample(correct.labels,length(correct.labels))
tp.label = "apple"

tryCatch({
  if (solution.sens(pred.labels,correct.labels,tp.label) == sens(pred.labels,correct.labels,tp.label)) {
    writeLines('sens is correct<br>',con=f)
  } else {
    writeLines('sens is incorrect<br>',con=f)
  }
}, error=function(e){
   writeLines('sens is incorrect, you did not supply a sens function<br>', con=f)
   writeLines(as.character(e))
})


#2)
tryCatch({
  if (solution.spec(pred.labels,correct.labels,tp.label) == spec(pred.labels,correct.labels,tp.label)) {
    writeLines('spec is correct<br>',con=f)
  } else {
    writeLines('spec is incorrect<br>',con=f)
  }
}, error=function(e){
   writeLines('spec is incorrect, you did not supply a spec function<br>', con=f)
   writeLines(as.character(e))
})

#3)
tryCatch({
  if (solution.accuracy(pred.labels,correct.labels) == accuracy(pred.labels,correct.labels)) {
    writeLines('accuracy is correct<br>',con=f)
  } else {
    writeLines('accuracy is incorrect<br>',con=f)
  }
}, error=function(e){
   writeLines('accuracy is incorrect, you did not supply an accuracy function<br>', con=f)
   writeLines(as.character(e))
})

close(f)
