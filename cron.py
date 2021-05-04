# TODO
from crontab import CronTab
import getpass

username = getpass.getuser()

#cron = CronTab(user=username)
cron = CronTab(tabfile='filename.tab')

cron.new(command='echo hi')