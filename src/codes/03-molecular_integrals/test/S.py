from numpy import sqrt, exp, pi 
def Sij(i, j, alpha, beta, Ax, Bx):
    AB_diff = Ax - Bx 
    AB_diff_squared = AB_diff**2 
    AB_sum = alpha + beta 
    AB_product = alpha * beta 
    if i < 0 or j < 0:
        return 0.0
    if (i,j) == (0, 0): 
        return sqrt(pi)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/sqrt(AB_sum)
    if (i,j) == (0, 1): 
        return sqrt(pi)*alpha*(AB_diff - AB_diff*alpha/AB_sum)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(sqrt(AB_sum)*beta)
    if (i,j) == (0, 2): 
        return sqrt(pi)*(alpha*(2*alpha*(AB_diff - AB_diff*alpha/AB_sum)**2 - 1 + alpha/AB_sum)/beta + 1)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(2*sqrt(AB_sum)*beta)
    if (i,j) == (0, 3): 
        return sqrt(pi)*alpha*(AB_diff - AB_diff*alpha/AB_sum)*(alpha*(2*alpha*(AB_diff - AB_diff*alpha/AB_sum)**2 - 3 + 3*alpha/AB_sum)/beta + 3)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(2*sqrt(AB_sum)*beta**2)
    if (i,j) == (1, 0): 
        return sqrt(pi)*(-AB_diff + AB_diff*alpha/AB_sum)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/sqrt(AB_sum)
    if (i,j) == (1, 1): 
        return sqrt(pi)*(2*alpha*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 1 - alpha/AB_sum)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(2*sqrt(AB_sum)*beta)
    if (i,j) == (1, 2): 
        return sqrt(pi)*(-AB_diff + AB_diff*alpha/AB_sum + alpha*(2*alpha*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**2 + (-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum) + 2*(1 - alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum))/beta)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(2*sqrt(AB_sum)*beta)
    if (i,j) == (1, 3): 
        return sqrt(pi)*(6*alpha*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + alpha*(4*alpha**2*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**3 + 6*alpha*(-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 6*alpha*(1 - alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**2 + 3*(-1 + alpha/AB_sum)*(1 - alpha/AB_sum))/beta + 3 - 3*alpha/AB_sum)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(4*sqrt(AB_sum)*beta**2)
    if (i,j) == (2, 0): 
        return sqrt(pi)*(2*alpha*(-AB_diff + AB_diff*alpha/AB_sum)**2 + alpha/AB_sum)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(2*sqrt(AB_sum)*alpha)
    if (i,j) == (2, 1): 
        return sqrt(pi)*(AB_diff - AB_diff*alpha/AB_sum + 2*alpha*(-AB_diff + AB_diff*alpha/AB_sum)**2*(AB_diff - AB_diff*alpha/AB_sum) + (-1 + alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 2*(1 - alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum))*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(2*sqrt(AB_sum)*beta)
    if (i,j) == (2, 2): 
        return sqrt(pi)*((2*alpha*(AB_diff - AB_diff*alpha/AB_sum)**2 - 1 + alpha/AB_sum)/beta + (4*alpha**2*(-AB_diff + AB_diff*alpha/AB_sum)**2*(AB_diff - AB_diff*alpha/AB_sum)**2 + 2*alpha*(-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)**2 + 2*alpha*(-1 + alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**2 + 8*alpha*(1 - alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + (-1 + alpha/AB_sum)**2 + 2*(1 - alpha/AB_sum)**2)/beta + (2*alpha*(-AB_diff + AB_diff*alpha/AB_sum)**2 - 1 + alpha/AB_sum)/alpha + 1/alpha)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(4*sqrt(AB_sum)*beta)
    if (i,j) == (2, 3): 
        return sqrt(pi)*(-3*AB_diff*alpha/AB_sum + 3*Ax - 3*Bx + 6*alpha*(-AB_diff + AB_diff*alpha/AB_sum)**2*(AB_diff - AB_diff*alpha/AB_sum) + alpha*(AB_diff - AB_diff*alpha/AB_sum)*(2*alpha*(AB_diff - AB_diff*alpha/AB_sum)**2 - 3 + 3*alpha/AB_sum)/beta + alpha*(4*alpha**2*(-AB_diff + AB_diff*alpha/AB_sum)**2*(AB_diff - AB_diff*alpha/AB_sum)**3 + 6*alpha*(-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)**2*(AB_diff - AB_diff*alpha/AB_sum) + 2*alpha*(-1 + alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**3 + 12*alpha*(1 - alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**2 + 3*(-1 + alpha/AB_sum)**2*(AB_diff - AB_diff*alpha/AB_sum) + 6*(-1 + alpha/AB_sum)*(1 - alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum) + 6*(1 - alpha/AB_sum)**2*(AB_diff - AB_diff*alpha/AB_sum))/beta + 3*(-1 + alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 6*(1 - alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum))*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(4*sqrt(AB_sum)*beta**2)
    if (i,j) == (3, 0): 
        return sqrt(pi)*(-AB_diff + AB_diff*alpha/AB_sum)*(2*alpha*(-AB_diff + AB_diff*alpha/AB_sum)**2 + 3*alpha/AB_sum)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(2*sqrt(AB_sum)*alpha)
    if (i,j) == (3, 1): 
        return sqrt(pi)*(4*alpha**2*(-AB_diff + AB_diff*alpha/AB_sum)**3*(AB_diff - AB_diff*alpha/AB_sum) + 6*alpha*(-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 6*alpha*(1 - alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)**2 + 6*alpha*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 3*(-1 + alpha/AB_sum)*(1 - alpha/AB_sum) + 3 - 3*alpha/AB_sum)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(4*AB_product*sqrt(AB_sum))
    if (i,j) == (3, 2): 
        return sqrt(pi)*((6*alpha*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**2 + 3*(-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum) + 6*(1 - alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum))/beta + (4*alpha**2*(-AB_diff + AB_diff*alpha/AB_sum)**3*(AB_diff - AB_diff*alpha/AB_sum)**2 + 2*alpha*(-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)**3 + 6*alpha*(-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**2 + 12*alpha*(1 - alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)**2*(AB_diff - AB_diff*alpha/AB_sum) + 3*(-1 + alpha/AB_sum)**2*(-AB_diff + AB_diff*alpha/AB_sum) + 6*(-1 + alpha/AB_sum)*(1 - alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 6*(1 - alpha/AB_sum)**2*(-AB_diff + AB_diff*alpha/AB_sum))/beta + (-3*AB_diff + 3*AB_diff*alpha/AB_sum)/alpha + (-AB_diff + AB_diff*alpha/AB_sum)*(2*alpha*(-AB_diff + AB_diff*alpha/AB_sum)**2 - 3 + 3*alpha/AB_sum)/alpha)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(4*sqrt(AB_sum)*beta)
    if (i,j) == (3, 3): 
        return sqrt(pi)*((12*alpha**2*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**3 + 18*alpha*(-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 18*alpha*(1 - alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**2 + 9*(-1 + alpha/AB_sum)*(1 - alpha/AB_sum))/beta + (8*alpha**3*(-AB_diff + AB_diff*alpha/AB_sum)**3*(AB_diff - AB_diff*alpha/AB_sum)**3 + 12*alpha**2*(-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)**3*(AB_diff - AB_diff*alpha/AB_sum) + 12*alpha**2*(-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**3 + 36*alpha**2*(1 - alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)**2*(AB_diff - AB_diff*alpha/AB_sum)**2 + 18*alpha*(-1 + alpha/AB_sum)**2*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 18*alpha*(-1 + alpha/AB_sum)*(1 - alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)**2 + 18*alpha*(-1 + alpha/AB_sum)*(1 - alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum)**2 + 36*alpha*(1 - alpha/AB_sum)**2*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 9*(-1 + alpha/AB_sum)**2*(1 - alpha/AB_sum) + 6*(1 - alpha/AB_sum)**3)/beta + (18*alpha*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 9 - 9*alpha/AB_sum)/alpha + (12*alpha**2*(-AB_diff + AB_diff*alpha/AB_sum)**3*(AB_diff - AB_diff*alpha/AB_sum) + 18*alpha*(-1 + alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)*(AB_diff - AB_diff*alpha/AB_sum) + 18*alpha*(1 - alpha/AB_sum)*(-AB_diff + AB_diff*alpha/AB_sum)**2 + 9*(-1 + alpha/AB_sum)*(1 - alpha/AB_sum))/alpha)*exp(alpha*(AB_diff**2*alpha/AB_sum - AB_diff_squared))/(8*sqrt(AB_sum)*beta**2)
