import matplotlib.pyplot as plt
Countries = ['India','USA','Australia','Japan','UK','France']
Tourists = [574809,4732842,928374,1238439,789244,6987209]
plt.plot(Countries,Tourists,marker="h",mec="#612113",mfc="#93FF00",color="#C20ECB")
plt.ylim(450000,7500000)
plt.xlabel("Countries")
plt.ylabel("Number of Tourists/Year")
plt.show()
