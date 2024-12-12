import numpy as np
import matplotlib.pyplot as plt
sample_sizes = np.logspace(1, 6, num=20, dtype=int)
n_repeats = 1000 # Number of repetitions to compute SEM and SE of sigma
means_X = []
means_Y = []
std_X = []
std_Y = []
sem_X = []
sem_Y = []
se_sigma_X = []
se_sigma_Y = []
def compute_sem(data):
    return np.std(data) / np.sqrt(len(data))
def compute_se_sigma(data):
    return np.std(data) / np.sqrt(2 * len(data))
for N in sample_sizes:
    X_samples = np.random.uniform(0, 1, (n_repeats, N))
    Y_samples = 1 / X_samples
    mean_X = np.mean(X_samples, axis=1)
    mean_Y = np.mean(Y_samples, axis=1)
    sem_X.append(compute_sem(mean_X))
    sem_Y.append(compute_sem(mean_Y))
    sigma_X = np.std(X_samples, axis=1)
    sigma_Y = np.std(Y_samples, axis=1)
    se_sigma_X.append(compute_se_sigma(sigma_X))
    se_sigma_Y.append(compute_se_sigma(sigma_Y))
    temp = np.random.uniform(0, 1, N)
    # means_X.append(np.mean(temp))
    # std_X.append(np.std(temp))
    # means_Y.append(np.mean(1/temp))
    # std_Y.append(np.std(1/temp))
    means_X.append(np.mean(mean_X))
    std_X.append(np.mean(np.std(X_samples, axis=1)))
    means_Y.append(np.mean(mean_Y))
    std_Y.append(np.mean(np.std(Y_samples, axis=1)))
fig, axs = plt.subplots(2, 1, figsize=(10, 12))
axs[0].loglog(sample_sizes, means_X, 'b-o', label='Mean of X ~ Uniform[0,1]')
axs[0].loglog(sample_sizes, std_X, 'b--o', label='Std of X ~ Uniform[0,1]')
axs[0].loglog(sample_sizes, means_Y, 'r-o', label='Mean of Y = 1/X')
axs[0].loglog(sample_sizes, std_Y, 'r--o', label='Std of Y = 1/X')
axs[0].set_xlabel('Sample Size')
axs[0].set_ylabel('Mean and Std')
axs[0].set_title('Mean and Standard Deviation vs Sample Size')
axs[0].legend()
axs[0].grid(True)
axs[1].loglog(sample_sizes, sem_X, 'b-o', label='SEM of X ~ Uniform[0,1]')
axs[1].loglog(sample_sizes, se_sigma_X, 'b--o', label='SE of Sigma of X ~ Uniform[0,1]')
axs[1].loglog(sample_sizes, sem_Y, 'r-o', label='SEM of Y = 1/X')
axs[1].loglog(sample_sizes, se_sigma_Y, 'r--o', label='SE of Sigma of Y = 1/X')
axs[1].set_xlabel('Sample Size')
axs[1].set_ylabel('Standard Error')
axs[1].set_title('Standard Error of the Mean and Std vs Sample Size')
axs[1].legend()
axs[1].grid(True)
plt.tight_layout()
plt.show()
