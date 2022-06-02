Exercises: Python Intro
=======================
Problems for exercises and homework for the [“Python Fundamentals” course @SoftUni](https://softuni.bg/opencourses/python-fundamentals-course).\
You can check your solutions here: [https://judge.softuni.bg/Contests/917](https://judge.softuni.bg/Contests/917).


1.Hello World
-----------
Write a Python program that prints out a simple “**Hello World!**” to get acquainted with writing Python code.

### Examples
| **Input**    | **Output**   |
|--------------|--------------|
| *(no input)* | Hello World! |


2.Person Info
-----------
Write a Python program, which reads a person’s **name**, **age**, **town** and **salary**, and prints it back to the **console** with the **following format**:  
“**{name} is {age} years old, is from {town} and makes \${salary}**”  
*Note: Leave floating point numbers unformatted.*

### Examples
| **Input**            | **Output**                                               |
|----------------------|----------------------------------------------------------|
| Gosho                | Gosho is 20 years old, is from Sofia and makes \$530.0   |
| 20                   |                                                          |
| Sofia                |                                                          |
| 530                  |                                                          |
| **Input**            | **Output**                                               |
| Pesho                | Pesho is 22 years old, is from Plovdiv and makes \$450.0 |
| 22                   |                                                          |
| Plovdiv              |                                                          |
| 450                  |                                                          |

#### Hints
-   To format a string, you can either use the **.format() function**, or a **template string** (**f"format"**)


3.Extended Person Info
--------------------

Write a Python program, which reads information about a **person** in the **same format** as the previous problem.

The **age range** is as follows:
-   If the person is **less than 18** years old, they are a “**teen**”
-   If the person is **less than 70** years old, they are an “**adult**”
-   Otherwise, the person is an “**elder**”

The **salary range** is as follows:
-   If the salary is **less than \$500**, it is “**low**”
-   If the salary is **less than \$2000**, it is “**medium**”
-   Otherwise, the salary is “**high**”  
NOTE: Format the **salary** to the **2nd decimal point**.

### Examples
| **Input**             | **Output**                                    |
|-----------------------|-----------------------------------------------|
| Gosho                 | Name: Gosho                                   |
| 20                    | Age: 20                                       |
| Sofia                 | Town: Sofia                                   |
| 530                   | Salary: \$530.00                              |
|                       | Age range: adult                              |
|                       | Salary range: medium                          |
| **Input**             | **Output**                                    |
| Ivan                  | Name: Ivan                                    |
| 77                    | Age: 77                                       |
| Montana               | Town: Montana                                 |
| 250                   | Salary: \$250.00                              |
|                       | Age range: elder                              |
|                       | Salary range: low                             |


4.Numbers from 1 to 10
--------------------

Write a simple **for loop**, with which to print all the **numbers from 1 to 10 on separatelines**.  
Use the **range()** function.

### Examples
| **Input**    | **Output**           |
|--------------|----------------------|
| *(no input)* | 1                    |
|              | 2                    |
|              | 3                    |
|              | 4                    |
|              | 5                    |
|              | 6                    |
|              | 7                    |
|              | 8                    |
|              | 9                    |
|              | 10                   |

### Hints
-   The **range()** function generates an **exclusive range**, so using **10** as an **end value** probably won’t work.


5.Numbers with Step
-----------------
Write a python program, which receives a **start number**, an **end number** and a **step**. Write a simple **for loop**, which prints all the numbers from the **start number** to the **end number**, using the **specified step**. Print the numbers on **separate lines**.  
Use the **range()** function.

### Examples
| **Input** | **Output**        |   | **Input** | **Output**                                    
|-----------|-------------------|---|-----------|-------------------------|
| 1         | 1                 |   | -20       | -20                     |
| 10        | 2                 |   | 4         | -18                     |
| 1         | 3                 |   | 2         | -16                     |
|           | 4                 |   |           | -14                     |     
|           | 5                 |   |           | -12                     | 
|           | 6                 |   |           | -10                     |  
|           | 7                 |   |           | -8                      |  
|           | 8                 |   |           | -6                      |  
|           | 9                 |   |           | -4                      |
|           |                   |   |           | -2                      |
|           |                   |   |           | 0                       |
|           |                   |   |           | 2                       |
