# CMPSC 202 - Midterm Programming Assignment

Name: *Your Name Here*

**Instructions**: Complete the exercise below. Open book, open notes, any tools allowed (except submitting another student's work). Due tonight (10/6) at 11:59pm.

**Submission**: Fork this repository as a private repository and invite your professor (username: bcmullins) to the repository. To submit, push your code to your forked repository. Make sure to include your name in the README file.

You have been provided with a starter Python file (`midterm_starter.py`). This file contains two fully implemented algorithms that solve the exact same problem: finding if an array contains duplicate values.

The file also contains a `flawed_benchmark()` function. The developer who wrote this benchmark made several severe methodological errors, making the printed timing results completely unreliable for comparing the asymptotic growth of these two algorithms.

**Your tasks**: 

1. Rewrite the `flawed_benchmark()` function to provide a robust empirical comparison of the two algorithms. List the methodological errors in the original benchmark and explain how you fixed them. Your benchmark should demonstrate the scaling behavior of the two algorithms across multiple input sizes.

*list your methodological errors and fixes here*

- Problem: code uses time.time instead of time.pref_counter which is design for performance tests.
    fix: changed time.time to time.pref_counter

- problem: code uses 2 different data sets
    fix: made both tests use the same data set

- problem: code only tests 1, n input
    fix: created a series of test of various n ranges of size n, as the functions are designed to check for 2 of the same value, so incresaing the range of values will result in better test cases.

- problem: mimuium value of number inserted into data is determined by the size of n
    fix: created a new min value to seperate it from the length of elements.

- problem: each test only runs 1 time.
    fix: run the same multiple times and take the average to esnure noise elmination

- problem: if the array doesnt have a match, it will cause an outlier in the data as it checks every possible element.
    fix: record that and graph it differently.

2. Run the empirical comparion and plot the results using a plotting library of your choice (e.g., `matplotlib`, `seaborn`, etc.). Include the plot in your submission called `results.png`. Be sure to label your axes and include a legend.



