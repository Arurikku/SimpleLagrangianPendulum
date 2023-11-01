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
Let $w \in ⟦1, n⟧$, we calculate the partial derivatives of the lagrangian with respect to $\dot{\theta}_w$ :
```math
\begin{aligned}
&\frac{\partial L}{\partial \dot{\theta}_w} = \sum_{k=1}^n m_k\Bigl(L_w \cos(\theta_w) \sum_{j=1}^k L_j \dot{\theta}_j \cos(\theta_j) + L_w \sin(\theta_w) \sum_{j=1}^kL_j \dot{\theta}_j \sin(\theta_j)\\
&\iff \frac{\partial L}{\partial \dot{\theta}_w} = \sum_{k=1}^n m_k L_w \sum_{j=1}^k L_j \dot{\theta}_j \bigl(\cos(\theta_j)\cos(\theta_w) + \sin(\theta_j)\sin(\theta_w)\bigr)\\
&\iff \frac{\partial L}{\partial \dot{\theta}_w} = \sum_{k=1}^n m_k L_w \sum_{j=1}^k L_j \dot{\theta}_j \cos(\theta_j - \theta_w)\\
\end{aligned}
```
Taking the time derivative yields:
```math
\begin{aligned}
&\frac{d}{dt}\frac{\partial L}{\partial \dot{\theta}_w} = L_w \sum_{k=1}^n m_k \sum_{j=1}^k L_j \bigl(\ddot{\theta}_j \cos(\theta_j - \theta_w) - \dot{\theta}_j (\dot{\theta}_j - \dot{\theta}_w) \sin(\theta_j - \theta_w)\bigr)
\end{aligned}
```
We now calculage the partial of the lagrangian with respect to $\theta_w$ :
```math
\begin{aligned}
&\frac{\partial L}{\partial \theta_w} = \sum_{k=1}^n m_k L_w \dot{\theta}_w \sum_{j=1}^k L_j \dot{\theta}_j \bigl(\sin(\theta_j)\cos(\theta_w) - \cos(\theta_j)\sin(\theta_w)\bigr) - g L_w \sin(\theta_w) \sum_{k=1}^n m_k \\
&\iff \frac{\partial L}{\partial \theta_w} = \sum_{k=1}^n m_k L_w \dot{\theta}_w \sum_{j=1}^k L_j \dot{\theta}_j sin(\theta_j -\theta_w ) - g L_w \sin(\theta_w) \sum_{k=1}^n m_k \\
\end{aligned}
```
### Applying the principle of least action (Euler-Lagrange):
```math
\begin{aligned}
&\text{The principle of least action says that } \frac{d}{dt} \frac{\partial L}{\partial \dot{\theta}_w} = \frac{\partial L}{\partial \theta_w}
\end{aligned}
```
We are now going to rewrite $\frac{d}{dt}\frac{\partial L}{\partial \dot{\theta}_w}$ to bring out a single $\ddot{\theta}_w$ term:
```math
\begin{aligned}
&\frac{d}{dt}\frac{\partial L}{\partial \dot{\theta}_w} = L_w \sum_{k=1}^n m_k \sum_{j=1}^k L_j \bigl(\ddot{\theta}_j \cos(\theta_j - \theta_w) - \dot{\theta}_j (\dot{\theta}_j - \dot{\theta}_w) \sin(\theta_j - \theta_w)\bigr) \\
&\iff \frac{d}{dt}\frac{\partial L}{\partial \dot{\theta}_w} = L_w \sum_{k=1}^n m_k \Bigl(\sum_{{j=1} \atop{j \neq w}}^k L_j \bigl(\ddot{\theta}_j \cos(\theta_j - \theta_w) - \dot{\theta}_j (\dot{\theta}_j - \dot{\theta}_w) \sin(\theta_j - \theta_w)\bigr) + L_w \ddot{\theta}_w \Bigr) \\
&\iff \frac{d}{dt}\frac{\partial L}{\partial \dot{\theta}_w} = L_w^2 \ddot{\theta}_w \sum_{k=1}^n m_k + L_w \sum_{k=1}^n m_k \sum_{{j=1} \atop{j \neq w}}^k L_j \bigl(\ddot{\theta}_j \cos(\theta_j - \theta_w) - \dot{\theta}_j (\dot{\theta}_j - \dot{\theta}_w) \sin(\theta_j - \theta_w)\bigr)
\end{aligned}
```
In the end, the principle of least action yields:
```math
\begin{aligned}
&L_w \ddot{\theta}_w \sum_{k=1}^n m_k + \sum_{k=1}^n m_k \sum_{{j=1} \atop{j \neq w}}^k L_j \bigl(\ddot{\theta}_j \cos(\theta_j - \theta_w) - \dot{\theta}_j (\dot{\theta}_j - \dot{\theta}_w) \sin(\theta_j - \theta_w)\bigr) = \dot{\theta}_w \sum_{k=1}^n m_k \sum_{j=1}^k L_j \dot{\theta}_j sin(\theta_j -\theta_w ) - g \sin(\theta_w) \sum_{k=1}^n m_k \\
&\iff L_w \ddot{\theta}_w \sum_{k=1}^n m_k + \sum_{k=1}^n m_k \sum_{{j=1} \atop{j \neq w}}^k L_j \ddot{\theta}_j \cos(\theta_j - \theta_w) = \dot{\theta}_w \sum_{k=1}^n m_k \sum_{j=1}^k L_j \dot{\theta}_j sin(\theta_j -\theta_w ) - g \sin(\theta_w) \sum_{k=1}^n m_k + \sum_{k=1}^n m_k \sum_{{j=1} \atop{j \neq w}}^k L_j \dot{\theta}_j (\dot{\theta}_j - \dot{\theta}_w) \sin(\theta_j - \theta_w)
\end{aligned}
```
We now package into simpler terms:
```math
\begin{aligned}
&\text{Let } \lambda_w = L_w \sum_{k=1}^n m_k \\
&\text{Let } R_w = \dot{\theta}_w \sum_{k=1}^n m_k \sum_{j=1}^k L_j \dot{\theta}_j sin(\theta_j -\theta_w ) - g \sin(\theta_w) \sum_{k=1}^n m_k + \sum_{k=1}^n m_k \sum_{{j=1} \atop{j \neq w}}^k L_j \dot{\theta}_j (\dot{\theta}_j - \dot{\theta}_w) \sin(\theta_j - \theta_w) \\
&\text{which gives us: } \ddot{\theta}_w \lambda_w + \sum_{k=1}^n m_k \sum_{{j=1} \atop{j \neq w}}^k \ddot{\theta}_j L_j \cos(\theta_j - \theta_w) = R_w \\
&\iff \ddot{\theta}_w \lambda_w + \sum_{k=1}^n \ddot{\theta}_k L_k \cos(\theta_k - \theta_w)  \sum_{{j=k} \atop{j \neq w}}^n m_j  = R_w \\
&\text{Let } Q_{k,w} = L_k \cos(\theta_k - \theta_w)  \sum_{{j=k} \atop{j \neq w}}^n m_j \\
&\text{We have } \ddot{\theta}_w \lambda_w + \sum_{k=1}^n \ddot{\theta}_k Q_{k,w}  = R_w \\
\end{aligned}
```
### Solving the system of equations
We now have $\forall w \in ⟦1, n⟧$:
```math
\begin{aligned}
&\ddot{\theta}_w \lambda_w + \sum_{k=1}^n \ddot{\theta}_k Q_{k,w}  = R_w
\end{aligned}
```
Which can be expressed as an n-dimension system of equations:
```math
\begin{cases}
\ddot{\theta}_1\lambda_1 + \ddot{\theta}_2 Q_{2,1} + \ddot{\theta}_3 Q_{3,1} + \ldots + \ddot{\theta}_n Q_{n,1}  = R_1 \\
\ddot{\theta}_1 Q_{1,2} + \ddot{\theta}_2 \lambda_2 + \ddot{\theta}_3 Q_{3,2} + \ldots + \ddot{\theta}_n Q_{n, 2}  = R_2 \\
\vdots \\
\ddot{\theta}_1 Q_{1,n} + \ddot{\theta}_2 Q_{2,n} + \ddot{\theta}_3 Q_{3,n} + \ldots + \ddot{\theta}_n \lambda_n  = R_n \\
\end{cases}
```
Written as a matrix equation yields
```math
\begin{pmatrix}
\lambda_1 \ \ \ Q_{2,1} \ \ \ Q_{3,1} \ \ \ \ldots  \ \ \ Q_{n,1} \\
Q_{1,2} \ \ \ \lambda_2 \ \ \ Q_{3,2} \ \ \ \ldots  \ \ \ Q_{n,2} \\
\vdots \\
Q_{1,n} \ \ \ Q_{2,n} \ \ \ Q_{3,n} \ \ \ \ldots  \ \ \ \lambda_n
\end{pmatrix}
\begin{pmatrix}
\ddot{\theta}_1\\
\ddot{\theta}_2\\
\vdots \\
\ddot{\theta}_n
\end{pmatrix}
=
\begin{pmatrix}
R_1\\
R_2\\
\vdots \\
R_n
\end{pmatrix}
```
Hence, 
```math
\begin{pmatrix}
\ddot{\theta}_1\\
\ddot{\theta}_2\\
\vdots \\
\ddot{\theta}_n
\end{pmatrix}
=
\begin{pmatrix}
\lambda_1 \ \ \ Q_{2,1} \ \ \ Q_{3,1} \ \ \ \ldots  \ \ \ Q_{n,1} \\
Q_{1,2} \ \ \ \lambda_2 \ \ \ Q_{3,2} \ \ \ \ldots  \ \ \ Q_{n,2} \\
\vdots \\
Q_{1,n} \ \ \ Q_{2,n} \ \ \ Q_{3,n} \ \ \ \ldots  \ \ \ \lambda_n
\end{pmatrix}^{-1}
\begin{pmatrix}
R_1\\
R_2\\
\vdots \\
R_n
\end{pmatrix}
```
So in the end we have a closed form for each $\ddot{\theta}_w$ with $w \in ⟦1, n⟧$, meaning we can use the basic backward Euler method to get every angle of every mass from a time $t_1$ to $t_2$ using python.

## Extra Stuff
- It should be reminded that computers are not perfectly accurate in floating point number arithmetic, and even a triple pendulum is infamous for its extremely sensitive chaotic behaviour.\
So while the final equation is perfectly accurate, simulating it will yield minuscule approximations which will create an unpredictable chaos very quickly.
- For very long simulations, it might be necessary to apply modular arithmetic to bound the angles between $0$ and $2\pi$, as the angle can keep increasing until overflow.
