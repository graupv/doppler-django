#   Django & Django Rest Framework

## Endpoints

    Token
        - Get token
        POST: api/v1/token-auth/
        BODY: {username, password}

        - Refresh
        POST: api/v1/token-refresh
        BODY: {token: old_valid_token}
        

    Tracks
        Header: {Authorization: JWT ${TOKEN}}
        
        - Create 
        POST: api/v1/tracks
        Body {
            id=1, name='string', username, 
            lyrics, key, version=1, 
            modify_date='2020-01-01'
            }

        - User Tracks
        GET: api/v1/tracks/mytracks

        - Single Track
        GET: api/v1/tracks/id

        - Single track lyrics
        GET: api/v1/tracks/id/lyrics

    Accounts
        - Create
        POST: /api/v1/account/create/
            BODY: {username, password, email}

        - Get user or user list (only super user)
        GET: api/v1/account or api/v1/account/id




         
