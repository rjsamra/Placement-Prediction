#knn algorithm
for i in range(len(x)):
    eform(x[i],y[i],x1,y1)

for i in range(len(x)):
    for j in range(len(x)-i-1):
      if x is x1:
        pass
      else:
        if d[j]>d[j+1]:
          t1=d[j]
          d[j]=d[j+1]
          d[j+1]=t1
          
          t2=x[j]
          x[j]=x[j+1]
          x[j+1]=t2

          t3=y[j]
          y[j]=y[j+1]
          y[j+1]=t3

# print(d)
print(d[0],d[1],d[2])

print()

print("The required three points are:")
print(x[0],',',y[0])
print(x[1],',',y[1])
print(x[2],',',y[2])
