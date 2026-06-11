# Sidecar Protocol

The CMPLX kernel is a token sidecar. It does not replace the host model. It
adds a repeatable method layer around the host model's current token stream.

## Host Loop

1. Host emits or drafts a token string.
2. Host sends the string to `boot.py`.
3. Kernel returns enriched text, a receipt, and boundary metadata.
4. Host may feed the enriched text back into its own context.
5. Host keeps the receipt as trace memory.

## Minimal CLI Integration

```bash
python kernel/boot.py --stdin --json < host_tokens.txt
```

## Minimal Repository Integration

Clone or copy this folder, then call:

```bash
python boot.py --file path/to/current_work.txt --json
```

## Guess Mode

Default mode is quiet so non-local agents can use the sidecar without reading
training receipts as ordinary task output.

Hidden Guess Result turns on when:

- CLI uses `--training-mode`.
- CLI uses `--local-full-program`.
- Request JSON contains `{"kernel_options": {"training_mode": true}}`.

When training mode is enabled, all non-math diagnostics must use Hidden Guess Result:

1. Hide the local result behind a hash.
2. Make the diagnostic guess first.
3. Reveal the result.
4. Score the guess.
5. Preserve the receipt.

## Adapter Invariant

Every host integration must be expressible through:

- Binary Boundary Adapter: stable bytes, hash, encoding, payload frame.
- Universal Adapter: host handshake and normalized payload contract.
