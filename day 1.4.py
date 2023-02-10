def onedigit(num):
      return((num>=0) and (num<10))
def hemesh(num,dupnum):
      if onedigit(num):
            return(num==(dupnum[0])%10)
      if not hemesh(num//10,dupnum):
            return False
      dupnum[0]=dupnum[0]//10
      return (num%10==(dupnum[0])%10)
def hemu(num):
      if (num<0):
            num=-num
      dupnum=[num]
      return hemesh(num,dupnum)
n=123421
if  hemu(n):
      print('yes')
else:
      print('no')

      
