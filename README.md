# Text-Analysis-Project
 
Please read the [instructions](instructions.md).

Project Overview:
For this project, I decided to do a text analysis on the Manchester United team's Wikipedia page. This would entail me gathering the text from the wiki page via an API and then interpreting that text using various functions and some different imports for public functions. From this project, I was able to learn about the use of APIs and how to use python to dissect the text. 

Implementation:
My implementation consisted of one piece of text with 3 different text analysis moments. After looking through the text options, I decided to go with Wikipedia because of the unique nature of the site. The fact that Wikipedia is a pretty much everything site for information intrigued me and I felt it would produce interesting results.

After choosing the site, I decided to focus on my favorite soccer team, Manchester United. This would allow me to have some background knowledge and prior understanding of what the text was about before python did the interpretation for me. With the interpretation, I would start out pretty simple with a histogram of all the words in the site. I would then move on to producing a short version of all the words in a different histogram. This second histogram got rid of the stopwords present on the site. I found the stopwords list through the NLTK library and imported at into my code. The final segment of my code was the sentiment analysis result.

The sentiment analysis result code came entirely from ChatGPT. This was my experimental code. It was a neat result as it was the first real interpretation of the text. The others were more so pulling out the text but this showed the text read in terms of negativity and positivity. 

![](https://lh4.googleusercontent.com/P7quwmB2y_vB_ocFBpZgNbmu2OE2TodH5T1u9OdFl31v4lwnItAgDgMT-Y1g0clE3WQFEfAjCSj5m3NmgUrQJESRqbz_8ueMR8Vbxhr3f6UhHvrEZo0oAXchjazPlKNacrp8oGDP_dWpLenkPGdm36Q)![](https://lh6.googleusercontent.com/hPROBFZAn1xNGuaV-0FcHXCyGkuC6q0XxyhedAhjjeV99juSzQHRe2nJLB-flFmMnO8hX462WZIrvReNGa7C8oyQCDkHB1k6GxPwukHn9v4nagEV0BCGbK0YKhnhZMK1K5Ze_YxnxjOFdeR-ATwtPk0)

![](https://lh3.googleusercontent.com/_doQy878DEgQ1uL1i2Z72IW4oYX50hbCQnAdvS0sB7zIo7fcHBPtHZkaE-fR_lfRLUcAwEA7zO90_RsvIoluEeMtxyVOKwlTqd4wPYi_--2rXdCrFbgu72tlNcZhj-bA1cn46n-OaSurOKX9pHKZYck)

Results:
When looking at the results of my code the text produced was rather neutral in tone, very focused, and analytical. These three results came from the 3 different functions that I ran on my text. 

Before starting my analysis, I had background knowledge of Manchester United as a team and Wikipedia as a website. Although I had not spent much time on the specific Manchester United Wikipedia site. So I was able to pre-assume what the results would be and I was not far off. Before running the word frequency analysis and sentiment analysis I figured the text would include a lot of soccer-based wording as well as winning words. Secondly, I imagined that the text would not include any extreme weight toward the positive or negative side. 

My projections were partially correct. They were mostly correct when it came to word repetition. Words like, "champion", "league", "player", and "team" were very common compared to the total variety of words mentioned on the site page. This was proven in the two histograms that I produced. however, when I saw the sentiment analysis, I was a bit surprised to see the percentage of text that was positive. The results show that 16% of the text was positive and I figured that was a little high for an informational piece. Although this could be because anyone is allowed to edit Wikipedia and some bias may be seen in the text. 

Reflection:
I felt that I did especially well when it comes to planning and structuring my code. Having started by reading the whole assignment and planning out in steps what I might do before actually doing it, I was able to make my code flow well. This makes for an easy-to-read and digest output that is more pleasant for the reader.

I was also surprised at how much code I was able to write on my own and through googles advice. In the past, I have jumped to ChatGPT a little bit too quickly for my coding. This time I tried to do it myself with either my past notes or sites like Stackabuse for help. This made me code out more than I would have if I had just used ChatGPT. In the end, I only needed ChatGPT for two small fixes in my code. Then I did use it for the last function but that was suggested in the assignment.

To succeed in a quicker way or more efficient manner I would have liked to have known a bit more about text analysis beyond a coder's outlook. I wasn't familiar with text analysis until now.