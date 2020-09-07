# To run on Synology NAS on schedule

1. Open control panel
![](resources/1._Control_Panel.png)
1. Switch to `Advanced Mode`
![](resources/2._Advanced_Control_Panel.png)
1. Create new scheduled task
![](resources/3._Task_scheduler.png)
1. Set task name and user
![](resources/4._Task_scheduler_general.png)
1. Set schedule
![](resources/5._Task_scheduler_schedule.png)
1. Set command to `docker run --rm -i justinasb/skelbiu.lt:latest python ./script.py $USERNAME $PASSWORD` in `Task Settings` by replacing `$USERNAME` and `$PASSWORD` with actual values
![](resources/6._Task_scheduler_task_settings.png)

# To run this on demand

```
docker build -t justinasb/skelbiu.lt:latest .
docker run --rm -it justinasb/skelbiu.lt:latest
docker run justinasb/skelbiu.lt:latest python ./script.py $USERNAME $PASSWORD
```
