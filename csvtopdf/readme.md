This script converts CSV file into PDF

The main variables in the code are:
	Dataframe - first column is str, all other are float
	Date (string)
	Title (string)
	Company logo (image/jpeg)

You can find example input and output of script as:
input.csv
output.pdf


Width of all columns is equal.
There is no text wrapping in table titles - only 1 row for title.
You should use reasonable number of columns and avoid extra long titles.
Otherwise text will be overlapped.


What columns do you want to color?
I colored third row as in example with next conditions
 >= 1 = green
 <  1 = red
If you need more columns to be colored you can add neccesary condition in script as in my example (Line 76)


Output of what columns should be formated?
Now, columns 6-10 formated as 6 signs after 0 as in your example.
And column 3 have 0 signs.
You can specify it in script. (Line 83)


You can use any image size, but it will be resized to fixed height = 30mm
If you use image with very high width/height ratio you should change it's position specified in script. (line 26)
