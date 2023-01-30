# final website name TBD - considering 'worth it', 'uplift' or similar empowering titles

A crowdfunding website for people leaving or recovering from family and domestic violence situations.

## Features

### User Accounts

- [X] Username
- [X] Email Address
- [X] Password

### Project

- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [ ] Destroy - people can close their project rather than delete it
- Pledge
  - [X] Create
  - [X] Retrieve
  - [X] Update - haven't removed ability to change pledge amount yet
  - [ ] Destroy - as people are donating money, we don't want them to be able to take it back
- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy

### Implement suitable permissions

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Limit who can create
  - [ ] Limit who can retrieve - anyone can view projects
  - [X] Limit who can update
  - [ ] Limit who can delete - no one can delete
- Pledge
  - [X] Limit who can create
  - [ ] Limit who can retrieve - can see list but not individal pledge details
  - [X] Limit who can update - haven't removed amount yet from being editible
  - [ ] Limit who can delete - no one can delete, project owner will have ability to hide pledges in future
- User
  - [ ] Limit who can retrieve
  - [ ] Limit who can update
  - [ ] Limit who can delete

### Implement relevant status codes

- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404

### Handle failed requests gracefully 

- [X] 404 response returns JSON rather than text

### Use token authentication

- [X] impliment /api-token-auth/

## Additional features

- [X] Random user generator

Creates a randomly generated character string for the username of new accounts. This is a read only field. the intention behind this feature is so the user cannot accidentally reveal their identity online through their username. 

I've not been able to implement a check to ensure the username is unique yet, but I'm working on it.

- [X] Filter

A simple filter to see a list of projects based on the name of the project owner, date created, and whether the project is open or closed.

- [X] Reset password

Logged in user can change their password.

- [ ] Comments or Categories (sorry I ran out of time)

{{ description of feature 4 }}

### External libraries used

- [X] django-filter


## Part A Submission

- [X] A link to the deployed project: https://morning-resonance-16.fly.dev/admin/
- [X] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a token being returned.
- [ ] Your refined API specification and Database Schema. - I've added my original 10 page document that I submitted for homework, will update when I get a chance

### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).

1. Create User

```shell
curl --request POST \
  --url http://localhost:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"email": "admin5@admin.com",
	"password": "admin"
}'
```
--- please note for above username is omitted because it's randomly generated (see insomnia screenshot)

2. Sign in User

```shell
curl --request POST \
  --url http://localhost:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "admin",
	"password": "admin"
}'
```

3. Create Project

```shell
curl --request POST \
  --url http://localhost:8000/projects/ \
  --header 'Authorization: Token 4d5c65912a641cf77554de903ad5c252ed43da64' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Fundraising for a new home",
	"description": "I'\''m trying to raise enough bond money for a rental.",
	"goal": "1500",
	"image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
	"is_open": "True",
	"date_created": "2023-01-29T12:23:55.671Z"
}'
```