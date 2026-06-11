from forgefactory_analog_workbench.kit import build_eightfold_kit, COLOR_FAMILIES, TOOL_CLASSES
from forgefactory_analog_workbench.simulation import WorkbenchSimulator
from forgefactory_analog_workbench.operators import legal_binding


def test_eightfold_manifest_count():
    m = build_eightfold_kit()
    assert m["object_count"] == len(COLOR_FAMILIES) * len(TOOL_CLASSES) * 8


def test_triadic_binding():
    ok, kind = legal_binding(["red", "green", "blue"])
    assert ok
    assert kind == "triadic_color_binding"


def test_demo_receipt_validates():
    sim = WorkbenchSimulator()
    demo = sim.demo()
    assert demo["receipt_count"] == 1
    assert sim.receipts[0].validate() == []
