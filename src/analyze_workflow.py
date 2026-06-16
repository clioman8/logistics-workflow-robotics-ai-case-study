"""
Generate a synthetic warehouse event log for the Logistics Workflow & Robotics AI Field Practice Project.

This script creates synthetic data only. It does not use real warehouse records,
resumes, phone numbers, addresses, or private training materials.
"""

from pathlib import Path
import random
from datetime import datetime, timedelta
import pandas as pd

def generate_synthetic_event_log(case_count=180, seed=42):
    random.seed(seed)
    item_categories = ["apparel", "household_goods", "food", "cosmetics", "mixed_goods"]
    base_activities = [
        "Pick List Received",
        "Location Search",
        "Item Picking",
        "Barcode Scan",
        "Product Sorting",
        "Inspection",
        "Packing",
        "Loading Support",
        "Daily Report",
    ]
    stations = {
        "Pick List Received": "Admin",
        "Location Search": "A",
        "Item Picking": "A",
        "Barcode Scan": "B",
        "Product Sorting": "C",
        "Inspection": "D",
        "Packing": "E",
        "Loading Support": "F",
        "Daily Report": "Admin",
    }
    actor_roles = {
        "Pick List Received": "admin_operator",
        "Location Search": "warehouse_operator",
        "Item Picking": "warehouse_operator",
        "Barcode Scan": "scan_operator",
        "Product Sorting": "sort_operator",
        "Inspection": "inspection_operator",
        "Packing": "packing_operator",
        "Loading Support": "loading_support",
        "Daily Report": "admin_operator",
    }
    robotics_ai_touchpoints = {
        "Pick List Received": "workflow_dashboard",
        "Location Search": "AMR_route_support",
        "Item Picking": "robotic_picking_support",
        "Barcode Scan": "barcode_ocr_verification",
        "Product Sorting": "automated_sorting",
        "Inspection": "vision_based_inspection",
        "Packing": "packing_assist",
        "Loading Support": "AMR_AGV_transport",
        "Daily Report": "operational_intelligence_report",
    }
    exceptions = ["", "label_mismatch", "scan_failure", "quantity_mismatch", "damaged_packaging", "wrong_location", "missing_item", "station_congestion", "safety_delay"]
    rows = []
    start = datetime(2024, 1, 3, 8, 30)

    for idx in range(1, case_count + 1):
        case_id = f"ORD-{idx:04d}"
        category = random.choice(item_categories)
        order_type = random.choices(["outbound", "return", "transfer"], weights=[0.72, 0.18, 0.10], k=1)[0]
        shift = random.choice(["morning", "afternoon", "night"])
        quantity = random.randint(1, 36)
        scan_method = random.choice(["handheld_scanner", "pda_terminal", "fixed_scanner"])
        current_time = start + timedelta(days=random.randint(0, 65), hours=random.randint(0, 10), minutes=random.randint(0, 50))

        for activity in base_activities:
            current_time += timedelta(minutes=random.randint(2, 25))
            exception_type = ""
            status = "completed"
            delay_minutes = 0

            if activity in ["Barcode Scan", "Product Sorting", "Inspection", "Packing", "Loading Support"] and random.random() < 0.18:
                exception_type = random.choice(exceptions[1:])
                status = random.choice(["exception", "rework"])
                delay_minutes = random.randint(5, 60)

            rows.append({
                "case_id": case_id,
                "timestamp": current_time.strftime("%Y-%m-%d %H:%M"),
                "activity": activity,
                "actor_role": actor_roles[activity],
                "item_category": category,
                "order_type": order_type,
                "quantity": quantity,
                "station": stations[activity],
                "shift": shift,
                "scan_method": scan_method,
                "status": status,
                "exception_type": exception_type,
                "delay_minutes": delay_minutes,
                "robotics_ai_touchpoint": robotics_ai_touchpoints[activity],
                "data_origin": "synthetic",
            })

    return pd.DataFrame(rows).sort_values(["case_id", "timestamp"]).reset_index(drop=True)

if __name__ == "__main__":
    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)
    df = generate_synthetic_event_log()
    df.to_csv(output_dir / "synthetic_warehouse_event_log.csv", index=False)
    print(f"Generated {len(df)} synthetic events.")
