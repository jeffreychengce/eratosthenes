import matplotlib.pyplot as plt
import numpy as np

def prime_prop(all_nmax, all_proportions):
    plt.plot(all_nmax, all_proportions)
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    plt.show()

def prime_prop_log(all_nmax, all_proportions):
    plt.plot(all_nmax, all_proportions)
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    plt.xscale("log")
    plt.yscale("log")
    plt.show()

def time_comp(times_1, times_2):
    times_1_mean = np.mean(times_1)
    times_2_mean = np.mean(times_2)
    
    times_1_std = np.std(times_1)
    times_2_std = np.std(times_2)
    
    fig, ax = plt.subplots()
    ax.bar(np.array([0, 1]), [times_1_mean, times_2_mean], yerr=[times_1_std, times_2_std], align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_ylabel('Time per Iteration')
    ax.set_xticks(np.array([0, 1]))
    ax.set_xticklabels(['Implementation 1', 'Implementation 2'])
    ax.set_title('Sieve Runtime over Differing Implementations')
    ax.yaxis.grid(True)
    plt.show()
