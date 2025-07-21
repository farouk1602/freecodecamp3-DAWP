# This file is for testing your functions
from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Save categorical plot
cat_plot = draw_cat_plot()
cat_plot.savefig("catplot.png")

# Save heat map
heat_map = draw_heat_map()
heat_map.savefig("heatmap.png")
