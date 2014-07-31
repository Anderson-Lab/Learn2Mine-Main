library(quantmod)

# Add set digits and set width
options(digits = 3,width=100)

f = file('PredictingStockMarket1.txt')
sink(f)

# Download the IBM stock performance using the following code
setSymbolLookup(IBM=list(name='IBM',src='yahoo'),
                USDEUR=list(name='USD/EUR',src='oanda',
                            from=as.Date('2013-01-01')))
getSymbols(c('IBM','USDEUR'))

# 1)
# Subset the data, so that only Jan 1, 2010 to Jan, 1, 2013 is in the dataset.
# Then run head(IBM)
IBM = IBM["2010-01-01/2013-01-01"]
writeLines("1)")
print(head(IBM))

# 2)
# change headers to match the headers from GSPC
colnames(IBM)=c("Open","High","Low","Close","Volume","Adjusted")
writeLines("2)")
print(head(IBM))

#3)

# using the features in the book, create a randomForest model, and tell me which
T.ind <- function(quotes,tgt.margin=0.025,n.days=10) {
  v <- apply(HLC(quotes),1,mean)
  
  r <- matrix(NA,ncol=n.days,nrow=NROW(quotes))
  ## The following statment is wrong in the book (page 109)!
  for(x in 1:n.days) 
    r[,x] <- Next(Delt(Cl(quotes),v,k=x),x)
  
  x <- apply(r,1,function(x) sum(x[x > tgt.margin | x < -tgt.margin]))
  if (is.xts(quotes)) xts(x,time(quotes)) else x
}

myATR <- function(x) ATR(HLC(x))[,'atr']
mySMI <- function(x) SMI(HLC(x))[,'SMI']
myADX <- function(x) ADX(HLC(x))[,'ADX']
myAroon <- function(x) aroon(x[,c('High','Low')])$oscillator
myBB <- function(x) BBands(HLC(x))[,'pctB']
myChaikinVol <- function(x) Delt(chaikinVolatility(x[,c("High","Low")]))[,1]
myCLV <- function(x) EMA(CLV(HLC(x)))[,1]
myEMV <- function(x) EMV(x[,c('High','Low')],x[,'Volume'])[,2]
myMACD <- function(x) MACD(Cl(x))[,2]
myMFI <- function(x) MFI(x[,c("High","Low","Close")], x[,"Volume"])
mySAR <- function(x) SAR(x[,c('High','Close')]) [,1]
myVolat <- function(x) volatility(OHLC(x),calc="garman")[,1]


library(randomForest)
data.model <- specifyModel(T.ind(IBM) ~ Delt(Cl(IBM),k=1:10) + 
                             myATR(IBM) + mySMI(IBM) + myADX(IBM) + myAroon(IBM) + 
                             myBB(IBM)  + myChaikinVol(IBM) + myCLV(IBM) + 
                             CMO(Cl(IBM)) + EMA(Delt(Cl(IBM))) + myEMV(IBM) + 
                             myVolat(IBM)  + myMACD(IBM) + myMFI(IBM) + RSI(Cl(IBM)) +
                             mySAR(IBM) + runMean(Cl(IBM)) + runSD(Cl(IBM)))
set.seed(1234)
rf <- buildModel(data.model,method='randomForest',
                 training.per=c(start(IBM),index(IBM["2012-01-04"])),
                 ntree=50, importance=T)

imp <- importance(rf@fitted.model,type=1)
writeLines("3)")
print(rownames(imp)[which(imp > 5)])

close(f)
