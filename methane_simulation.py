import cantera as ct
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.yaml')
gas.TPX = 1000, 101325, 'O2:2, N2:7.56, CH4:1'
r = ct.Reactor(gas)
sim = ct.ReactorNet([r])
times = []
T = []
OH_fraction = []
CH4_fraction = []
O2_fraction = []
time = 5.e-1
for i in range(1, 2000):
    time += 5.e-4
    sim.advance(time)
    times.append(time)
    T.append(r.T)
    OH_fraction.append(r.thermo['OH'].X)
    CH4_fraction.append(r.thermo['CH4'].X)
    O2_fraction.append(r.thermo['O2'].X)

plt.plot(times, T)
plt.xlabel('Time [ms]')
plt.ylabel('Temperature [K]')
plt.savefig('methane_sim_T', dpi=1000)
plt.show()
plt.plot(times, OH_fraction)
plt.xlabel('Time [ms]')
plt.ylabel('OH mole fraction')
plt.arrow(0, 0.008, 1.072, 0, width=0.0001, head_width=0.001, head_length=0.05, length_includes_head=True, color='r',
          shape='full')
plt.annotate(r'$Ignition Delay$', xy=(0.6, 0.0085), fontsize=12)
plt.savefig('methane_sim_OH', dpi=1000)
plt.show()
plt.plot(times, CH4_fraction)
plt.xlabel('Time [ms]')
plt.ylabel('CH4 mole fraction')
plt.savefig('methane_sim_fuel', dpi=1000)
plt.show()
plt.plot(times, O2_fraction)
plt.xlabel('Time [ms]')
plt.ylabel('O2 mole fraction')
plt.savefig('methane_sim_O2', dpi=1000)
plt.show()
