What is a Nested Loop?
A nested loop is a loop placed inside another loop
for i in range(3):
    for j in range(2):
        print(i, j)
Here:
Outer loop → controls rows
Inner loop → controls columns

Execution Rule (MUST UNDERSTAND)
For each iteration of the outer loop,
the inner loop runs completely.
________________________________________
Step-by-Step Execution (VERY IMPORTANT)
for i in range(2):
    for j in range(3):
        print(i, j)

 
If:
●	Outer runs N times
●	Inner runs M times
👉 Total executions = N × M
Common Beginner Mistake
❌ Assuming both loops run together
❌ Forgetting inner loop resets every time
10.2 LOOP CONTROL FOR PATTERN GENERATION
Patterns are visual representations of logic.
________________________________________
Pattern Thinking Rules
1.	Outer loop → number of rows
2.	Inner loop → number of columns
3.	print() without newline controls layout
4.	print() with newline moves to next row
Example 1: Solid Rectangle
Requirement
* * * *
* * * *
* * * *

________________________________________
Code
for i in range(3):
    for j in range(4):
        print("*", end=" ")
    print()

Explanation
●	Outer loop → 3 rows
●	Inner loop → 4 stars per row
●	end=" " keeps printing on same line
●	Empty print() moves to next line

Example 2: Number Grid
1 2 3
1 2 3



for i in range(2):
    for j in range(1, 4):
        print(j, end=" ")
    print()

Example 3: Row-Based Numbers
1 1 1
2 2 2
3 3 3

for i in range(1, 4):
    for j in range(3):
        print(i, end=" ")
    print()
 
Example–4: COLUMN NUMBER PATTERN
Output
1 2 3
1 2 3
1 2 3

for i in range(3):
    for j in range(1, 4):
        print(j, end=" ")
    print()
Key Insight:

Printing j → column-controlled output
Example–5: CONTINUOUS NUMBERS GRID
Output
1 2 3
4 5 6
7 8 9
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

Why important:
Introduces external counter control.
Example–6: RIGHT ANGLE TRIANGLE (STAR)
Output
*
* *
* * *
* * * *

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
Mental Model:

The inner loop runs i times.
Example–7: INVERTED RIGHT TRIANGLE
Output

* * * *
* * *
* *
*

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

Introduces reverse range logic.

Example–8: NUMBER TRIANGLE
Output
1
1 2
1 2 3
1 2 3 4

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
Example–9: REPEATED NUMBER TRIANGLE
Output
1
2 2
3 3 3
4 4 4 4

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

 






10.3 LAB — PATTERN PRINTING & MINI LOGIC GAMES 
This lab is about doing, not watching.
________________________________________
LAB–1: STAR PYRAMID (HALF)
Output

*
* *
* * *
* * * *
* * * * *

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()



LAB–2: INVERTED NUMBER TRIANGLE
Output

1 2 3 4
1 2 3
1 2
1

for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

LAB–3: MULTIPLICATION GRID
Output
1 2 3
2 4 6
3 6 9

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()


LAB–4: CHECKERBOARD PATTERN
Output
0 1 0
1 0 1
0 1 0

for i in range(3):
    for j in range(3):
        print((i + j) % 2, end=" ")
    print()

Introduces logic inside patterns.

LAB–5: ALPHABET PATTERN
Output
A A A
B B B
C C C

import string

letters = string.ascii_uppercase
+

for i in range(3):
    for j in range(3):
        print(letters[i], end=" ")
    print()


LAB–6: ROW–COLUMN DISPLAY 
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)

for i in range(2):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()

LAB–7: MINI LOGIC GAME — EVEN / ODD GRID
Output
E O E
O E O
E O E

for i in range(3):
    for j in range(3):
        if (i + j) % 2 == 0:
            print("E", end=" ")
        else:
            print("O", end=" ")
    print()

LAB–8: MINI LOGIC GAME — COUNTDOWN GRID
Output
5 4 3
2 1 0

num = 5
for i in range(2):
    for j in range(3):
        print(num, end=" ")
        num -= 1
    print()
10.4 MINI BUILD — QUIZ APP CLI v1 (LOOP BASED)
________________________________________
Build Objective
Build a Quiz App CLI v1 that:
●	Asks multiple questions
●	Uses loops for repetition
●	Uses conditions to check answers
●	
●	Displays final score

Step 1: Define Questions & Answers
questions = [
    "What is the capital of India?",
    "What keyword is used to define a function?",
    "Which loop is used for fixed iterations?"
]

answers = ["delhi", "def", "for"]

Step 2: Initialize Score
score = 0

________________________________________
Step 3: Loop Through Questions
for i in range(len(questions)):
    print("\nQuestion:", questions[i])
    user_answer = input("Your answer: ").lower()

    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")


Step 4: Display Final Score
print("\nQuiz Completed")
print("Your Score:", score, "/", len(questions))

________________________________________
Why This Build Matters
●	Combines loops + conditions
●	Reinforces list traversal
●	Mimics real interview problems
●	Foundation for advanced quiz apps

PRACTICE QUESTIONS (WITH ANSWERS)
________________________________________

🧩 CODING QUESTION 1 — HOLLOW SQUARE PATTERN
Problem
Print a 4×4 hollow square using *.
Expected Output

* * * *
*     *
*     *
* * * *
Hint
●	First row → stars
●	Last row → stars
●	First & last column → stars
Solution
for i in range(4):
    for j in range(4):
        if i == 0 or i == 3 or j == 0 or j == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

🧩 CODING QUESTION 2 — LEFT ALIGNED NUMBER TRIANGLE
Problem
Print the following pattern.
Expected Output
1
2 3
4 5 6
7 8 9 10

Solution
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
🧩 CODING QUESTION 3 — INVERTED NUMBER PYRAMID
Problem
Print numbers in decreasing rows.
Expected Output
1 2 3 4
1 2 3
1 2
1

Solution
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


🧩 CODING QUESTION 4 — ALTERNATE STAR PATTERN
Problem
Print stars only in alternate columns.
Expected Output
*   *   *
*   *   *
*   *   *

Solution
for i in range(3):
    for j in range(5):
        if j % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


🧩 CODING QUESTION 5 — DIAGONAL STAR PATTERN
Problem
Print stars only on the main diagonal.
Expected Output
*      
  *    
    *  
      *

Solution
for i in range(4):
    for j in range(4):
        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


🧩 CODING QUESTION 6 — MULTIPLICATION TABLE GRID (1–5)
Problem
Print multiplication values from 1 to 5.
Expected Output
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25

Solution
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()



🧩 CODING QUESTION 7 — BORDER NUMBER PATTERN
Problem
Print numbers only on the border.
Expected Output
1 1 1 1
1     1
1     1
1 1 1 1

Solution
for i in range(4):
    for j in range(4):
        if i == 0 or i == 3 or j == 0 or j == 3:
            print("1", end=" ")
        else:
            print(" ", end=" ")
    print()

🧩 CODING QUESTION 8 — CHESSBOARD (X/O)
Problem
Print a chessboard pattern using X and O.
Expected Output
X O X O
O X O X
X O X O
O X O X

Solution
for i in range(4):
    for j in range(4):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()
Patterns are not about stars.
They are about control, flow, and conditions.

