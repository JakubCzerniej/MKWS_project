import cantera as ct
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.yaml')


def IgnitionDelay(gas):
    r = ct.Reactor(gas)
    sim = ct.ReactorNet([r])

    OH_fraction_prev = 0
    OH_fraction_now = 0

    while OH_fraction_prev <= OH_fraction_now:
        t = sim.step()
        OH_fraction_prev = OH_fraction_now
        OH_fraction_now = r.thermo['OH'].X

    return 1e6 * t


T = 2000  # constant initial temperature

for phi in range(50, 200, 25):
    P = []
    X = 'O2:2, N2:7.52, CH4:' + str(phi / 100)
    ign_delay = []
    for i in range(50000, 500000, 25000):
        P.append(i / 100000)
        gas.TPX = T, i, X
        ign_delay.append(IgnitionDelay(gas))
    plt.plot(P, ign_delay, label="phi=%.2f" % (phi / 100))

plt.legend()
plt.xlabel('Pressure [bar]')
plt.ylabel('Ignition delay time [microsecons]')
# plt.yscale('log')
plt.title('Ignition delay of methane-air mixture', fontweight='bold')
plt.grid()
plt.savefig('metan_pressure.png', dpi=1000)
plt.show()

