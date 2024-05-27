import matplotlib.pyplot as plt

def gen_lineplot(var):

    plt.figure()
    plt.plot(var.timestamps, var.samples)
    plt.show()

    return
