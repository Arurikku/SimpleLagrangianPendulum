import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def getCartesian(L, theta, previousPoint):
    return [previousPoint[0] + L*np.sin(theta), previousPoint[1] - L*np.cos(theta)]

def getAllPoints(data, n, L):
    output = [[0, 0]]
    for i in range(n):
        output.append(getCartesian(L[i], data[2*i], output[i]))
    xs = [el[0] for el in output]
    ys = [el[1] for el in output]
    return xs, ys

def getTheta(j, data):
    return data[2*j]

def getThetaDot(j, data):
    return data[2*j+1]

def pendulum_next(previous_data, masses, lengths):
    R_matrix = []
    coeff_matrix = []
    n = len(masses)
    for w in range(n):
        Lambda_w = lengths[w]*sum([masses[k] for k in range(n)])
        F_w = getThetaDot(w, previous_data)*sum([sum([masses[k]*lengths[j]*getThetaDot(j, previous_data)*np.sin(getTheta(j, previous_data)-getTheta(w, previous_data)) for j in range(k)]) for k in range(n)]) - g*np.sin(getTheta(w, previous_data))*sum([masses[k] for k in range(n)])
        R_w = F_w + sum([sum([masses[k]*lengths[j]*getThetaDot(j, previous_data)*(getThetaDot(j, previous_data) - getThetaDot(w, previous_data))*np.sin(getTheta(j, previous_data)-getTheta(w, previous_data)) for j in range(k) if j != w]) for k in range(n)])
        R_matrix.append(R_w)

        Q_k_w = lambda k: lengths[k]*np.cos(getTheta(k, previous_data) - getTheta(w, previous_data))*sum([masses[j] for j in range(k) if j != w])

        matrix_row = []
        for k in range(n):
            if k == w:
                matrix_row.append(Lambda_w)
                continue
            matrix_row.append(Q_k_w(k))
        coeff_matrix.append(matrix_row)
    Matrix_Inv = np.linalg.inv(coeff_matrix)
    output = Matrix_Inv.dot(R_matrix)
    return output



#Format: theta_1, theta_dot_1, theta_2, theta_dot_2, ..., theta_n, theta_dot_n
initial_conditions = [np.pi/3, 0, np.pi/2.5, 0, np.pi/2, 0, np.pi/1.5, 0, np.pi, 0]

#Format: m_1, m_2, ..., m_n
mass_list = [0.1, 0.1, 0.1, 0.1, 1]

#Format: L_1, L_2, ..., L_n
length_list = [0.5, 0.5, 0.5, 0.5, 0.5]


g = 9.81

n = len(mass_list)

dt = 0.0001
t_end = 20

U = initial_conditions

ctr = 0
print("Start")

scale = sum([length_list[i] for i in range(n)])
scale *= 1.1

speedUp = int(1/(100*dt))
print("FastForward factor:", speedUp)

fig, ax = plt.subplots()
ax.axis([-scale,scale,-scale,scale])
ax.set_aspect("equal")
xCoords, yCoords = getAllPoints(U, n, length_list)
line, = ax.plot(xCoords, yCoords, marker="o")

def update(t):
    for AAAA in range(speedUp):
        next_data = pendulum_next(U, mass_list, length_list)
        new_U = []
        for i in range(n):
            new_theta = (dt * U[2 * i + 1] + U[2 * i])
            new_theta_dot = (dt * next_data[i] + U[2 * i + 1])
            new_U.append(new_theta)
            new_U.append(new_theta_dot)
        for i in range(len(U)):
            U[i] = new_U[i]
    xCoords, yCoords = getAllPoints(U, n, length_list)
    line.set_data(xCoords, yCoords)
    return line,

ani = FuncAnimation(fig, update, interval=1, blit=True, frames=int(t_end/dt))

plt.show()