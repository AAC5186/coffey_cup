import argparse
import scipy.stats as stats
import numpy as np

# Parsearg arguments to set things up so user input is defined and able to be used
#	a. Alpha (--alpha; default = 0.05)
#	b. Effect size (--effect; no default; necessary)
#	c. Desired power (--power; default = 0.8)
#	d. Sample size (--n; default=None)

parser = argparse.ArgumentParser(
	description="This program allows the user to specify the expected effect size and/or the alpha (--alpha, default = 0.05) and desired power (--power, default = 0.8) for a one-way ANOVA analysis on three groups. The program simulates data to calculate the number of subjects needed per group to achieve the desired power. The user can also input the expected effect size and the sample size per group (--n). In this case, the program will calculate the power of this experiment.",
)
parser.add_argument(
	"--alpha",
	type = float,
	default = 0.05,
	dest = "alpha",
	help = "The probability of rejecting the null hypothesis when the null hypothesis is true",
)
parser.add_argument(
	"effect",
	type = float,
	help = "The size of the smallest effect that would be biologically meaningful",
)
parser.add_argument(
	"--power",
	type = float,
	default = 0.8,
	dest = "power",
	help = "The probability of rejecting the null hypothesis when the null hypothesis is false",
)
parser.add_argument(
	"--n",
	type = int,
	dest = "n",
	default = None,
	help="The sample size per group",
)
args = parser.parse_args( )

# Generate random numbers from normal distributions with means differing by the effect size to populate 3 lists (for 3 groups)
def simulate(n):
	args2 = (args.effect) * 2
	control = np.random.normal(0,1,n)
	lst2 = np.random.normal(args.effect,1,n)
	lst3 = np.random.normal(args2,1,n)
	return control, lst2, lst3

#Run a one-way ANOVA
def run_anova(list1,list2,list3):
	f_val, p_val = stats.f_oneway(list1,list2,list3)
	if p_val < args.alpha:
		return 1
	else:
		return 0

# Repeat 100 times
def repeat_analysis(n):
	g = 0
	sigresults = 0
	for i in range(100):
		list1,list2,list3 = simulate(n)
		result = run_anova(list1,list2,list3)
		sigresults += result
	return sigresults

# Calculate the proportion of trials that was statistically significant (p<alpha) and compare with --power, repeat with increasing sample size until result >= --power
def power_analysis():
	samplesize = 2
	pwr = 0
	while pwr < args.power:
		sigresults = repeat_analysis(samplesize) #the problem is here
		pwr = sigresults/100
		if pwr < args.power:
			print("A sample size of {0} per group yields a power of {1}".format(samplesize,pwr))
			samplesize = samplesize + 1
		else:
			print("Using alpha = {0} with an expected effect size of {1}, a sample size of {2} per group is necessary to achieve a power of {3}".format(args.alpha,args.effect,samplesize,pwr))

#If the n is specified, calculate the power of the experiment
#If n is not specified, calculate the necessary n per group to get the desired power
if args.n:
	sigresults = repeat_analysis(args.n)
	pwr = sigresults/100
	print("Using alpha = {0} with an expected effect size of {1} and {2} subjects per group, this experiment has a power of {3}".format(args.alpha,args.effect,args.n,pwr))
else:
	power_analysis()
