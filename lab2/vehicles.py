import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
	# Original Data
	df = pd.read_csv('./vehicles.csv')

	# New Split Tables
	newDFCurrent = df.copy()
	newDFProposed = df.copy()
	newDFCurrent.drop(['MPG of Proposed Fleet'], axis = 1, inplace = True)
	newDFProposed.drop(['MPG of Current Fleet'], axis = 1, inplace = True)

	# Drop Incomplete Data Rows from OG Data
	df.dropna(how='any', inplace=True)
	newDFCurrent.dropna(how='any', inplace=True)
	newDFProposed.dropna(how='any', inplace=True)
	#df.fillna(0, inplace=True)

	# Print for Testing Data
	print((df.columns))
	print((newDFCurrent.columns))
	print((newDFProposed.columns))
	print((newDFCurrent))
	print((newDFProposed))

	# Add incrementing columns to new datafiles.
	newDFCurrent.insert(0, 'Car_Number', range(0, 0+len(newDFCurrent)))
	print((newDFCurrent))
	newDFProposed.insert(0, 'Car_Number', range(0, 0+len(newDFProposed)))
	print((newDFProposed))

	# Begin SNS Plotting
	# OG DATA PLOT
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)
	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)
	sns_plot.savefig("scaterplot.png",bbox_inches='tight')
	sns_plot.savefig("scaterplot.pdf",bbox_inches='tight')
	data = df.values.T[1]
	print(("\nORIGINAL VEHICLE FLEET DATA"))
	print((("Mean: %f")%(np.mean(data))))
	print((("Median: %f")%(np.median(data))))
	print((("Var: %f")%(np.var(data))))
	print((("std: %f")%(np.std(data))))
	print((("MAD: %f")%(mad(data))))
	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()
	axes = plt.gca()
	axes.set_xlabel('MPG of Current Car') 
	axes.set_ylabel('MPG of Proposed Car')
	sns_plot2.savefig("histogram.png",bbox_inches='tight')
	sns_plot2.savefig("histogram.pdf",bbox_inches='tight')

	# CURRENT VEHICLES DATA PLOT
	sns_plot = sns.lmplot(newDFCurrent.columns[0], newDFCurrent.columns[1], data=newDFCurrent, fit_reg=False)
	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)
	sns_plot.savefig("scaterplotCurr.png",bbox_inches='tight')
	sns_plot.savefig("scaterplotCurr.pdf",bbox_inches='tight')
	data = newDFCurrent.values.T[1]
	print(("\nCURRENT VEHICLE FLEET DATA"))
	print((("Mean: %f")%(np.mean(data))))
	print((("Median: %f")%(np.median(data))))
	print((("Var: %f")%(np.var(data))))
	print((("std: %f")%(np.std(data))))
	print((("MAD: %f")%(mad(data))))
	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()
	axes = plt.gca()
	axes.set_xlabel('Current Models of Fleet') 
	axes.set_ylabel('MPG of Current Fleet')
	sns_plot2.savefig("histogramCurr.png",bbox_inches='tight')
	sns_plot2.savefig("histogramCurr.pdf",bbox_inches='tight')

	# PROPOSED VEHICLES DATA PLOT
	sns_plot = sns.lmplot(newDFProposed.columns[0], newDFProposed.columns[1], data=newDFProposed, fit_reg=False)
	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)
	sns_plot.savefig("scaterplotPro.png",bbox_inches='tight')
	sns_plot.savefig("scaterplotPro.pdf",bbox_inches='tight')
	data = newDFProposed.values.T[1]
	print(("\nPROPOSED VEHICLE FLEET DATA"))
	print((("Mean: %f")%(np.mean(data))))
	print((("Median: %f")%(np.median(data))))
	print((("Var: %f")%(np.var(data))))
	print((("std: %f")%(np.std(data))))
	print((("MAD: %f")%(mad(data))))
	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()
	axes = plt.gca()
	axes.set_xlabel('Proposed Models of Fleet') 
	axes.set_ylabel('MPG of Proposed Fleet')
	sns_plot2.savefig("histogramPro.png",bbox_inches='tight')
	sns_plot2.savefig("histogramPro.pdf",bbox_inches='tight')



	
