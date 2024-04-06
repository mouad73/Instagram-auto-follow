# Automation Guide

This guide provides instructions on how to automate the Instagram automation script using Task Scheduler on Windows.

## Prerequisites

Before proceeding with automation, ensure that you have completed the following steps:
- Installed Python 3.x on your machine.
- Cloned the Instagram automation script repository to your local machine.
- Modified the `config.yaml` file with your Instagram credentials, hashtags, and other settings.
- Tested the script to ensure it runs successfully manually.

## Automating with Task Scheduler

Follow these steps to set up automation using Task Scheduler:

1. **Open Task Scheduler:**
   - Open Task Scheduler by searching for it in the Start menu.

2. **Create a New Task:**
   - In the right-hand panel, click on "Create Task..." to create a new task.

3. **General Settings:**
   - Give your task a name and description in the General tab.
   - Choose "Run whether the user is logged on or not."
   - Check "Run with highest privileges."
   - Select the appropriate Windows version for your script.

4. **Triggers:**
   - Click "New" in the Triggers tab to create a trigger for your task.
   - Choose the schedule (daily, weekly, etc.) and set the time when you want the task to run.

5. **Actions:**
   - Click "New" in the Actions tab to create a new action for your task.
   - Choose "Start a program" as the action.
   - Browse and select the `run_instagram_script.bat` file from your cloned repository.

6. **Save and Test:**
   - Click "OK" to save the task.
   - Right-click on your task in Task Scheduler and choose "Run" to test if it runs successfully.

7. **Monitor Task Scheduler:**
   - Monitor Task Scheduler to ensure that the task runs at the scheduled time and executes the Instagram automation script.

## Troubleshooting

If your task fails to run or encounters errors, check the following:
- Ensure that Python and the required packages are installed correctly.
- Verify that the paths in your batch file (`run_instagram_script.bat`) are correct.
- Check Task Scheduler logs for any error messages or issues.

By following these steps, you can automate the Instagram automation script to run at specified intervals using Task Scheduler on Windows.
