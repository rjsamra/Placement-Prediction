#extragraph
def ex_graph(x, y, z, b, x1, y1):
      xp=[]
      yp=[]
      xq=[]
      yq=[]
      for i in range(len(x)):
        if z[i]=='NO':
          xp.append(x[i])
          yp.append(y[i])
        elif z[i]=='YES':
          xq.append(x[i])
          yq.append(y[i])

      fig = plt.figure()

      ax = fig.add_subplot(111)    
      ax.scatter(xq, yq, s=30, marker='>', label='Placed')
      ax.scatter(xp, yp, s=30, marker='<', label='Not placed')
      plt.plot(x1, y1, color = "k", marker = "v", markersize= 10)
      plt.legend()
      plt.show()
