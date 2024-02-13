"""
Load Files

👉 Day 49 Challenge
In yesterday's challenge, you created a file called high.score and stored some high scores in it.

We've added a version of that file to this repl.

Your program should:

Read in the data from the high.score file.
Identify which of those users had the highest score. Automatically! (Not you doing it!)
Output the name and score of the winner.
Example:

🌟Current Leader🌟
Analyzing high scores......
Current leader is DJM 898,000

Hints:
Read each element one at a time.
Split each element into two pieces.
You'll have to cast one element as an integer to make it a number.
Think back to list indexing to access the second index for the score.
Use a max_score list to store the details of the high scorer (starting with line 1 from the file, overwrite the details if the current line has a higher score).

"""

import os, time

highScores = []


f = open("high.score", "r")
while True:
    fileContent = f.readline().strip()
    if fileContent == "":
        break
    initials, score = fileContent.split()
    highScores.append([initials, int(score)])

f.close()

highScores.sort(key=lambda e: e[1], reverse=True)

os.system("clear")
print("🌟 Current Leader 🌟")
time.sleep(1)
print("Analyzing high scores......")
time.sleep(1)
print(f"\nCurrent leader is:\n\n🌟 {highScores[0][0]} -> {highScores[0][1]}🌟\n")
time.sleep(1)
print("--- Rest of the table ---")
time.sleep(1)
for i in range(1, len(highScores)):
    print(f"{i + 1}. {highScores[i][0]} -> {highScores[i][1]}")
