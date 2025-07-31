#!/usr/bin/env python3
"""
Task Manager Helper Functions for Cursor AI

This module provides helper functions that Cursor AI can use to:
- Add new tasks with proper ID generation
- Read and filter existing tasks  
- Move tasks between active and completed
- Validate task data formats

Usage: Cursor AI can run these functions to manage the task JSON files
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional

# File paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ACTIVE_FILE = os.path.join(BASE_DIR, "data", "active.json")
COMPLETED_FILE = os.path.join(BASE_DIR, "data", "completed.json")

def load_tasks(file_path: str) -> List[Dict]:
    """Load tasks from JSON file, return empty list if file doesn't exist"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(file_path: str, tasks: List[Dict]) -> None:
    """Save tasks to JSON file with pretty formatting"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def get_next_task_id() -> int:
    """Generate the next sequential task ID"""
    active_tasks = load_tasks(ACTIVE_FILE)
    completed_tasks = load_tasks(COMPLETED_FILE)
    
    all_ids = []
    for task in active_tasks + completed_tasks:
        if 'id' in task:
            all_ids.append(task['id'])
    
    return max(all_ids, default=0) + 1

def add_task(name: str, notes: str = "", category: str = "General", 
            planned_work_day: str = "Filler", status: str = "Active") -> Dict:
    """
    Add a new task with auto-generated ID and today's date
    
    Args:
        name: Task name/summary
        notes: Additional details
        category: Projects, Project Management, or General
        planned_work_day: Monday-Friday or Filler
        status: Active, Complete, or Recurring
    
    Returns:
        The created task dictionary
    """
    task = {
        "id": get_next_task_id(),
        "name": name.strip(),
        "notes": notes.strip(),
        "date_added": datetime.now().strftime("%Y-%m-%d"),
        "status": status,
        "planned_work_day": planned_work_day,
        "category": category
    }
    
    active_tasks = load_tasks(ACTIVE_FILE)
    active_tasks.append(task)
    save_tasks(ACTIVE_FILE, active_tasks)
    
    return task

def get_tasks_by_day(day: str) -> List[Dict]:
    """Get all active tasks for a specific day"""
    active_tasks = load_tasks(ACTIVE_FILE)
    return [task for task in active_tasks if task.get('planned_work_day') == day]

def get_tasks_by_category(category: str) -> List[Dict]:
    """Get all active tasks for a specific category"""
    active_tasks = load_tasks(ACTIVE_FILE)
    return [task for task in active_tasks if task.get('category') == category]

def complete_task(task_id: int) -> Optional[Dict]:
    """
    Move a task from active to completed
    
    Args:
        task_id: ID of task to complete
        
    Returns:
        The completed task if found, None otherwise
    """
    active_tasks = load_tasks(ACTIVE_FILE)
    completed_tasks = load_tasks(COMPLETED_FILE)
    
    # Find and remove from active
    task_to_complete = None
    for i, task in enumerate(active_tasks):
        if task.get('id') == task_id:
            task_to_complete = active_tasks.pop(i)
            break
    
    if task_to_complete:
        # Update status and add completion date
        task_to_complete['status'] = 'Complete'
        task_to_complete['date_completed'] = datetime.now().strftime("%Y-%m-%d")
        
        # Add to completed list
        completed_tasks.append(task_to_complete)
        
        # Save both files
        save_tasks(ACTIVE_FILE, active_tasks)
        save_tasks(COMPLETED_FILE, completed_tasks)
        
        return task_to_complete
    
    return None

def update_task_notes(task_id: int, new_notes: str) -> Optional[Dict]:
    """
    Update the notes field for a task
    
    Args:
        task_id: ID of task to update
        new_notes: New notes content
        
    Returns:
        The updated task if found, None otherwise
    """
    active_tasks = load_tasks(ACTIVE_FILE)
    
    for task in active_tasks:
        if task.get('id') == task_id:
            task['notes'] = new_notes.strip()
            save_tasks(ACTIVE_FILE, active_tasks)
            return task
    
    return None

def get_workload_summary() -> Dict:
    """Get a summary of tasks grouped by day"""
    active_tasks = load_tasks(ACTIVE_FILE)
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Filler']
    summary = {}
    
    for day in days:
        day_tasks = [task for task in active_tasks if task.get('planned_work_day') == day]
        summary[day] = {
            'count': len(day_tasks),
            'tasks': day_tasks
        }
    
    return summary

if __name__ == "__main__":
    # Example usage for testing
    print("Task Manager Helper Functions")
    print(f"Next ID: {get_next_task_id()}")
    print(f"Active tasks: {len(load_tasks(ACTIVE_FILE))}")
    print(f"Completed tasks: {len(load_tasks(COMPLETED_FILE))}")