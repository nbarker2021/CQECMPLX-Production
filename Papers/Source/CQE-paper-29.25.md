# Paper 29.25 - Monster Horizon Toolkit Supplement

## Purpose

This supplement shows how to reproduce Paper 29's Monster/energy-bound
quarantine. The proof is in Paper 29 and its formal verifier. The toolkit is a
reader aid for checking which rows are closed and which rows remain horizon
hypotheses.

## Digital Route

Run:

`python production/formal-papers/CQE-paper-29/verify_monster_energy_bound_hypotheses.py`

The expected status is `pass_with_quarantined_hypotheses`. The verifier checks
`47*59*71 = 196883`, checks `196884 = 1 + 196883`, verifies the finite VOA
partition `Z(q) = 2q^0 + 6q^5`, and confirms that all physical energy-bound
readings remain unwitnessed.

## Analog Route

Place three factor cards labeled `47`, `59`, and `71`. Multiply them into a
single binding card labeled `196883`. Add a separate observer bead labeled
`1`, then write `196884` on the combined McKay card.

Lay out eight chart-state cards. Mark `(0,0,0)` and `(1,1,1)` as weight 0.
Mark the other six cards as weight 5. The white-thread result is
`Z(q) = 2q^0 + 6q^5`.

Now place black tags on three attempted promotions: "weight 5 is physical
energy", "196883 is a universal ceiling", and "Pariah closure is a physical
law". Leave those strings loose until a witness function exists.

## Hidden-Guess Diagnostic

Training mode should hide the label until after the reviewer chooses one:

- closed arithmetic row,
- closed finite VOA partition row,
- valid energy analog,
- invalid physical-energy promotion,
- invalid universal-ceiling promotion,
- invalid physical-boundary promotion,
- open horizon obligation.

The answer key distinguishes replayable finite evidence from unwitnessed
physical interpretation.
