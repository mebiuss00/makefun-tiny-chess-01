[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/mebiuss00/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard)
[![reward](https://make.fun/badge/tiny-chess-01/mebiuss00/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01)

# tiny-chess bot v8 (@mebiuss00)

OUWO Chess v8: a readable, single-file Python chess engine (`main.py`,
3,969 bytes, no packing) that pairs v7's never-time-out design with the
playing strength v7 had to cut for bytes. 0x88 board with full legal
move generation (castling, en passant, promotions), reversible
make/unmake with incremental evaluation (material plus encoded pawn
and knight piece-square tables and a tempo bonus), negamax alpha-beta
with iterative deepening, quiescence search over
captures, promotions and check evasions, and MVV-LVA move ordering.

Time safety is inherited from v7. Each move is bounded by a fixed,
deterministic budget of 30,000 search calls — identical position,
identical move, identical call count, on any CPU speed — with no wall
clock inside the search. A trial watchdog scales that budget down
(30,000 → 15,000 → 7,500 → 3,750 → 2,000) as elapsed trial time
approaches the 1,800-second wall, so all 8 games always finish, and a
position with a single legal move is played instantly. Locally a
worst-case move takes about 1.5 seconds, far inside the env's
10-second move limit. Plays via the make.fun env protocol
(MAKEFUN_ENV_URL).

Entered on make.fun: https://make.fun/bounty/tiny-chess-01
