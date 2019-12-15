import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv

def generate_plot(plot_data):
   # nem oversigt over hvilket data vi bruger. Kan fjernes. Hvad syntes i? 
   maze_sizes = plot_data["maze_sizes"]
   avg_times = plot_data["avg_times"]
   min_times = plot_data["min_times"]
   max_times = plot_data["max_times"]
   avg_counts = plot_data["avg_counts"]
   min_counts = plot_data["min_counts"]
   max_counts = plot_data["max_counts"]


   # subplot fortæller at der kommer flere grafer og bestemmer opsætning. de tre tal er et todimentionelt array og nr. i arryaet
   plt.subplot(1,2,1)

   # bar laver de firkanter der viser tiden
   plt.bar(maze_sizes, max_times, width=1, align='center', label='Max solve time')
   plt.bar(maze_sizes, avg_times, width=1, align='center', label='Avg solve time') # bar(x-vals, y-vals, bar width, align bar relative to x-val on x-axis) )
   plt.bar(maze_sizes, min_times, width=1, align='center', label='Min solve time')

   # legend er den lille boks som viser hvad baren/farverne betyder 
   plt.legend(loc='upper left')

   plt.axis([min(maze_sizes)-2, max(maze_sizes) +2, 0, max(max_times) + (max(max_times) / 5)]) #axis(x-min, x-max, y-min, y-max)

   # Plot udskriver den tynde linjer.
   plt.plot(maze_sizes, max_times, linewidth=0.5, linestyle="-", marker="o")
   plt.plot(maze_sizes, avg_times, linewidth=0.5, linestyle="-", marker="o")
   plt.plot(maze_sizes, min_times, linewidth=0.5, linestyle="-", marker="o")

   # grid giver det grå grid i baggrunden
   plt.grid(color="g", linestyle="--", linewidth="0.1") # laver grid
   plt.title('Solving time', fontsize=12)
   plt.xlabel("maze size", fontsize=10)
   plt.ylabel("time in ns", fontsize=10)
   # Nr. 2 graf starter her 
   plt.subplot(1,2,2)

   plt.bar(maze_sizes, max_counts, width=1, align='center', label='Max points visited')
   plt.bar(maze_sizes, avg_counts, width=1, align='center', label='Avg points visited')
   plt.bar(maze_sizes,min_counts, width=1, align='center', label='Min points visited')

   plt.legend(loc='upper left')

   plt.axis([min(maze_sizes)-2, max(maze_sizes) +2, 0, max(max_counts) + (max(max_counts) / 5)])

   plt.plot(maze_sizes, max_counts, linewidth=0.5, linestyle="-", marker="o")
   plt.plot(maze_sizes, avg_counts, linewidth=0.5, linestyle="-", marker="o")
   plt.plot(maze_sizes, min_counts, linewidth=0.5, linestyle="-", marker="o")


   plt.grid(color="g", linestyle="--", linewidth="0.1")
   plt.title('Points vissited', fontsize=12)
   plt.xlabel("maze size", fontsize=10)
   plt.ylabel("points vissited", fontsize=10)
   plt.tick_params(axis='both', which='major', labelsize=10)

   plt.show()