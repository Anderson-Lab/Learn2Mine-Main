#!/usr/bin/ruby
rundir = "/usr/local/Learn2Mine-Main/rps"
mntdir = "/rps"
bots = `cd #{rundir}/bots && ls *.py`.split("\n")
bots = bots.collect{|bot| mntdir+"/bots/"+bot}.join(",")
results = `docker run -a stdout -v #{rundir}:#{mntdir} -i learn2mine python #{mntdir}/rpsrunner.py #{bots} | grep matches | grep won`
results = results.split("\n")
results = results.collect{|result| 
  name = result.split(":")[0].split("/")[-1].sub(".py","")
  score = result.split(":")[1].split("%")[0].split(" ")[-1].to_f()
  [name,score]
}
results = results.sort_by{|value| -value[1]}
print "<html><body><table>"
results.each_with_index{|r,i| 
  print "<tr><td>#{i+1}.</td><td>#{r[0]}</td><td>#{r[1]}</td></tr>"
}
print "</table></body></html>"
