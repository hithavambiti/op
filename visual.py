import numpy as np
import matplotlib.pyplot as plt

with open('omega_output.csv', 'r') as f:
    lines = f.read().splitlines()

lines = [l.strip() for l in lines if l.strip()]

data = np.array([
    [float(x) for x in line.split(',')]
    for line in lines
])

norms = np.linalg.norm(data, axis=1)
time = np.arange(len(norms))

# Save to CSV
np.savetxt('norms.csv', np.column_stack((time, norms)), delimiter=',', header='time,norm', fmt=['%d', '%.15e'])

# Plot
plt.figure(figsize=(10, 5))
plt.plot(time, norms, linewidth=1.5)
plt.xlabel('Time (index)')
plt.ylabel('Norm')
plt.title('Vector Norm over Time')
plt.grid(True)
plt.tight_layout()
plt.savefig('norms_plot.png', dpi=150)
plt.show()
print('Saved norms.csv and norms_plot.png')
