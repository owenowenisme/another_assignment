# fastapi_assignment

Built with fastapi and sqlite as db.

## Requirement
Have docker installed on your machine.

**macOS:**

1. Download Docker Desktop for Mac from the [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-mac/).
2. Double-click the downloaded `.dmg` file and drag the Docker app to your Applications folder.
3. Open Docker Desktop from your Applications folder. You'll see a whale icon in the top status bar indicating that Docker is running.

**Windows:**

1. Download Docker Desktop for Windows from the [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-windows/).
2. Run the installer and follow the instructions.
3. Docker Desktop will start automatically once installation is complete. You'll see a whale icon in the notification area indicating that Docker is running.

**Linux (Ubuntu):**
```
 curl -fsSL https://get.docker.com -o get-docker.sh
 sudo sh get-docker.sh
```
 ## Usage
1. Clone this repo and enter in terminal.
2. Type in your terminal: ```docker compose up -d ```
3. Go to http://localhost:8000/docs for API testing
## API Reference

### Get user

```GET /user```
| Parameter  | Type     |
| :--------  | :------- | 
| `user_id`  | `int`    |  


### Create user

```POST /user```

* Request Body
```json
{
  "name": "string",
  "email": "string",
  "password": "string"
}
```

### Update user

```PUT /user```
``` json
{
  "name": "string",
  "email": "string",
  "password": "string",
  "id": 0
}
```
### Delete user

```DELETE /user ```

| Parameter  | Type     |
| :--------  | :------- | 
| `user_id`  | `int`    |  
