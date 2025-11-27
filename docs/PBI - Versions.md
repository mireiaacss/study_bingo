  
PRODUCT BACKLOG VERSION 1

1\. Define and set up the project structure (folders, files, documentation, dependencies). 

2\. Create an initial number dataset. 

3\. Build bingo card generation logic. 

4\. Implement random number drawing each round. 

5\. Enable players to mark answers on their cards. 

6\. Validate correctness of marked answers. 

7\. Detect winning bingo patterns. 

8\. Create the final trivia dataset. 

9\. Implement the final dataset replacing the numbers. 

10\. Verify correctness when a player declares bingo. 

11\. Handle invalid win declarations. 

12\. Track incorrect answers for later review. 

13\. Write unit tests for core functionality. 

14\. Document gameplay rules and setup instructions. 

15\. Provide guide for updating trivia content. 

16\. Ensure overall code quality and maintainability. 

Product backlog version 2:  
\*\*\*the structure is not the final but it was our guide during sprint 2\. We changed later for understanding and clarity

| \#  | User Story  | Product Backlog  |
| :---- | ----- | ----- |
| PB-01  | As a developer, I want a clean and organized project structure so that the game can be extended easily.  | Define and set up the project structure (folders, files, documentation, dependencies).  |
| PB-02  | As a player, I want to see a bingo card when the game starts so that I can begin playing immediately.  | Implement the card generation using initial placeholder numbers  |
| PB-03  | As a player, I want the bingo card to use real questions and answers so that I can study while playing.  | Load Q\&A from CSV, fill card with answers, pair questions randomly.  |
| PB-04  | As a player, I want the game to understand coordinates like “A1” or “B3” so that I can mark my answers easily.  | Convert coordinates, validate ranges, support skip & quit  |
| PB-05  | As a player, I want the game to progress question by question so that I can interact with the board.  | Implement the full game flow (ask question → user input → mark or mistake → check win).  |
| PB-06  |  I want to understand what is going on in the game and when I loose | Validate correctness of marked answers.  |
| 7  | As a player, I want the game to automatically detect when I have a winning BINGO  | Detect winning bingo patterns.  |
| 8  |  I want to be able to play a functional game with meaningful questions  | Create the final trivia dataset.  |
| 9  | As a player, I want my bingo card to contain trivia questions from terminal Usage and python basics, so that I can test my knowledge while playing.  | Implement the final dataset replacing the numbers.  |
| 10  | As a player, I want the system to check my winning card to ensure all my answers were correct, so that my victory is legitimate.  | Verify correctness when a player declares bingo.  |
| 11  | As a player, I want to be clearly told why my BINGO declaration was invalid, so that I can understand my mistake.  | Handle invalid win declarations.  |
| 12  | As a player, I want to see which questions I got wrong at the end of the game, so that I can learn from my mistakes and study those topics.  | Track incorrect answers for later review.  |
| 13  |  As a player I want the game to work well | Write unit tests for core functionality.  |
| 14  | As a new player, I want to read clear instructions on how to play the game, so that I can get started quickly and easily.  | Document gameplay rules and setup instructions.  |
| 15  | As a Developer, I want a clear guide on how to add new questions, so that I can keep the game's content fresh and relevant.  | Provide a guide for updating trivia content.  |
| 16  |  As a player I want the game to work without error and smoothly | Ensure overall code quality and maintainability.  |

**Version sprint 3**

| \# | User Story | Description | Acceptance Criteria |
| :---- | :---: | :---: | :---: |
| PB-01 | As a developer, I want a clean and organized project structure so that the game can be extended easily. | Define and set up the project structure (folders, files, documentation, dependencies). | Project root contains: src/, data/, tests/, docs/. Basic python package imports work and README and license exist |
| PB-02 | As a player, I want to see a bingo card when the game starts so that I can begin playing immediately. | Implement the card generation using initial placeholder numbers | Board is generated with unique values and prints successfully in terminal as well as passes all board tests. |
| PB-03 | As a player, I want the bingo card to use real questions and answers so that I can study while playing. | Load Q\&A from CSV, fill card with answers, pair questions randomly. | CSV is read successfully, board displays answers and questions are paired correctly |
| PB-04 | As a player, I want the game to understand coordinates like “A1” or “B3” so that I can mark my answers easily. |  Convert coordinates, validate ranges, support skip & quit | Function that coordinates indices works for A-I and 1-3. Invalid inputs show clear feedback and skip (enter) and quit (q) work. |
| PB-05.1 | As a player, I want the game to progress question by question so that I can interact with the board. |  Implement the full game flow (ask question → user input → mark or mistake → check win). | Game asks questions sequentially, marks X on correct answers, tracks and stops after max mistakes and full bingo is detected |
| PB-05.2 | As a player, i want to receive one question at a time so I can respond without confusion | Prompt one question at a time and output to the player their options for answering | Systems displays one question at a time and the question shown matches the key value pairs. No questions are repeated during game |
| PB-05.3 | As a player, I want correct answers to be marked with an 'X' so that I can visually track my progress | After a coordinate is selected, the game verifies the answer and marks the board with X where chosen | Cells update immediately after marking and board layout stays intact |
| PB-05.4 | As a player I want the game to end when I reach maximum number of mistakes, so the game does not go on wrong forever | Define a maximum number of mistakes and when player reaches this number, the game ends immediately | Game ends when mistake counter reaches maximum and game prints out a message that the player lost. |
| PB-05.5               | As a player I want clear feedback at the end of the game, so I understand what I have done wrong | Implement message for full board win or loss shown in readable and consistent format | Different messages are printed for bingo win, loss by maximum number of mistakes and loss by not completing bingo board |
| PB-05.6 | As a player, I want to learn from my mistakes in the game and understand when I lose and when I input a wrong answer. | Track wrong answers throughout the game and print when I get something wrong | Game stores question, wrong answer and right answer ad print clearly when player loses. |
| PB-06 | As a player, I want to choose the subject I want to practice so that the game can adapt to my study needs. | Add new CSVs and a menu to select the subject | Subject selection prompt works, the correct CSV is loaded and game runs fully in any subject. |
| PB-07 | As a player, I want to see which questions I got wrong at the end so that I can learn from my mistakes. | Track errors and print reviews at the end. | Errors stored as key value pairs and printed clearly in the end. This should work for any subject |
| PB-08 | As a developer, I want the game to run in a Docker container so that anyone can execute it easily. | Deploy in docker by creating a Dockerfile | Dockerfile exists, docker build works and docker run launches the game |

