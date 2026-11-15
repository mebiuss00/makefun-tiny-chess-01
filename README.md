# tiny-chess bot v3 (@mebiuss00)

A compact Python chess engine in a single `main.py` (lzma-packed payload,
4,071 bytes). 0x88 board, full legal move generation, negamax alpha-beta
with iterative deepening to a fixed 130k-node budget (deterministic, no
wall clock), quiescence over captures/promotions/check evasions,
transposition table with bound flags, MVV-LVA move ordering, null-move
pruning, late-move reductions, principal-variation search, and an
incremental material + piece-square evaluation tapered by game phase
(endgame king table) with the bishop pair. Game-history repetitions are
scored as draws. Plays via the make.fun env protocol (MAKEFUN_ENV_URL).

Entered on make.fun: https://make.fun/bounty/tiny-chess-01
