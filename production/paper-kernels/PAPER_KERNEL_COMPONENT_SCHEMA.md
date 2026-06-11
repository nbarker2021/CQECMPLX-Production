# Paper Kernel Component Schema

Every CQECMPLX paper kernel has exactly eight required components.

1. **Claims** (`claims`)
2. **Math** (`math`)
3. **Formal, Normal, Closed-Form Algebra and Calculus** (`formal_algebra_calculus`)
4. **By-Hand Reconstruction** (`hand_work`)
5. **Code Rebuild** (`code_rebuild`)
6. **Installable Lib Bindings** (`lib_bindings`)
7. **Tests and Receipts** (`tests_and_receipts`)
8. **Deployment Kernel** (`deployment_kernel`)

Validation rule: any diagnostic, validation, or test that is not purely math-based must support the hidden-guess honesty layer when training mode is enabled. The guess is made before the answer/reconciliation layer is revealed.
