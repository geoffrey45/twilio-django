from django.db import models
from twilio.rest import Client

#defining a simple class
class Score(models.Model):
    #integer field
    test_result = models.PositiveIntegerField()

    #string representation
    def __str__(self):
        return str(self.test_result)

    #save method
    def save(self, *args, **kwargs):
        #if test_result is less than 80 execute this
        if self.test_result < 80:
            #twilio code
            account_sid = 'AC1a1xxxxxxxxxxxxxxxxxxxxxxxxxx'
            auth_token = 'ccbd11xxxxxxxxxxxxxxxxxxxxxxxxxx'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'Hi, your test result is {self.test_result}. Great job',
                                        from_='+14806xxxxx',
                                        to='+254111xxxxxx' 
                                    )

            print(message.sid)
        return super().save(*args, **kwargs)