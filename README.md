**AI Code Review Assistant**

**Overview**

One challenge I noticed while working on personal and professional projects is that code reviews often happen after the code has already been pushed to a remote repository. At that point, developers have already created a pull request, CI pipelines have started running, and reviewers spend time pointing out issues that could have been caught much earlier.

I wanted to see if an AI agent could provide meaningful feedback before the code ever left my machine.

To solve this, I built an AI-powered code review assistant integrated into a Spring Boot application. The application hooks into Git using a pre-commit hook, allowing the AI agent to automatically review only the files that have changed whenever a commit is made.

Instead of waiting for a pull request review, the agent analyzes the code locally and provides suggestions related to code quality, readability, security concerns, potential bugs, and adherence to best practices. This creates a faster feedback loop, allowing issues to be fixed immediately before they become part of the repository history.

The project gave me practical experience integrating LLMs into an existing Java application, designing an automated developer workflow, and building an AI-assisted tool that fits naturally into the software development lifecycle instead of replacing it.

**Features**

Automatic code review before every Git commit
Spring Boot backend integration
Git pre-commit hook automation
Reviews only modified files
Detects potential bugs and code smells
Suggests improvements for readability and maintainability
Identifies possible security issues
Provides instant local feedback before code is pushed
