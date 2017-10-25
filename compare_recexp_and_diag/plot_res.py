import matplotlib
import matplotlib.pyplot as plt
import numpy as np

THREADS = [20, 16, 10, 8, 4, 2, 1]


N1 = np.array([100, 1000, 5000, 10000, 15000, 20000, 25000, 30000])
N2 = np.array([100, 1000, 5000, 10000, 15000, 20000, 25000, 30000])
N3 = np.array([100, 1000, 5000, 10000, 15000, 20000])
N4 = np.array([100, 1000, 5000, 10000, 15000, 20000])
N5 = np.array([100, 1000, 5000, 10000, 15000, 20000])
N6 = np.array([100, 1000, 5000, 10000, 15000, 20000])
N7 = np.array([100, 1000, 5000, 10000, 15000, 20000]) # 15000 missing results


Tdiag1 = np.array([0.0188479423523, 0.356379032135,19.4848539829,113.130937099,359.47751689,800.875842094, 1518.46860099, 2592.353899])
Tdiag2 = np.array([0.00961995124817,0.349864006042,17.0613050461,124.045060873,360.266511917,814.154867887, 1527.82458305, 2610.37607193])
Tdiag3 = np.array([0.00727200508118,0.390928983688,17.0855660439,118.816667795,376.383109093,864.058187962])
Tdiag4 = np.array([0.00897288322449,0.323593854904,12.6111221313,84.3528590202,267.745352983,589.306200981])
Tdiag5 = np.array([0.00906586647034,0.393745183945,15.6505720615,119.744168043,374.395128965, 851.253773928])
Tdiag6 = np.array([0.0110139846802,0.479855060577,23.5666759014,183.546396017,615.514752865, 1387.71345496])
Tdiag7 = np.array([0.00998497009277,0.581919908524,39.5270929337,309.263792038, -1, 2545.10688305])


index = 5
Tdiag_th = []
Tdiag_th.append(Tdiag1[index])
Tdiag_th.append(Tdiag2[index])
Tdiag_th.append(Tdiag3[index])
Tdiag_th.append(Tdiag4[index])
Tdiag_th.append(Tdiag5[index])
Tdiag_th.append(Tdiag6[index])
Tdiag_th.append(Tdiag7[index])
Tdiag_th = Tdiag_th[::-1]
print(Tdiag_th)



Trecexp1 = np.array([0.00690007209778,0.234297990799,19.7610099316,109.937275887,337.808438063,740.753391027, 1406.92849207, 2367.13096714])
Trecexp2 = np.array([0.0077211856842,0.268532991409,20.223954916,125.253087044,396.855451107,889.922856808, 1705.32206202, 2878.85547686])
Trecexp3 = np.array([0.00575113296509,0.309669971466,25.981139183,170.785896063,543.941596985,1222.2428968])
Trecexp4 = np.array([0.00772309303284,0.364115953445,30.4156019688,200.828611851,634.645853043,1465.40962005])
Trecexp5 = np.array([0.007493019104,0.509330034256,45.0090708733,337.196034908,1100.20056581,  2551.07903409])
Trecexp6 = np.array([0.00880599021912,0.793797016144,85.6862039566,628.422485113,2082.95721507, 4881.04941106])
Trecexp7 = np.array([0.00839495658875,1.26920604706,149.727632046,1174.69930506, -1, 9512.92980194])


index = 5
Trecexp_th = []
Trecexp_th.append(Trecexp1[index])
Trecexp_th.append(Trecexp2[index])
Trecexp_th.append(Trecexp3[index])
Trecexp_th.append(Trecexp4[index])
Trecexp_th.append(Trecexp5[index])
Trecexp_th.append(Trecexp6[index])
Trecexp_th.append(Trecexp7[index])
Trecexp_th = Trecexp_th[::-1]
print(Trecexp_th)



font = {'family': 'serif',
        'weight': 'normal',
        'size': 16,
        }
plt.rc('font', **font)

Tdiag_min = [x / 60 for x in Tdiag6]
Trecexp_min = [x / 60 for x in Trecexp6]

plt.figure(1)
plt.plot(N7, Tdiag_min, '-or', label='Diag.')
plt.plot(N7, Trecexp_min, '-*b',  label='Rec. exp.')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Matrix size')
plt.ylabel('Time [min]')
# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(right=0.7)
plt.grid(True)
plt.show()

THREADS_REV = THREADS[::-1]
plt.figure(2)
plt.plot(THREADS_REV, Tdiag_th[0]/Tdiag_th, '-or', label='Diag.')
plt.plot(THREADS[::-1], Trecexp_th[0]/Trecexp_th, '-*b',  label='Rec. exp.')
plt.plot(THREADS_REV, [x / THREADS_REV[0] for x in THREADS_REV], ':k',  label='Ideal')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Number of threads')
plt.ylabel('Scaling')
# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(right=0.7)
plt.grid(True)
plt.show()





