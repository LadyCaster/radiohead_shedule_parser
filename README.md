- First, specify both "FROMADDR" and "TOADDR" in docker-compose.yml to set sender and reciever. Also fill in field "PASSWORD" with password from senders e-mail.
*If you are using gmail, let unsafe applications use your account* 
*If you are using vpn service docker might have a problem creating a network bridge*

- Then give a shedule.sh permission to run the script by typing ```chmod +x ./shedule.sh``` in your terminal (be sure that you are in project's directory).

- Finally, create crontab rule to start application on time. Type ```crontab -e``` and create job for cron in opened editor. You can use http://www.nncron.ru/help/EN/working/cron-format.htm as a guide. Your crontab job should look like "*/10 * * * * /fullpath/shedule.sh"

Everything's done, you're stunning, don't miss the concerts!
