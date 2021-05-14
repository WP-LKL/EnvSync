# EnvSync
A major reason for using paid/hosted services is syncronization uniformity. EnvSync exists to enable stand-alone shared config and environment settings across users and systems. Specifically EnvSync should be expanded and developed organically by those who seeks such functionality in the open-source software they love and enjoy.

## Automation
* GNU/Linux
    * Celery 
    * Cron
        * ``python-crontab``
* Windows
    * TaskScheduler
    * Startup folder (implemented)

## Logic
I. We assume GitHub contains the latest Env. <br>
II. We backup before updating our env in case assumption I. is incorrect. <br>
III. We can always go back and track changes in our environments.

## Compatibility
* Conda Environments (TODO)

## Development

Synchronizing Code Environments and Configs using CronTab and Celery for cross-OS compatibility. 


### TODO
* Move conda specific functions to a separate folder/file

### Future

This tool will be more useful when lockdown stops, and changing (Laptop/Desktop) systems will be more frequent, in the meantime I have raised a [feature request](https://github.com/conda/conda/issues/10630) for Conda; that more metadata is added for their environments, namely: [created date, last updated] when exporting.