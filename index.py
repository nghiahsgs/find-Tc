import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import interpolate


#tim Tc_left
def hamFindGiao2Interpolation(x,y1,y2):
    
    # chuan bi data roi rac
    y3=y2-y1

    #ve thu data roi rac
    # plt.plot(x, y1,'x')
    # plt.plot(x, y2,'o')
    # plt.show()
    #noi suy
    #tck1 = interpolate.splrep(x, y1, s=0)
    #tck2 = interpolate.splrep(x, y2, s=0)
    tck3 = interpolate.splrep(x, y3, s=0)

    #ve thu ham sau noi suy
    # x_new=x
    # y1_new=interpolate.splev(x_new, tck1, der=0)
    # y2_new=interpolate.splev(x_new, tck2, der=0)
    # y3_new=interpolate.splev(x_new, tck3, der=0)

    # plt.plot(x, y1,'x',x_new, y1_new,'b')
    # plt.plot(x, y2,'o',x_new, y2_new,'r')
    # plt.plot(x, y3,'o',x_new, y3_new,'-')

    #plt.plot()
    #plt.savefig("xacsuat_b.pdf")
    
    #tim nghiem cua 2 duong
    return interpolate.sproot(tck3)[0] #khi co 1 diem cat



def hamVeDothiCatNhauModiTrucX(data_dir,L,nu,plt):
    #data_dir="/home/nghiahsgs/Desktop/find-Tc/0.2_angle/xacsuat12.dat"
    data=np.genfromtxt(data_dir)

    temp = set(data[:, 0])
    temp =list(temp)
    temp.sort()

    d=[]
    for t in temp: d.append(np.mean(data[abs(data[:, 0] - t) < 1e-5, 1:], 0))
    d=np.array(d)

    #plt.plot(temp,d[:,0],'-')
    #plt.plot(temp,d[:,1],'-')
    #plt.plot(temp,d[:,2],'-')

    #plt.legend(['z','a','q'])
    #plt.show()

    #tim Tc_left
    '''
    temp=np.array(temp)
    x=temp[temp<0.5]
    y1=d[temp<0.5][:,1]
    y2=d[temp<0.5][:,2]
    Tc_left=hamFindGiao2Interpolation(x,y1,y2)
    '''
    temp=np.array(temp)
    x=temp
    y1=d[:,0]
    y2=d[:,2]
    Tc_left=hamFindGiao2Interpolation(x,y1,y2)
    #print(Tc_left)

    #x_new=temp[temp<0.5]
    x_new=temp
    x_new=(x_new-Tc_left)/Tc_left*(L**(1/nu))
    
    #plt.plot(x_new,d[temp<0.5][:,1],'-')
    #plt.plot(x_new,d[temp<0.5][:,2],'-')
    plt.plot(x_new,d[:,0],'-')
    plt.plot(x_new,d[:,2],'-')

    #plt.legend(['z','a','q'])
    #plt.legend([L,L])
    #plt.show()

#ve do thi xac suat phan bo theo nhiet do
args=sys.argv
#data_dir=args[1]
#L=int(args[2]) #12
nu=float(args[1])

f = plt.figure()
#doi truc + lap lai voi tat ca cac L khac nhau
for L in [16,24,32,40,48,56,64]:
    print("L",L)
    data_dir="/home/nghiahsgs/Desktop/find-Tc/1.0_angle/xacsuat%s.dat"%L
    hamVeDothiCatNhauModiTrucX(data_dir,L,nu,plt)
plt.legend([12,12,16,16,24,24,32,32,40,40,48,48,64,64])
#plt.show()
f.savefig('fig%s.pdf'%str(nu))

# L=64
# data_dir="/home/nghiahsgs/Desktop/find-Tc/0.2_angle/xacsuat%s.dat"%L
# hamVeDothiCatNhauModiTrucX(data_dir,L,nu,plt)
# plt.show()
