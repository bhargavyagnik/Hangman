# Hangman
A  fully functional Python Game of Hangman

![enter image description here](https://github.com/bhargavyagnik/Hangman/blob/main/img/load.jpg?raw=true)

Algorithm 
```
1. Initialize chance = max_chances
2. read the words
3. Randomly select a word and convert letters  into list
4. if chances > 0 continue step 5 else goto step 11.
5. Print underscores for unknown letter
6. Get input letter 
7. If letter is null or is not a  single letter or is a number go to step 4
8. If letter is one  of the word
9. Append it to list of known letters
10. Else reduce chance and print part of hangman
11. If chance is 0, exit as Game over
12. If there is no unknown letter, Player guessed the word
13. GO to step 4.
15. Finish


```
