# Get PC Updates on web anywhere , anytime using Discord

## Monitor your PC / Server on discord anytime and anywhere on the intervals of 5 mins.

## <br> Usage

### Clone the repository
``` git clone https://github.com/ishaan230/Web-PC-Updates```

### Navigate to the directory
``` cd Web-PC-Updates ```

## Discord 
### Setup Discord:

#### 1. Create a private server in your discord account

#### 2. Create 3 channels named battery_updates, temp_updates, cpu_updates in your server.

#### 3. Go to Server Settings > Integrations > Webhooks > New Webhook

#### 4. Create 3 webhooks one for each channel and change channel location to battery_updates, temp_updates, cpu_updates in each of them.

#### 5. Copy the webhook url from each of them and paste it into updates.py

#### 6. Run the file
```python3 updates.py```