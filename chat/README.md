# Associations : Chat

In this exercise, you job is to create the models and functions defined below:

## Models

1. [ ] `Channel`: A channel must have a name.
2. [ ] `User`: A channel must have a name.
3. [ ] `Message`: A message must have a user, a channel, and some text content.

## Functions

- [ ] `create_channel(name)`: Create a `Channel`
  - [ ] `create_channel` is thoroughly tested
- [ ] `create_user(name)`: Create a `User`
  - [ ] `create_user` is thoroughly tested
- [ ] `create_message(user, channel, text)`: Create a message from `user` with the provided `text` in the `channel`
  - [ ] `create_message` is thoroughly tested
- [ ] `messages_for(channel)`: Return the `Message`s in `channel`
  - [ ] `messages_for` is thoroughly tested
- [ ] `active_users(channel)`: Return the `User`s that have created a message in `channel`
  - [ ] `active_users` is thoroughly tested
- [ ] `lurkers(channel)`: Return the `User`s that have not created a message in `channel`
  - [ ] `lurkers` is thoroughly tested
