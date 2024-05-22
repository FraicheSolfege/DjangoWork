from django.db import models

# Create your models here.

class Channel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    text_content = models.CharField(max_length=1000)

    def __str__(self):
        return self.text_content

def create_channel(name):
    return Channel.objects.create(name=name)

def create_user(name):
    return User.objects.create(name=name)

def create_message(user,channel,text):
    return Message.objects.create(user=user,channel=channel, text_content=text)

def messages_for(channel):
    return Message.objects.filter(channel__name = channel)

def active_users(channel):
    messages = Message.objects.filter(channel__name = channel)
    active = []
    for message in messages:
        active.append(message.user)
    
    return active

def lurkers(channel):
    users = User.objects.all()
    active = active_users(channel)
    lurkers = []
    for user in users:
        if user not in active:
            lurkers.append(user.name)

    return lurkers