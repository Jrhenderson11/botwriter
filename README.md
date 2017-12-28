# botwriter

This program is a simple attempt to create something similar to the bot writer found at http://botnik.org/content/harry-potter.html

It reads in text and builds up a model using uni/bigrams. Simply:
it creates a recordof the frequencies of which words appear after which and uses this to predict the next word after the current one. It keeps generating words by examining the last (or last 2 for bigrams) until it reaches the word limit. To simplify things puncuation is included with each word.

It is currently set to write sherlock holmes snippets by learning from the file sherlockHolmes.txt which works quite well.
Also provided is big.txt which contains Tolstois War and Peace. Whilst it once generated a fairly funny few sentences about napoleon going inside his own head it doesn't seem to work as well. This is perhaps due to the larger vocabulary and training data meaning there is more choice to the bot at each word (and with more choice less predictability). Also the paragraph breaks are far too commmon.

If you substitute the file loaded with your own example of text it will use that as a model and replicate it. You can also change the amount of text generated easily. Have fun writing the adventures of "Sherlock Holmes and the blackest treachery of the only geese in the south"



