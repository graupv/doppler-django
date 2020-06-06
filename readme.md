#   Django & Django Rest Framework

## Endpoints

    Token
        - Get token
        api/v1/token-auth/
        BODY: {username, password}

        - Refresh
        api/v1/token-refresh
        BODY: {token: old_valid_token}
        

    Tracks
        - Create 
        POST, api/v1/tracks
        Body {id, name, username, lyrics, key, version, modify_date}

        - User Tracks
        GET, api/v1/tracks/mytracks

        - Single Track
        GET, api/v1/tracks/id

        - Single track lyrics
        GET, api/v1/tracks/id/lyrics

    Accounts
        - Create
        POST, /api/v1/account
        BODY : {username, password, email}



         
