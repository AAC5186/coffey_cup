1.	List your name and email address.

NAME: Alissa Coffey
EMAIL: acoffey1@bidmc.harvard.edu
GITHUB URL: https://github.com/AAC5186/coffey_cup

2.	Summarize your experience working on the final project. For example, you might approximate how many hours you spent on it and how those hours were distributed. If you found some aspects considerably harder than others, list those here. If there are known problems with your final project script, list those here.

ANSWER: First, I wrote out each step of the program in English. Then I went through and wrote code for all of it (with the assumption that almost none of it would work). Then I went through troubleshooting one function at a time. I spent a couple of hours researching whether I could run a repeated measures ANOVA in python and trying to run a linear mixed model before ultimately switching to a one-way ANOVA. I spent probably about 45 min reading about effect size to make sure I understood what it actually meant. Once I had a program that worked without a --n keyword, I went back in and coded the option to calculate the power of an experiment with a known sample size. Troubleshooting and researching took the most time, but ultimately it was pretty rewarding to write a program that actually worked that I could use in lab.

3.	In a few sentences, describe what your final project script does.

ANSWER: This program allows the user to specify the expected effect size, alpha (--alpha, default = 0.05), and desired power (--power, default = 0.8) for a one-way ANOVA analysis on three groups. The program simulates data to calculate the number of subjects needed per group to achieve the desired power. The user can also input the expected effect size and the sample size per group (--n). In this case, the program will calculate the power of this experiment.

4.	List any modules (outside of the Python standard library) that are required to execute your final project script. You may answer “N/A” if no such modules are required.

ANSWER: argparse
	scipy.stats
	numpy

5.	Describe your sample INPUT FILE(S). If you are completing a custom final project that does not require an input file, explain that clearly here.

ANSWER: There is no input file. All input is on the command line (specifications for a power analysis: alpha, expected effect size, desired power, sample size). The only required input is the expected effect size.

6.	Provide the command used to produce your sample OUTPUT FILE with flags and arguments specified (e.g. “$ python script_name.py arguments”).

ANSWER: Generic: $ python CoffeyBST273final.py (float for the effect size) --n (int; optional)
	Sample:  $ python CoffeyBST273final.py 0.8
	Sample2: $ python CoffeyBST273final.py 0.8 --n 7
	*Please note that a number for the effect size is required*

7.	Describe your sample OUTPUT FILE(S). If you are completing a custom final project that does not produce an output file, capture the STDOUT of the command specified above and include it here (e.g. “$ command > sample_stdout.txt”).

ANSWER: If calculating the necessary sample size (no --n specified): Each line indicates the power of an experiment with a given n. The program starts with a sample size of 2 per group and increases until the power is greater than or equal to the desired power (default = 0.8)
		See sample_stdout.txt
	If calculating power (--n specified): The program provides the power of an experiment with n subjects per group. It lists the specifications of the power analysis in the output.
		See sample2_stdout.txt

8.	What was your favorite part of learning to program in BST 273 (i.e. something we should definitely NOT change in future incarnations of the course)?

ANSWER: Object-oriented programming. This felt like looking under the hood after spending the course working with the default classes in Python. It also was really helpful for understanding how video games are coded. The live coding exercises were very helpful.  I also liked the homework with all of the DNA examples.

9.	What was your LEAST favorite part of learning to program in BST 273 (i.e. something we should look into changing for future incarnations of the course)?

ANSWER: Something about interacting with the computer at the terminal took a while to click for me. I think more live coding practice might have helped with that. One thing I would like to see included in the class, even briefly, is some discussion of how user interfaces/graphics are created. There's still a bit of a black box in my understanding of how source code produces images on the computer screen.