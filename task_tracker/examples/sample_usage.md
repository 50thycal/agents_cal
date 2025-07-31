# Sample Usage Examples

## Adding Tasks

### Example 1: Project Task with Specific Day
**User**: "Add a task to update the Heinz project budget on Thursday"

**Expected Result**:
```json
{
  "id": 1,
  "name": "Update Heinz project budget",
  "notes": "",
  "date_added": "2024-01-29",
  "status": "Active",
  "planned_work_day": "Thursday",
  "category": "Project Management"
}
```

### Example 2: General Task with Details
**User**: "I need to schedule a 1:1 with Isaiah for sometime this week"

**Expected Result**:
```json
{
  "id": 2,
  "name": "Schedule 1:1 with Isaiah",
  "notes": "Meeting for sometime this week",
  "date_added": "2024-01-29",
  "status": "Active",
  "planned_work_day": "Filler",
  "category": "General"
}
```

### Example 3: Project Deliverable
**User**: "Remind me to send the FiberPoint list to the Thistle client by Wednesday"

**Expected Result**:
```json
{
  "id": 3,
  "name": "Send FiberPoint list to Thistle client",
  "notes": "Due by Wednesday",
  "date_added": "2024-01-29",
  "status": "Active",
  "planned_work_day": "Wednesday",
  "category": "Projects"
}
```

## Viewing Tasks

### Example 1: Weekly Overview
**User**: "What tasks do I have planned this week?"

**Expected Response**:
```
## This Week's Tasks

**Monday**
- No tasks scheduled

**Tuesday** 
- No tasks scheduled

**Wednesday**
- **Task #3**: Send FiberPoint list to Thistle client
  - Due by Wednesday
  - Category: Projects

**Thursday**
- **Task #1**: Update Heinz project budget
  - Category: Project Management

**Friday**
- No tasks scheduled

**Filler Tasks** (flexible timing)
- **Task #2**: Schedule 1:1 with Isaiah
  - Meeting for sometime this week
  - Category: General
```

### Example 2: Category Filter
**User**: "Show me all my project management tasks"

**Expected Response**:
```
## Project Management Tasks

**Task #1**: Update Heinz project budget
- Planned for: Thursday
- Category: Project Management
```

### Example 3: Specific Day
**User**: "What do I have on Thursday?"

**Expected Response**:
```
## Thursday Tasks

**Task #1**: Update Heinz project budget
- Category: Project Management
```

## Workload Analysis

### Example: Checking Balance
**User**: "Do I need to reprioritize? Is any day overloaded?"

**Expected Response**:
```
## Workload Analysis

**Monday**: 0 tasks
**Tuesday**: 0 tasks  
**Wednesday**: 1 task
**Thursday**: 1 task
**Friday**: 0 tasks
**Filler**: 1 task

**Assessment**: Your workload is well-balanced this week. Consider moving the filler task to Tuesday or Friday to spread work more evenly.

**Suggestions**:
- Task #2 (Schedule 1:1 with Isaiah) could be scheduled for Tuesday
```

## Completing Tasks

### Example: Mark Complete
**User**: "Mark task #1 complete"

**Expected Response**:
```
✅ Marked complete: Task #1: Update Heinz project budget
```

**Result**: Task moves from active.json to completed.json with completion date.

## Adding Notes

### Example: Update Task Details
**User**: "Add this note to task #3: Include updated pricing and delivery timeline"

**Expected Response**:
```
✅ Updated notes for Task #3: Send FiberPoint list to Thistle client
- Notes: Due by Wednesday. Include updated pricing and delivery timeline
```

## Error Handling

### Example: Invalid Task ID
**User**: "Mark task #99 complete"

**Expected Response**:
```
Could not find task #99. Current active tasks are #1, #2, #3
```

### Example: Unclear Request
**User**: "Add something about the thing"

**Expected Response**:
```
Could you clarify what task you'd like to add? For example: "Add a task to [specific action] on [day]" or "Remind me to [specific task]"
```