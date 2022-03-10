'''
Write a function, which takes a non-negative integer (seconds) as
input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
'''

def make_readable(seconds):
    c=0
    if seconds>359999:
        return("Time exceeds 100 hours")
    else:
        for i in range(100):
            for j in range(60):
                for k in range(60):
                    if c==seconds+1:
                        break
                    t=("%d:%d:%d"%(i,j,k))
                    c+=1  
        t1=t.split(':')
        if len(t1[0])==1:
            t1[0]='0'+t1[0]
        if len(t1[1])==1:
            t1[1]='0'+t1[1]
        if len(t1[2])==1:
            t1[2]='0'+t1[2]
        t2=':'.join(t1)
        return(t2)
print(make_readable(int(input("Enter seconds: "))))
