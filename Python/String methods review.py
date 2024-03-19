# Excellent work! This lesson has shown you the vast variety of string methods and their power. Whatever the problem you are trying to solve, if you are working with strings then string methods are likely going to be part of the solution.

# Over this lesson you’ve learned:

# .upper(), .title(), and .lower() adjust the casing of your string.
# .split() takes a string and creates a list of substrings.
# .join() takes a list of strings and creates a string.
# .strip() cleans off whitespace, or other noise from the beginning and end of a string.
# .replace() replaces all instances of a character/string in a string with another character/string.
# .find() searches a string for a character/string and returns the index value that character/string is found at.
# .format() allows you to interpolate a string with variables.
# Well I’ve been stringing you along for long enough, let’s get some more practice in!



highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(',')
highlighted_poems_stripped = []
for i in highlighted_poems_list:
  highlighted_poems_stripped.append(i.strip())
# print(highlighted_poems_stripped)
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
titles =[]
poets =[]
dates = []
for j in highlighted_poems_details:
  titles.append(j[0])
  poets.append(j[1])
  dates.append(j[2])

for i in range(len(titles)): 
  print("The poem {} was published by {} in {}.".format(titles[i], poets[i], dates[i]))