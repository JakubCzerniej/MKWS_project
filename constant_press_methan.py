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


P = 100000 * 5  # constant initial pressure

for phi in range(25, 175, 25):
    T = []
    X = 'O2:2, N2:7.52, CH4:' + str(phi / 100)
    ign_delay = []
    for i in range(1500, 4000, 100):
        T.append(i)
        gas.TPX = i, P, X
        ign_delay.append(IgnitionDelay(gas))
    plt.plot(T, ign_delay, label="phi=%.2f" % (phi / 100))

plt.legend()
plt.xlabel('Temperature [Kelvins]')
plt.ylabel('Ignition delay time [microsecons]')
# plt.yscale('log')
plt.title('Ignition delay of methane-air mixture', fontweight='bold')
plt.grid()
plt.savefig('metan-temp.png', dpi=1000)
plt.show()