**PB version sprint 4:**

| \# | User Story | Description | Acceptance Criteria |
| :---- | :---: | ----- | :---: |
| PB-01 | As a developer, I want a clean and organized project structure so that the game can be extended easily. | Define and set up the project structure (folders, files, documentation, dependencies). | Project root contains: src/, data/, tests/, docs/. Basic python package imports work and README and license exist |
| PB-02.1 | As a player, I want to see a bingo card when the game starts so that I can begin playing immediately. | Implement the card generation using initial placeholder numbers | Board is generated with unique values and prints successfully in terminal as well as passes all board tests. |
| PB-02.2 | As a player, I want the game to be dynamic and move fast | Make the board a 3x4 size so that the game is fast and dynamic | The board presented on the screen follows a 3x4 format |
| PB-03 | As a player, I want the bingo card to use real questions and answers so that I can study while playing. | Load Q\&A from CSV, fill card with answers, pair questions randomly. | CSV is read successfully, board displays answers and questions are paired correctly |
| PB-04 | As a player, I want the game to understand coordinates like “A1” or “B3” so that I can mark my answers easily. |  Convert coordinates, validate ranges, support skip & quit | Function that coordinates indices works for A-C and 1-3. Invalid inputs show clear feedback and skip (enter) and quit (q) work. |
| PB-05.1 | As a player, I want the game to progress question by question so that I can interact with the board. |  Implement the full game flow (ask question → user input → mark or mistake → check win). | Game asks questions sequentially, marks X on correct answers, tracks and stops after max mistakes and full bingo is detected |
| PB-05.2 | As a player, i want to receive one question at a time so I can respond without confusion | Prompt one question at a time and output to the player their options for answering | Systems displays one question at a time and the question shown matches the key value pairs. No questions are repeated during game |
| PB-05.3 | As a player, I want my answers to be marked with an 'X' so that I can visually track my progress | After a coordinate is selected, the game verifies the answer and marks the board with X where chosen | Cells update immediately after marking and board layout stays intact |
| PB-05.4 | As a player I want the game to end when I reach maximum number of mistakes, so the game does not go on wrong forever | Define a maximum number of mistakes and when player reaches this number, the game ends immediately | Game ends when mistake counter reaches maximum and game prints out a message that the player lost. |
| PB-05.5               | As a player I want clear feedback at the end of the game, so I understand what I have done wrong | Implement message for full board win or loss shown in readable and consistent format | Different messages are printed for bingo win, loss by maximum number of mistakes and loss by not completing bingo board |
| PB-05.6 | As a player, I want to learn from my mistakes in the game and understand when I loose | Track wrong answers throughout the game internally and halt game when 3 is reached.  | Game stores question, wrong answer and right answer ad print clearly when player loses. |
| PB-06.1 | As a player, I want to choose the topics I want to practice so that the game can adapt to my study needs. | Add new CSVs and a menu to select the topics | Topic selection prompt works, the correct CSV is loaded and game runs fully in any topic. |
| PB-06.2 | As a player, I want to be able to upload new csv files if I want to study something else | Make a csv reader function that works for multiple CSVs uploaded In the correct format | Player uploads CSV and the key value pairs are extracted successfully for the game. |
| PB-07 | As a player, I want to see which questions I got wrong at the end so that I can learn from my mistakes. | Track errors and print review at the end. | Errors stored as key value pairs and printed clearly in the end. This should work for any topic. |
| PB-08 | As a player, I want to be prompted if I want to start a new game quickly after finishing so that I do not need to restart the program. | Prompt user if they want to restart game or quit. | Asks "play again?" And restarts the gameplay loop |
| PB-09 | As a developer, I want the game to run in a Docker container so that anyone can execute it easily without dependencies. | Deploy in docker by creating a Dockerfile | Dockerfile exists, docker build works and docker run launches the game |

