from crontab import CronTab
#init cron
cron   = CronTab()

#add new cron job
job  = cron.new(command='data_collection/dotabot2.py')

#job settings
job.minutes.every(30)