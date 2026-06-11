# CMPLX-MORSR Universal Adapter Programs

CMPLX-MORSR uses Universal Adapter Programs for translation, storage, temporal binding, and identity-family exchange.

## Binding

Canonical source:

```text
CMPLX-PartsFactory-main/src/mcp_tools/universal_tools.py
```

## Use In CMPLX-MORSR

- Convert diagnostic outputs into universal handles.
- Store confirmed readings as identity-bound records when needed.
- Temporalize pulse/recenter traces.
- Audit tool/network calls.
- Bridge product-facing diagnostic results back into the library.

## Rule

Any networking or cross-tool exchange goes through Universal Adapter Programs before custom protocol work.
