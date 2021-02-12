from twilio.rest import Client 
 
account_sid = 'AC1611fa776d7720d7859eda7628d4523e' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(         
                              to='+639777800349' 
                          ) 
 
print(message.sid)