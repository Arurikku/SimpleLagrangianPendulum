# N-uple Pendulum

## Reminders
A double pendulum looks like this:
![image_2023-10-31_161657269](https://github.com/Arurikku/SimpleLagrangianPendulum/assets/61802068/63ada122-09f3-4ca1-95e2-0e9b00247038)

Solving for the theta angles is simple using Lagrangian Mechanics.\
Let $A_1$ the point represented by the mass $m_1$ and $A_2$ the point represented by the mass $m_2$.\
From quick trigonometry, it follows that the coordinates of $A_1$ and $A_2$ are:
```math
\begin{aligned}
&A_1 = (x_1, y_1) = \bigl(L_1 \cdot \sin(\theta_1), -L_1 \cdot \cos(\theta_1)\bigr)\\
&A_2 = (x_2, y_2) = \bigl(L_1 \cdot \sin(\theta_1) + L_2 \cdot \sin(\theta_2), -L_1 \cdot \cos(\theta_1) - L_2 \cdot \cos(\theta_2)\bigr)
\end{aligned}
```
Hence,
```math
\begin{aligned}
&\dot{x_1} = \dot{\theta_1}L_1\cos(\theta_1) \ , \ \dot{y_1} = \dot{\theta_1}L_1\sin(\theta_1)\\
&\dot{x_2} = \dot{\theta_1}L_1\cos(\theta_1) + \dot{\theta_2}L_2\cos(\theta_2) \ , \ \dot{y_2} = \dot{\theta_1}L_1\sin(\theta_1) + \dot{\theta_2}L_2\sin(\theta_2)
\end{aligned}
```

Finding the kinetic energy $K_e$ and potentiel energy $P_e$ is straightforward here:
```math
\begin{aligned}
&K_e = \frac{1}{2}m_1(\dot{x_1}^2+\dot{y_1}^2) + \frac{1}{2}m_1(\dot{x_2}^2+\dot{y_2}^2)\\
&P_e = g(m_1 y_1 + m_2 y_2)
\end{aligned}
```
Changing to the $\theta$ coordinates and applying Euler-Lagrange equations solves the problem quite quickly
But why leave it at a double pendulum? What about a triple, quadruple, or N-uple pendulum?

## The N-uple Pendulum
For finding the differential equation governing our system, we follow the same steps as for the double pendulum.
Let $n$ be the number of masses in our pendulum, and each mass denoted by $m_1, m_2, \ldots , m_n$ with lengths $L_1, L_2, \ldots , L_n$ of angles $\theta_1, \theta_2, \ldots , \theta_n$.\
Each point of mass is denoted by the points $A_1(x_1, y_1) \ , \ A_2(x_2, y_2) \ , \ldots , \ A_n(x_n, y_n)$.
We have:
```math
\begin{aligned}
&x_1 = L_1\sin(\theta_1)\\
&y_1 = -L_1\cos(\theta_1)\\
&x_2 = x_1 + L_2\sin(\theta_2)\\
&y_2 = y_1 -L_2\cos(\theta_2)
\end{aligned}
```
and in general, for $w \in ⟦1, n⟧$:
```math
\begin{aligned}
&x_w = \sum_{k=1}^w L_k\sin(\theta_k)\\
&y_w = -\sum_{k=1}^w L_k\cos(\theta_k)\\
&\dot{x}_{w} = \sum_{k=1}^w L_k\dot{\theta}_k\cos(\theta_k)\\
&\dot{y}_w = \sum_{k=1}^w L_k\dot{\theta}_k\sin(\theta_k)
\end{aligned}
```

### Building the Lagrangian
```math
\begin{aligned}
&K_e = \frac{1}{2} \sum_{k=1}^n m_k \bigl(\dot{x}_k^2 + \dot{y}_k^2\bigr) = \frac{1}{2} \sum_{k=1}^n m_k \biggl(\Bigl(\sum_{j=1}^kL_j \dot{\theta}_j \cos(\theta_j)\Bigr)^2 + \Bigl(\sum_{j=1}^kL_j \dot{\theta}_j \sin(\theta_j)\Bigr)^2 \biggr)\\
&P_e = g\sum_{k=1}^nm_k y_k = -g\sum_{k=1}^nm_k \sum_{j=1}^k L_j\cos(\theta_j)\\
\end{aligned}
```
In the end, we have our Lagrangian:
```math
\begin{aligned}
&L = K_e - P_e\\
&L = \frac{1}{2} \sum_{k=1}^n m_k \biggl(\Bigl(\sum_{j=1}^kL_j \dot{\theta}_j \cos(\theta_j)\Bigr)^2 + \Bigl(\sum_{j=1}^kL_j \dot{\theta}_j \sin(\theta_j)\Bigr)^2 \biggr) + g\sum_{k=1}^n \sum_{j=1}^k m_k L_j\cos(\theta_j)\\
\end{aligned}
```
Let $w \in ⟦1, n⟧$, we calculate the partial derivatives of the lagrangian with respect to $\dot{\theta}_w$ and $\theta_w$:\
```math
\begin{aligned}
&\frac{\partial L}{\partial \dot{\theta}_w} = \sum_{k=1}^n m_k\Bigl(L_w \cos(\theta_w) \sum_{j=1}^k L_j \dot{\theta}_j \cos(\theta_j) + L_w \sin(\theta_w) \sum_{j=1}^kL_j \dot{\theta}_j \sin(\theta_j)\\
&\iff \frac{\partial L}{\partial \dot{\theta}_w} = \sum_{k=1}^n m_k L_w \sum_{j=1}^k L_j \dot{\theta}_j \bigl(\cos(\theta_j)\cos(\theta_w) + \sin(\theta_j)\sin(\theta_w)\bigr)\\
&\iff \frac{\partial L}{\partial \dot{\theta}_w} = \sum_{k=1}^n m_k L_w \sum_{j=1}^k L_j \dot{\theta}_j \cos(\theta_j - \theta_w)\\
\end{aligned}
```
```math
\begin{aligned}

\end{aligned}
```
