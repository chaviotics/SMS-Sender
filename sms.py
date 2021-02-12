'''
I can't really use Twilio because I don't have an upgraded account and I'm in the Philippines. I must have an upgraded account for me to be able to send messages outside the US or Canada.
'''


from twilio.rest import Client 
 
account_sid = 'AC1611fa776d7720d7859eda7628d4523e' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='+1 205 289 3402', 
                              body='HELLLOOOOOO CHAVIIIU!',      
                              to='+639777800349' 
                          ) 
 
print(message.sid)