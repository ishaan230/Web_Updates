
## Monitor your PC / Server on discord anytime and anywhere on the intervals of 5 mins.
![alt text](https://www.shutterstock.com/shutterstock/videos/1077996398/thumb/7.jpg?ip=x480)

## <br> Usage

### Clone the repository
``` 
git clone https://github.com/ishaan230/Web_Updates
```

### Navigate to the directory
``` 
cd Web_Updates 
```
### Install Requirements
```
pip install -r requirements.txt
```

## Discord 
### Setup Discord:

#### 1. Create a private server in your discord account

#### 2. Create 3 channels named battery_updates, temp_updates, cpu_updates in your server.

#### 3. Go to Server Settings > Integrations > Webhooks > New Webhook

#### 4. Create 3 webhooks one for each channel and change channel location to battery_updates, temp_updates, cpu_updates in each of them.

#### 5. Copy the webhook url from each of them and paste it into updates.py

#### 6. Add a cronjob
```
crontab -e
```
#### 7. Add time in cronjob tasks in the end(5 mins interval)
```
*/5 * * * * /bin/python3 "ENTER YOUR PATH TO updates.py file"
```

#### 8. You are ready !

#### 9. logs are in generated in logs/log.txt