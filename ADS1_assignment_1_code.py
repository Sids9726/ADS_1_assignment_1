"""
Created on Wed Nov  8 05:45:18 2023

@author: Lenovo
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def initial_operation():
    """ 
        this function gives the value of x axis and y axis and also the 
        countries name as well
    """

    # read the CSV file
    data_f = pd.read_csv("mortality.csv")

    # total years (data for X-axis)
    year = ["Country Name", "1990", "2000", "2003"]
    second_phase = np.arange(2013, 2022).astype(str)
    year.extend(second_phase)

    # total countries
    countries = ["India", "Spain", "Finland", "Zimbabwe"]

    # mortality rate (data for Y-axis)
    mortality_rate = data_f.loc[(data_f["Country Name"].isin(countries)) & ( 
    data_f["Series Name"] == "Mortality rate, under-5 (per 1,000 live births)"
    ), year]
    return mortality_rate


def mortality_rate_type_conversion(mortality_rate):
    """
       this whole function converts the values from one type to another type
       and also transpose the dataframe.
    """

    # transpose of dataframe
    mortality_rate_t = pd.DataFrame.transpose(mortality_rate)
    header = mortality_rate_t.iloc[0].values.tolist()
    mortality_rate_t.columns = header
    mortality_rate_t = mortality_rate_t.iloc[2:]
    mortality_rate_t.index = mortality_rate_t.index.astype(int)

    # conversion of mortality rate value from string to float
    mortality_rate_t["India"] = mortality_rate_t["India"].astype(float)
    mortality_rate_t["Spain"] = mortality_rate_t["Spain"].astype(float)
    mortality_rate_t["Finland"] = mortality_rate_t["Finland"].astype(float)
    mortality_rate_t["Zimbabwe"] = mortality_rate_t["Zimbabwe"].astype(float)
    return mortality_rate_t


def generate_linechart(new_mortality_rate):
    '''
        this function i have used to define line chart with all kind of 
        parameters such as label and others in this function the labelling 
        is done for both axis and also given the title to this graph and at
        the end the figure has saved using savefig() function
    '''

    # set the size of figure
    plt.figure(figsize=(8, 6))
    mortality_rate_t = mortality_rate_type_conversion(new_mortality_rate)

    # plotting of line chart with additional information (legend and title)
    plt.plot(mortality_rate_t.index,
             mortality_rate_t["India"], label="india")
    plt.plot(mortality_rate_t.index,
             mortality_rate_t["Spain"], label="spain")
    plt.plot(mortality_rate_t.index,
             mortality_rate_t["Finland"], label="Finland")
    plt.plot(mortality_rate_t.index,
             mortality_rate_t["Zimbabwe"], label="Zimbabwe")

    # set the label to x-axis and y-axis
    plt.xlabel("year")
    plt.ylabel("mortality")

    # set title to this chart
    plt.title("Mortality rate (per 1000 live births)")
    plt.legend(loc='upper right')

    # Saving the figure
    plt.savefig("linechart.jpg")


def generate_piechart(new_mortality_rate):
    """
        this function i have used to define pie chart with all kind of 
        parameters such as label, index, labeldistance, fontsize and others 
        in this function. the labelling is done for both axis and also given 
        the title to this graph and at the end the figure has saved using 
        savefig() function
    """

    # size of figure
    plt.figure(figsize=(10, 6))

    # method of subplotting to display the two plots in single screen.
    plt.subplot(1, 2, 1)
    mortality_rate_t = mortality_rate_type_conversion(new_mortality_rate)
    countries = ["India", "Spain", "Finland", "Zimbabwe"]

    plt.pie(mortality_rate_t.loc[mortality_rate_t.index == 2019, countries].
            values[0], labels=countries, autopct='%1.1f%%',
            startangle=90,
            shadow=False,
            wedgeprops={"edgecolor": "black",
                        'linewidth': 1,
                        'antialiased': True},
            textprops={'fontsize': 9}, radius=0.5, pctdistance=1.17,
            labeldistance=1.30)

    # set title to pie graph
    plt.title("mortality rate 2019")
    plt.axis('equal')

    # method of subplotting to display the two plots in single screen.
    plt.subplot(1, 2, 2)

    plt.pie(mortality_rate_t.loc[mortality_rate_t.index == 2000, countries].
            values[0], labels=countries, autopct='%1.1f%%',
            startangle=90,
            shadow=False,
            wedgeprops={"edgecolor": "black",
                        'linewidth': 1,
                        'antialiased': True},
            textprops={'fontsize': 9}, radius=0.5, pctdistance=1.17,
            labeldistance=1.30)

    # set title to pie graph
    plt.title("mortality rate 2021")
    plt.axis('equal')

    # Saving the figure.
    plt.savefig("piechart.jpg")


def generate_barchart():
    """ 
        plot bar graph using bar function and give some parameters to make 
        effective look.
    """

    # size of figure
    plt.figure(figsize=(10, 6))

    # read the CSV file using pandas library
    df_2 = pd.read_csv("global-energy-investment.csv",
                       skiprows=(0, 1, 2))

    # define total number of pillars to draw on bar graph
    number = 9
    outout = np.arange(number)
    width = 0.30

    plt.bar(outout, df_2["Clean energy"],
            width=width, color='r',
            label='Clean energy', edgecolor='black')
    plt.bar(outout + width, df_2["Fossil fuels"],
            width=width,  color='y',
            label='Fossil fuels', edgecolor='black')

    # xticks for giving the value of x axis
    labels = np.arange(2015, 2024)
    plt.xticks(outout, labels, rotation='horizontal')

    # labelling for x and y axis
    plt.xlabel("Year")
    plt.ylabel("billion USD (2022)")

    # to give title
    plt.title("Global energy investment [2015-2023]")

    # to save figure
    plt.savefig("bargraph.png")

    plt.legend()


# funtion calling
# to generate the essential value of x and y
new_mortality_rate = initial_operation()

# to generate linechart
generate_linechart(new_mortality_rate)

# to generate pie chart
generate_piechart(new_mortality_rate)

# to generate pie chart
generate_barchart()

plt.show()
