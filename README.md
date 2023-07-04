# WordleConsole

Wordle is a console game implemented in Python where you have to guess a secret word within a limited number of attempts. The objective is to uncover the hidden word by guessing individual letters and receiving feedback on whether the guessed letters are in the correct position or not.

The Python implementation I provided is a basic version of the Wordle game in the console. In the code, a word is randomly selected from a predefined list, and the player needs to guess letters. The current state of the game, including the hidden word with underscores for the yet-to-be-guessed letters and the remaining attempts, is displayed.

The player enters a letter, and the program checks if it is in the secret word. If it is, all occurrences of the letter in the hidden word are revealed. If the letter is not in the secret word, the remaining attempts are decreased. The game continues until the player guesses all the letters or runs out of attempts.

The goal is to guess the secret word before running out of attempts. You can customize the list of words to make the game more interesting.

Keep in mind that this is a basic implementation, and additional features can be added, such as displaying the already guessed letters or allowing the player to enter the complete word instead of one letter at a time.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



MIT License

Copyright (c) 2022 Martín José Imoberdorf

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
