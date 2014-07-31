library(DMwR)
library(quantmod)

f = file('simulatedTraderResults.txt')
sink(f)

source('parameters.txt')

T.ind <- function(quotes,tgt.margin=0.025,n.days=10) {
  v <- apply(HLC(quotes),1,mean)
  
  r <- matrix(NA,ncol=n.days,nrow=NROW(quotes))
  ## The following statment is wrong in the book (page 109)!
  for(x in 1:n.days) r[,x] <- Next(Delt(Cl(quotes),v,k=x),x)
  
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

data.model <- specifyModel(T.ind(GSPC) ~ Delt(Cl(GSPC),k=1) + myATR(GSPC) 
                           + myADX(GSPC) +    myEMV(GSPC) + myVolat(GSPC)  + myMACD(GSPC) 
                           + mySAR(GSPC) + runMean(Cl(GSPC)) )


Tdata.train <- as.data.frame(modelData(data.model,
                                       data.window=c('1970-01-02','1999-12-31')))
Tform <- as.formula('T.ind.GSPC ~ .')

# Train and test periods
start <- 1
len.tr <- 1000
len.ts <- 500
tr <- start:(start+len.tr-1)
ts <- (start+len.tr):(start+len.tr+len.ts-1)

# getting the quotes for the testing period
data(GSPC)
date <- rownames(Tdata.train[start+len.tr,])
market <- GSPC[paste(date,'/',sep='')][1:len.ts]

# learning the model and obtaining its signal predictions
library(e1071)
s <- svm(Tform,Tdata.train[tr,],cost=10,gamma=0.01)
p <- predict(s,Tdata.train[ts,])
sig <- trading.signals(p,0.1,-0.1)

# The above code is what to give the students (approximately). Below is what they have to write.

policy.1 <- function(signals,market,opened.pos,money,
                     bet=0.2,hold.time=10,
                     exp.prof=0.025, max.loss= 0.05
                     )
  {
    d <- NROW(market) # this is the ID of today
    orders <- NULL
    nOs <- NROW(opened.pos)
    # nothing to do!
    if (!nOs && signals[d] == 'h') return(orders)

    # First lets check if we can open new positions
    # i) long positions
    if (signals[d] == 'b' && !nOs) {
      quant <- round(bet*money/market[d,'Close'],0)
      if (quant > 0) 
        orders <- rbind(orders,
              data.frame(order=c(1,-1,-1),order.type=c(1,2,3), 
                         val = c(quant,
                                 market[d,'Close']*(1+exp.prof),
                                 market[d,'Close']*(1-max.loss)
                                ),
                         action = c('open','close','close'),
                         posID = c(NA,NA,NA)
                        )
                       )

    # ii) short positions  
    } else if (signals[d] == 's' && !nOs) {
      # this is the nr of stocks we already need to buy 
      # because of currently opened short positions
      need2buy <- sum(opened.pos[opened.pos[,'pos.type']==-1,
                                 "N.stocks"])*market[d,'Close']
      quant <- round(bet*(money-need2buy)/market[d,'Close'],0)
      if (quant > 0)
        orders <- rbind(orders,
              data.frame(order=c(-1,1,1),order.type=c(1,2,3), 
                         val = c(quant,
                                 market[d,'Close']*(1-exp.prof),
                                 market[d,'Close']*(1+max.loss)
                                ),
                         action = c('open','close','close'),
                         posID = c(NA,NA,NA)
                        )
                       )
    }
    
    # Now lets check if we need to close positions
    # because their holding time is over
    if (nOs) 
      for(i in 1:nOs) {
        if (d - opened.pos[i,'Odate'] >= hold.time)
          orders <- rbind(orders,
                data.frame(order=-opened.pos[i,'pos.type'],
                           order.type=1,
                           val = NA,
                           action = 'close',
                           posID = rownames(opened.pos)[i]
                          )
                         )
      }

    orders
  }



policy.2 <- function(signals,market,opened.pos,money,
                     bet=0.2,exp.prof=0.025, max.loss= 0.05
                    )
  {
    d <- NROW(market) # this is the ID of today
    orders <- NULL
    nOs <- NROW(opened.pos)
    # nothing to do!
    if (!nOs && signals[d] == 'h') return(orders)

    # First lets check if we can open new positions
    # i) long positions
    if (signals[d] == 'b') {
      quant <- round(bet*money/market[d,'Close'],0)
      if (quant > 0) 
        orders <- rbind(orders,
              data.frame(order=c(1,-1,-1),order.type=c(1,2,3), 
                         val = c(quant,
                                 market[d,'Close']*(1+exp.prof),
                                 market[d,'Close']*(1-max.loss)
                                ),
                         action = c('open','close','close'),
                         posID = c(NA,NA,NA)
                        )
                       )

    # ii) short positions  
    } else if (signals[d] == 's') {
      # this is the money already committed to buy stocks
      # because of currently opened short positions
      need2buy <- sum(opened.pos[opened.pos[,'pos.type']==-1,
                                 "N.stocks"])*market[d,'Close']
      quant <- round(bet*(money-need2buy)/market[d,'Close'],0)
      if (quant > 0)
        orders <- rbind(orders,
              data.frame(order=c(-1,1,1),order.type=c(1,2,3), 
                         val = c(quant,
                                 market[d,'Close']*(1-exp.prof),
                                 market[d,'Close']*(1+max.loss)
                                ),
                         action = c('open','close','close'),
                         posID = c(NA,NA,NA)
                        )
                       )
    }

    orders
  }


# now using the simulated trader
t1 <- trading.simulator(market,sig,
             'policy.1',list(exp.prof=profit.margin.positions,bet=frac.money.invest,max.loss=max.loss.admit))
evaluation1 = tradingEvaluation(t1)
ret1 = evaluation1[["Ret"]]

t2 <- trading.simulator(market,sig,'policy.2',list(exp.prof=profit.margin.positions,bet=frac.money.invest))
evaluation2 = tradingEvaluation(t2)
ret2 = evaluation2[["Ret"]]

writeLines(c('1)'))
writeLines(paste('Percent return of policy.1 is',ret1))
writeLines(c('2)'))
writeLines(paste('Percent return of policy.2 is',ret2))

close(f)