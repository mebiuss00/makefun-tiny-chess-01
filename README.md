[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/mebiuss00/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard)
[![reward](https://make.fun/badge/tiny-chess-01/mebiuss00/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01)

# tiny-chess bot v7 (@mebiuss00)

OUWO Chess v7: a readable, single-file Python chess engine (`main.py`,
4,043 bytes, no packing) built to never lose on time. 0x88 board with
full legal move generation (castling, en passant, promotions), negamax
alpha-beta search with iterative deepening, snapshot make/unmake, and
an incremental evaluation (material, pawn advancement, piece
centrality, king corner bonus, tempo).

Time safety is the design point. Each move is bounded by a fixed,
deterministic budget of 14,000 search calls — identical position,
identical move, identical call count, on any CPU speed. A trial
watchdog scales that budget down (14,000 → 7,000 → 3,500 → 1,750 →
2,000) as elapsed trial time approaches the 1,800-second wall, so all
8 games always finish, and a position with a single legal move is
played instantly. Locally a worst-case move takes about 1.2 seconds,
far inside the env's 10-second move limit. Plays via the make.fun env
protocol (MAKEFUN_ENV_URL).

Entered on make.fun: https://make.fun/bounty/tiny-chess-01
