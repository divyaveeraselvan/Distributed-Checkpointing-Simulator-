# Checkpoint Simulator

A lightweight Python simulation script designed to model and test checkpointing mechanisms, state saving, and recovery workflows.

## Features

- **State Management**: Simulates periodic state saving during long-running tasks.
- **Failure Simulation**: Allows testing process recovery by injecting artificial failures.
- **Resume & Restore**: Reads saved checkpoint states to resume operations seamlessly from the last successful checkpoint.

## Requirements

- Python 3.8+

## Usage

Run the simulator directly using Python:

```bash
python checkpoint_simulator.py
```

### Configuration

You can adjust parameters inside `checkpoint_simulator.py`:
- `TOTAL_STEPS`: Number of total steps in the task.
- `CHECKPOINT_INTERVAL`: How frequently (in steps) to save state.
- `FAIL_AT_STEP`: Optional step number to trigger a simulated failure.