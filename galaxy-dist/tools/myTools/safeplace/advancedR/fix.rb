dirs = `ls`
dirs.each{|dir|
  system("cd #{dir}")
  system("python fix.py")
  system("cd ..")
}
