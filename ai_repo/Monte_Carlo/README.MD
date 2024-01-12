Running the python file unchanged lets a human play a game of connect 4 with an AI. 

The AI finds the best moves using the Monte Carlo search method.

```
position - Board state
N - Games simulated
player - 'X' or 'O'
```


* The Monte Carlo search method takes the current position, N and player as input. 
* The playable valid moves are saved. 
* In the simulation it plays the first valid move.
* After that it plays random moves for both sides until the end of the game. It does this N times.
* If N number of games is played it saves the won games amount for that specific starting move.
* Then it starts the simulation again with the next valid move N times.
* The starting valid move with the most amount of wins is then returned from the function.

```
# AI simulates 200 games with every possible valid move
N = 200
pos.move = pure_mc(pos, 'O', N)
```

N is directly related to the time the algorithm takes to return the best move.
At the end of the game the number of valid moves decreases, this means that the
algorithm also picks up speed and returns the best move faster.
But a bigger N value also ensures that the move Monte Carlo algorithm returns is actually
better. Bigger N value ==  Better move

At N == 100 I could not beat the AI anymore. Im not the best connect 4 player ;(

I also tested the algorithm by letting 2 AI's play with eachother.

Different N values:
In this example Player 'O' won 10/10 times because it has a bigger N
```
# Player 'X'
pos.move = pure_mc(pos, 'X', 50)
# Player 'O'
pos.move = pure_mc(pos, 'O', 200)
```

Equal N values:
In this example Player 'O' won 6/10 times
```
# Player 'X'
pos.move = pure_mc(pos, 'X', 200)
# Player 'O'
pos.move = pure_mc(pos, 'O', 200)
```
Instead of letting the AIs play 1000 instead of 10 the winning percentage would be very close to 50%

The outputs of the games played human vs AI and also AI vs AI are found in the.txt files.
