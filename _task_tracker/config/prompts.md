# AI Instruction Templates

## Core Behavior

When the user mentions tasks, always:
1. Read the current task files to understand context
2. Follow the organization rules in `organization.md`
3. Use the exact format specified in `formats.md`
4. Update the appropriate JSON files
5. Provide a clear confirmation of what was done

## Adding Tasks

### User Pattern Examples:
- "Add a task to update the Heinz project budget on Thursday"
- "I need to schedule a 1:1 with Isaiah"
- "Remind me to send the FiberPoint list to the Thistle client"

### AI Response Template:
1. **Parse the request** to extract:
   - Task description/name
   - Any specific timing (day of week)
   - Context clues for category
   - Additional details for notes

2. **Generate task data**:
   - Auto-assign next sequential ID
   - Create clear, concise name
   - Set date_added to today
   - Determine category using organization rules
   - Set planned_work_day (or "Filler" if unspecified)
   - Set status to "Active"

3. **Update active.json** by adding the new task

4. **Confirm with user**: 
   "✅ Added Task #[ID]: [Name] 
   - Category: [Category]
   - Planned for: [Day]
   - Notes: [Notes if any]"

## Reviewing Tasks

### User Pattern Examples:
- "What tasks do I have planned this week?"
- "Show me everything for Friday"
- "What are my active project management tasks?"

### AI Response Template:
1. **Read active.json**
2. **Filter/group** based on request:
   - By day: Group Monday through Friday, separate Filler
   - By category: Group Projects, Project Management, General
   - By status: Show only Active, Complete, or Recurring

3. **Format response**:
   ```
   ## [Grouping Category]
   
   **Task #[ID]**: [Name]
   - [Notes if relevant]
   - Category: [Category]
   ```

## Workload Analysis

### User Pattern Examples:
- "Do I need to reprioritize? Is any day overloaded?"
- "How's my workload this week?"

### AI Response Template:
1. **Count tasks per day**
2. **Identify heavy days** (>3-4 tasks)
3. **Suggest redistributions**:
   - Move low-impact tasks to Filler
   - Suggest shifting to lighter days
   - Identify tasks that could be delegated

4. **Format response**:
   ```
   ## Workload Analysis
   
   **Heavy Days:**
   - Thursday: 5 tasks (consider moving 1-2 to Filler)
   
   **Light Days:**
   - Tuesday: 1 task (could take on more)
   
   **Suggestions:**
   - Move Task #[ID] to Filler (low impact)
   - Consider shifting Task #[ID] to Tuesday
   ```

## Completing Tasks

### User Pattern Examples:
- "Mark task #12 complete"
- "I finished the Heinz budget update"

### AI Response Template:
1. **Find the task** in active.json
2. **Move to completed.json** with completion date
3. **Remove from active.json**
4. **Confirm**: "✅ Marked complete: Task #[ID]: [Name]"

## Adding Notes

### User Pattern Examples:
- "Add this note to task #8: Client wants revised timeline"
- "Update task #15 with follow-up details"

### AI Response Template:
1. **Find task** in active.json
2. **Append or update notes** field
3. **Save changes**
4. **Confirm**: "✅ Updated notes for Task #[ID]"

## Error Handling

- **Invalid task ID**: "Could not find task #[ID]. Current active tasks are #[list]"
- **Unclear request**: "Could you clarify [specific part]? For example: [suggestion]"
- **Missing files**: Create empty JSON arrays if files don't exist

## Always Remember

- Generate sequential IDs (never duplicate)
- Use today's date for new tasks
- Follow exact category and day options
- Keep task names concise but descriptive
- Default unclear categories to "General"
- Default unclear timing to "Filler"