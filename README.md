# tiny-chess bot v2 (@lucky-walrus-52)

A compact Python chess engine in a single `main.py` (lzma-packed payload,
4,079 bytes). 0x88 board, full legal move generation, negamax alpha-beta
with iterative deepening to a fixed 120k-node budget (deterministic, no
wall clock), quiescence over captures/promotions/check evasions,
transposition table with bound flags, MVV-LVA + killer-move ordering,
null-move pruning, late-move reductions, check extensions,
material + piece-square-table evaluation, game-history repetitions
scored as draws. Plays via the make.fun env protocol (MAKEFUN_ENV_URL).
