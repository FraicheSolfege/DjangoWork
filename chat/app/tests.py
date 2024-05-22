from django.test import TestCase
from app import models as c
# Create your tests here.

class TestCases(TestCase):
    def test_create_channel(self):
        bri = c.create_channel("Bri Channel")
        kera = c.create_channel("Kera Channel")
        
        self.assertEqual(bri.name, "Bri Channel")
        self.assertEqual(kera.name, "Kera Channel")

    def test_create_user(self):
        bri = c.create_user("Bri")
        kera = c.create_user("Kera")

        self.assertEqual(bri.name, "Bri")
        self.assertEqual(kera.name, "Kera")

    def test_create_message(self):
        bri_user = c.create_user("Bri")
        kera_user = c.create_user("Kera")
        
        bri_channel = c.create_channel("Bri Channel")
        kera_channel = c.create_channel("Kera Channel")

        bri_message = c.create_message(bri_user, bri_channel, "This is Bris Message")
        kera_message = c.create_message(kera_user, kera_channel, "This is Keras Message")

        self.assertEqual(bri_message.user, bri_user)
        self.assertEqual(bri_message.channel, bri_channel)
        self.assertEqual(bri_message.text_content, "This is Bris Message")

        self.assertEqual(kera_message.user, kera_user)
        self.assertEqual(kera_message.channel, kera_channel)
        self.assertEqual(kera_message.text_content, "This is Keras Message")

    def test_messages_for(self):
        bri_user = c.create_user("Bri")
        kera_user = c.create_user("Kera")
        
        bri_channel = c.create_channel("Bri Channel")
        kera_channel = c.create_channel("Kera Channel")

        bri_message = c.create_message(bri_user, bri_channel, "This is Bris Message")
        kera_message = c.create_message(kera_user, kera_channel, "This is Keras Message")

        bri_messages_for = c.messages_for("Bri Channel")
        kera_messages_for = c.messages_for("Bri Channel")

        self.assertEqual(len(bri_messages_for), 1)
        self.assertEqual(len(kera_messages_for), 1)

    def test_active_users(self):
        bri_user = c.create_user("Bri")
        kera_user = c.create_user("Kera")
        
        bri_channel = c.create_channel("Bri Channel")
        kera_channel = c.create_channel("Kera Channel")

        bri_message = c.create_message(bri_user, bri_channel, "This is Bris Message")
        kera_message = c.create_message(kera_user, kera_channel, "This is Keras Message")

        bri_active = c.active_users("Bri Channel")
        kera_active = c.active_users("Kera Channel")

        self.assertEqual(len(bri_active), 1)
        self.assertEqual(len(kera_active), 1)

    def test_lurkers(self):
        bri_user = c.create_user("Bri")
        kera_user = c.create_user("Kera")
        smore_user = c.create_user("Smore")

        
        bri_channel = c.create_channel("Bri Channel")
        kera_channel = c.create_channel("Kera Channel")
        smore_channel = c.create_channel("Smore Channel")


        bri_message = c.create_message(bri_user, bri_channel, "This is Bris Message")
        kera_message = c.create_message(kera_user, kera_channel, "This is Keras Message")

        smore_lurks = c.lurkers("Smore Channel")
        print(smore_lurks)
        self.assertEqual(len(smore_lurks), 3)
