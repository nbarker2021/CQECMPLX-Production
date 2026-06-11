from forgefactory_analog_workbench import WorkbenchSimulator

sim = WorkbenchSimulator()
result = sim.run_action(
    action_id="example-001",
    observed_action="Sort a claim into proof or obligation using the analog kit.",
    colors=["red", "green", "blue"],
    continue_here=True,
)
print(result["receipt"])
sim.export("exports/example_run")
