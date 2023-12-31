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

     - `SECRET_KEY=<BAD_SECRET_KEY>`

     - `CONNECTION_STRING=<connection_string>`

3. Map launch.json file to 'run and debug' configuration
4. In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Create Environment command to create a virtual environment in your workspace. Select venv and then the Python environment you want to use to create it.
5. After your virtual environment creation has been completed, run Terminal: Create New Terminal (Ctrl+Shift+`)) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.
   > Note: On Windows, if your default terminal type is PowerShell, you may see an error that it cannot run activate.ps1 because running scripts is disabled on the system. The error provides a link for information on how to allow scripts. Otherwise, use Terminal: Select Default Profile to set "Command Prompt" or "Git Bash" as your default instead.
6. Run the following commands in the terminal:

     - `pip install flask`

     - `pip install python-dotenv`

     - `pip install sqlalchemy`

     - `pip install psycopg2`

     - `pip install pyOpenSSL`
   
8. Create a db with the following tables
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
- Dockerize the project
- Overall code base could use a cleanup/optimization
- Use object-relational mapping instead of raw sql
- Roll-over logging
- Setting the python hash seed in the launch.json file does not seem right
