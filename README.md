# chess-bedex
Example provider for [BEDEX](https://www.bayesesports.com/bedex). Generates valid BayesMessageEnvelopes for simulated chess games between two Stockfish players. Will continuously run games until stopped.

# Payload of BayesMessageEnvelope
* **msg_type**: (string) Message type, either `"GAMESTATE"` or `"GAME_END"`

Then, based on the `msg_type` there are additional fields defined below:

For GAME_END
--------------------
* **winner**:  (string) `"WHITE"` or `"BLACK"` or `"DRAW"`

For GAMESTATES:
-----------------------
* **current_move_number**: (int) one-indexed half-move number. Example: `12`.
* **player_to_move**: (string) which player to move next, `"WHITE"` or `"BLACK"`
* **previous_move**: (string) 	UCI-compatible long algebraic notation of the move which happened most recently (to arrive in this state). Example: `f3e2`
* **board_state**: (string) FEN (Forsyth–Edwards Notation) of the current board state. Example: `"rn1qr1
k1/p1p2ppp/1p3n2/2Pp4/1b1P2b1/2NBBN2/PP3PPP/R2Q1RK1 w - - 2 11"`


# Docker
Build with `docker build -t chess_bedex:latest .`

Run with `docker run chess_bedex:latest`