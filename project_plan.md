Minesweeper GUI

Data Source: 
- initial board setup will generate a grid of cells where some randomly have mines and others do not
- some information from user input (ex. size of the board or difficulty can determine number of mines placed)

Data Storage:
- board will be stored in a 2D list with each element representing a cell
- each cell will keep track of 1) if the cell contains a mine, 2) number of mines adjacent, 3) status (has the cell been clicked or flagged)
- keep track of the game itself (ex. number of cells remaining, number of mines left to be flagged, has the user won/lost)

Data Utilization:
- board is initialized and filled with mines at the beginning of the grid
- number of adjacent mines for each cell is calculated and stored
- during the game, a user will click on/flag a cell, and the code will check the data stored for that cell to determine the outcome
- throughout the game, the code will check if all non-mine-cells have been revealed, or if all mines have been flagged
- if the player wins/loses, game status is updated and board is revealed
