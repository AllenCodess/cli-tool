import argparse
from utils.storage import load_data, save_data
from utils.helpers import print_success, print_error, print_info
from models.user import User
from models.project import Project
from models.task import Task

def add_user(args):
    users = load_data()
    user = User(args.name, args.email)
    users.append(user)
    save_data(users)
    print_success(f"User '{args.name}' added successfully!")

def list_users(args):
    users = load_data()
    if not users:
        print_info("No users found.")
    for u in users:
        print_info(f"{u.id}: {u.name} ({u.email})")

def add_project(args):
    users = load_data()
    user = next((u for u in users if u.id == args.user_id), None)
    if not user:
        print_error("User not found.")
        return
    project = Project(args.title, args.description, args.due_date)
    user.add_project(project)
    save_data(users)
    print_success(f"Project '{args.title}' added for user {user.name}")

def list_projects(args):
    users = load_data()
    user = next((u for u in users if u.id == args.user_id), None)
    if not user:
        print_error("User not found.")
        return
    for p in user.projects:
        print_info(f"{p.id}: {p.title} (Due: {p.due_date})")

def add_task(args):
    users = load_data()
    for u in users:
        for p in u.projects:
            if p.id == args.project_id:
                task = Task(args.title, assigned_to=args.assigned_to)
                p.add_task(task)
                save_data(users)
                print_success(f"Task '{args.title}' added to project '{p.title}'")
                return
    print_error("Project not found.")

def complete_task(args):
    users = load_data()
    for u in users:
        for p in u.projects:
            for t in p.tasks:
                if t.id == args.task_id:
                    t.status = "completed"
                    save_data(users)
                    print_success(f"Task '{t.title}' marked as completed!")
                    return
    print_error("Task not found.")

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(title="Commands")

    # add-user
    p1 = subparsers.add_parser("add-user", help="Add a new user")
    p1.add_argument("name")
    p1.add_argument("email")
    p1.set_defaults(func=add_user)

    # list-users
    p2 = subparsers.add_parser("list-users", help="List all users")
    p2.set_defaults(func=list_users)

    # add-project
    p3 = subparsers.add_parser("add-project", help="Add a new project to a user")
    p3.add_argument("user_id", type=int)
    p3.add_argument("title")
    p3.add_argument("description")
    p3.add_argument("due_date")
    p3.set_defaults(func=add_project)

    # list-projects
    p4 = subparsers.add_parser("list-projects", help="List projects of a user")
    p4.add_argument("user_id", type=int)
    p4.set_defaults(func=list_projects)

    # add-task
    p5 = subparsers.add_parser("add-task", help="Add a new task to a project")
    p5.add_argument("project_id", type=int)
    p5.add_argument("title")
    p5.add_argument("--assigned_to", default=None)
    p5.set_defaults(func=add_task)

    # complete-task
    p6 = subparsers.add_parser("complete-task", help="Mark a task as completed")
    p6.add_argument("task_id", type=int)
    p6.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
