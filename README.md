# Technical Test - Wise Athena

# Software
Visual Studio Code

# Hardware
i7 de 10th GEN con 16GB de RAM

# Requirements
Python 3.8.0
Libreries: os, sys, pandas, matplotlib, seaborn

#  Folders description

- Data
    - maestro_clientes_prueba.xlsx: information about the stores and distributors that sell the customer's products.
    - maestro_productos_prueba.xlsx: information about products sold by our customer and competitors.
    - sellin_final.csv: final csv with all the data cleaned about sellin.
    - sellin.csv: sales history and sellin price (from manufacturer to retailer) for each product and store.
    - sellout_final.csv: final csv with all the data cleaned about sellout
    - sellout-proveedor1.csv: sales history and sellout price (from the retailer to the final consumer) for each product and each store of supplier 1.
    - sellout-proveedor2.csv: sales history and sellout price (from the retailer to the final consumer) for each product and each store of supplier 2.

- documentation:
    - instrucciones_prueba.pdf: Test instructions.

- reports:
    - Figures / visualizations of the analysis part of the project.

- src:
    - utils:
        - mining_data_tb.py: functions(def) related to data mining.
        - visualization_tb.py: functions related to displaying graphs about data.

    - main.ipynb: file with the main code of the project.
    - main.html: the same file as main.ipynb but in html format.