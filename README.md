# SSLCertExpirySummary

Thanks for taking a look at my project. The purpose of this project is to monitor SSL certificate expiry dates for sites.

### Project Functions:
- Card and list view
- Add/Edit/Remove SSL certificate's
- Filter based off Environment Type and/or Team
- Accounts (admin, regular)
- Add/Remove Users
- Add/Remove Environment Types
- Logging

### How to Setup your local environment:
1. Use VSCode (extensions: Pylance, Python)
2. Create a .env file in root of project

     `SECRET_KEY=<BAD_SECRET_KEY>`

     `CONNECTION_STRING=<connection_string>`

3. Map launch.json file to 'run and debug' configuration
4. Create a db with the following tables
     #### CertInfo
     | Column Name | Data Type | Allow Nulls |
     | ----------- | --------- | ----------- |
     | id | int | no |
     | name | nvarchar(150) | no |
     | address | nvarchar(150) | no |
     | port | int | no |
     | team | nvarchar(150) | no |
     | environmentId | int | no |

     > environmentId is a foreign key to id field in Environment table

     #### Environment
     | Column Name | Data Type | Allow Nulls |
     | ----------- | --------- | ----------- |
     | id | int | no |
     | environment | nvarchar(100) | no |

     #### UserInfo
     | Column Name | Data Type | Allow Nulls |
     | ----------- | --------- | ----------- |
     | id | int | no |
     | email | nvarchar(150) | no |
     | password | nvarchar(150) | no |
     | isAdmin | int | no |

### Things I would improve on
- Overall code base could use a cleanup/optimization
- Use object-relational mapping instead of raw sql
- Roll-over logging
- Setting the python hash seed in the launch.json file does not seem right
