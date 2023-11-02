import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import moviepy.editor as mp

def printForDesmos(tab): #Prints the coordinates in a way Desmos can understand
    strOut = ""
    for i in range(0, len(tab), stp):
        xPt = str(tab[i])
        if "e" in xPt:
            ind = xPt.index("e")
            strOut += xPt[:ind] + "*10^{" + xPt[ind + 1:] + "},"
            continue
        strOut += xPt + ","
    return strOut

def getTheta(j, data):
    return data[2*j]

def getThetaDot(j, data):
    return data[2*j+1]

def getCartesian(t, L, data):
    return (L*np.sin(data[t]), -L*np.cos(data[t]))

#TODO: Pendulum seems to gain speed? especially when it goes to the left.

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

    #print(output)
    return output



#Format: theta_1, theta_dot_1, theta_2, theta_dot_2, ..., theta_n, theta_dot_n
initial_conditions = [np.pi/3, 0, np.pi/2.5, 0, np.pi/2.5, 0, np.pi/1.5, 0]

#Format: m_1, m_2, ..., m_n
mass_list = [1, 1, 1]

#Format: L_1, L_2, ..., L_n
length_list = [1, 1, 1]


g = 9.81

n = len(mass_list)

dt = 0.001
t_end = 5
nPoints = 400
stp = int(t_end/(dt*nPoints))

U = initial_conditions

curr_time = 0
ctr = 0
print("Start")
#Get all the angles
while curr_time <= t_end:
    previous_data = U[2*n*ctr:2*n*(ctr+1)]
    next_data = pendulum_next(previous_data, mass_list, length_list)
    for i in range(n):
        new_theta = (dt*previous_data[2*i+1] + previous_data[2*i])
        new_theta_dot = (dt*next_data[i] + previous_data[2*i+1])
        U.append(new_theta)
        U.append(new_theta_dot)
    if ctr % int((t_end / dt) / 100) == 0:
        print(round(curr_time, 4), "out of", t_end, "(" + str(round(100 * curr_time/t_end, 4)) + "%)")
    curr_time+=dt
    ctr += 1

#Pack just the values of of all the thetas (not the theta_dot)
thetas = []
for j in range(n):
    theta_j = []
    for i in range(2*j, len(U), 2 * n):
        theta_j.append(U[i])
    thetas.append(theta_j)

txt = [printForDesmos(x) for x in thetas]

print("Parsed for desmos:")
print("M_{1}=\\left(L_{1}\\sin\\left(P_{t1}\\left[t\\right]\\right),-L_{1}\\cos\\left(P_{t1}\\left[t\\right]\\right)\\right)")
print("L_{1}=" + str(length_list[0]))

for i in range(1,len(txt)):
    print("M_{" + str(i+1) + "}=\\left(M_{" + str(i) + "}.x+L_{" + str(i+1) + "}\\sin\\left(P_{t" + str(i+1) + "}\\left[t\\right]\\right),M_{" + str(i) + "}.y-L_{" + str(i+1) + "}\\cos\\left(P_{t" + str(i+1) + "}\\left[t\\right]\\right)\\right)")
    print("L_{" + str(i+1) + "}=" + str(length_list[i]))

print("\\left(0,0\\right),M_{1}")
for i in range(1,len(txt)):
    print("M_{" + str(i) + "},M_{" + str(i+1) + "}")

for i in range(len(txt)):
    print("P_{t" + str(i+1) + "}=\\left[", txt[i][:-1], "\\right]")
