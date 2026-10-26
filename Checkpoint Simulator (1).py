import json
import time
import os
from typing import Dict, Any

CHECKPOINT_FILE = "checkpoint.json"
TOTAL_STEPS = 10
CHECKPOINT_INTERVAL = 3
FAIL_AT_STEP = 7  # Set to None to run without failure simulation

def load_checkpoint(filepath: str) -> Dict[str, Any]:
    """Loads state from a checkpoint file if it exists."""
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                print(f"[RECOVERY] Found checkpoint at step {data.get('step')}.")
                return data
        except Exception as e:
            print(f"[WARN] Failed to read checkpoint: {e}")
    return {"step": 0, "state_data": {}}

def save_checkpoint(filepath: str, step: int, state_data: Dict[str, Any]) -> None:
    """Saves the current process state to a JSON file."""
    temp_file = f"{filepath}.tmp"
    data = {"step": step, "state_data": state_data, "timestamp": time.time()}
    
    # Write atomically using a temporary file
    with open(temp_file, "w") as f:
        json.dump(data, f, indent=2)
    os.replace(temp_file, filepath)
    print(f"[CHECKPOINT] Saved state at step {step}.")

def run_simulation(fail_step: int = None):
    """Executes the main task loop with checkpointing and optional failure simulation."""
    state = load_checkpoint(CHECKPOINT_FILE)
    start_step = state["step"] + 1

    print(f"[SYSTEM] Starting process execution from step {start_step}...")

    for step in range(start_step, TOTAL_STEPS + 1):
        print(f" -> Processing step {step}/{TOTAL_STEPS}...")
        time.sleep(0.5)  # Simulate work

        # Update dummy state
        state["state_data"]["last_processed"] = step

        # Checkpoint interval trigger
        if step % CHECKPOINT_INTERVAL == 0:
            save_checkpoint(CHECKPOINT_FILE, step, state["state_data"])

        # Simulate unexpected crash/failure
        if step == fail_step:
            print(f"[CRASH] Simulated failure occurred at step {step}!")
            return

    print("[SYSTEM] Task completed successfully!")
    if os.path.exists(CHECKPOINT_FILE):
        os.remove(CHECKPOINT_FILE)
        print("[CLEANUP] Removed checkpoint file upon task completion.")

if __name__ == "__main__":
    print("=== Run 1: Execution with failure ===")
    run_simulation(fail_step=FAIL_AT_STEP)
    
    print("\n=== Run 2: Resuming execution from checkpoint ===")
    run_simulation(fail_step=None)