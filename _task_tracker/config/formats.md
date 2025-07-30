# Task Format Specifications

## Required Task Fields

Each task must contain exactly these fields:

```json
{
  "id": 42,
  "name": "Short summary of the task",
  "notes": "Additional details or context",
  "date_added": "2024-01-29",
  "status": "Active",
  "planned_work_day": "Thursday", 
  "category": "Project Management"
}
```

## Field Specifications

### 1. Task ID
- **Type**: Sequential number
- **Generation**: Auto-assigned, increment from highest existing ID
- **Example**: 1, 2, 3, 42, etc.

### 2. Task Name  
- **Type**: String
- **Length**: Keep concise but descriptive
- **Generation**: Auto-generate from user input if not provided
- **Example**: "Update Heinz project budget"

### 3. Notes
- **Type**: String  
- **Content**: Additional details, context, or specifics
- **Generation**: Extract from user prompt or ask for clarification
- **Example**: "Review Q4 expenses and adjust forecast based on client feedback"

### 4. Date Added
- **Type**: Date string (YYYY-MM-DD format)
- **Generation**: Auto-set to today's date when task is created
- **Example**: "2024-01-29"

### 5. Status
- **Type**: String (exact values only)
- **Options**: 
  - "Active" (default for new tasks)
  - "Complete" 
  - "Recurring"
- **Default**: "Active"

### 6. Planned Work Day
- **Type**: String (exact values only)
- **Options**:
  - "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
  - "Filler" (for flexible timing)
- **Default**: "Filler" if not specified

### 7. Category  
- **Type**: String (exact values only)
- **Options**:
  - "Projects"
  - "Project Management" 
  - "General"
- **Default**: "General" if unclear

## File Storage Format

### Active Tasks
- **File**: `_task_tracker/data/active.json`
- **Structure**: Array of task objects
- **Sorting**: By ID ascending

### Completed Tasks  
- **File**: `_task_tracker/data/completed.json`
- **Structure**: Array of task objects
- **Sorting**: By completion date descending

## Example Complete Task Entry

```json
{
  "id": 15,
  "name": "Send FiberPoint list to Thistle client", 
  "notes": "Include updated pricing and delivery timeline. Follow up if no response in 2 days.",
  "date_added": "2024-01-29",
  "status": "Active",
  "planned_work_day": "Wednesday",
  "category": "Projects"
}
```