def merge_sort(ar,br):
    i=0
    j=0
    cr=[]
    while i<len(ar) and j<len(br):
        if ar[i]<=br[j]:
            cr.append(ar[i])
            i+=1
        else:
            cr.append(br[j])
            j+=1
    if i<len(ar):
        cr.extend(ar[i:])
    if j<len(br):
        cr.extend(br[j:])
    return cr
def merge_parts(pr,width):
    res=[]
    for i in range(0,len(pr),width*2):
        xr=merge_sort(pr[i:(i+width)],pr[(i+width):(i+(2*width))])
        res.extend(xr)
    return res
array=[28,44,17,35,67,57,49,66,33,14]
width=1
while width<len(array):
    array=merge_parts(array,width)
    width*=2
print(array)
        
        
