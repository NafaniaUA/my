def shut_down(s):
     if s=="yes":
        return "Shutting down"
     elif s=="no":
        return "Shutdown aborted"
     else:
        return "Sorry"
s=input(str("Input s "))
print(shut_down(s))