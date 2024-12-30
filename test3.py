import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def plot_sin_cx():
    x = np.linspace(0, 2 * np.pi, 100)
    c = 1
    y = np.sin(c * x)

    fig, axis = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.25)
    l, = axis.plot(x, y, 'r-', label=f'$\\sin({c}x)$')
    axis.set_xlabel('$x$')
    axis.set_ylabel('$y$')
    axis.set_title(f'Graf funkce $\\sin({c}x)$')
    axis.grid(True, linestyle='--', color='lightgrey')
    axis.legend()

    # Přesunutí os do bodu (0,0)
    axis.spines['left'].set_position('zero')
    axis.spines['bottom'].set_position('zero')
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')

    # Přidání posuvníku
    ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03], facecolor='lightgoldenrodyellow')
    slider = Slider(ax_slider, 'c', 1, 10, valinit=c, valstep=0.1, valfmt='%1.2f', color='blue', track_color='red')

    def update(val):
        c = round(slider.val, 2)
        l.set_ydata(np.sin(c * x))
        l.set_label(f'$\\sin({c}x)$')
        axis.set_title(f'Graf funkce $\\sin({c}x)$')
        fig.canvas.draw_idle()
        axis.legend()

    slider.on_changed(update)

    plt.show()

plot_sin_cx()