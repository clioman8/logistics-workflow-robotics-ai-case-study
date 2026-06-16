[synthetic_data_explanation.md](https://github.com/user-attachments/files/28987161/synthetic_data_explanation.md)
# Synthetic warehouse event-log dataset

This folder contains synthetic data for the `Logistics Workflow & Robotics AI Field Practice Project`.

## Important note

The files in this folder are fully synthetic. They do not contain real warehouse records, real employee records, real company data, raw resumes, phone numbers, addresses, or private training materials.

The dataset is designed only for portfolio, workflow-analysis, and operational-intelligence demonstration purposes.

## Why synthetic data?

The original case is based on anonymized evidence of logistics-center work experience and robotics AI training. However, real logistics event logs, resumes, training files, and personal records must not be uploaded to GitHub.

Synthetic data allows the project to demonstrate:

- event-log modeling
- logistics workflow analysis
- bottleneck detection
- exception analysis
- human-robot task mapping
- robotics AI touchpoint mapping
- operational intelligence reporting

without exposing private or sensitive information.

## Main file

`synthetic_warehouse_event_log.csv`

Each row represents a synthetic warehouse event.

Core process-mining fields:

- `case_id`: order or workflow instance
- `timestamp`: event time
- `activity`: workflow step
- `actor_role`: anonymized role executing the task
- `item_category`: synthetic item group
- `station`: warehouse station
- `status`: completed, rework, exception, or reviewed
- `exception_type`: synthetic exception label
- `delay_minutes`: synthetic delay caused by the event or exception
- `robotics_ai_touchpoint`: possible robotics/AI support point
- `data_origin`: always `synthetic`

## Related files

- `role_task_matrix.csv`: maps roles to tasks and robotics AI touchpoints.
- `workflow_exception_taxonomy.csv`: explains exception categories and recommended responses.

## Research framing

The synthetic event log is designed for a case-based study of logistics workflow and robotics AI field practice. It connects manual warehouse work such as scanning, sorting, inspection, packing, loading support, and reporting with robotics AI concepts such as AMR/AGV transport, barcode/OCR verification, vision-based inspection, and workflow dashboards.
