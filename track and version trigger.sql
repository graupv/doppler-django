-- insert to version table for every update/insert to Track table
-- track_track & versions_versions

CREATE OR REPLACE FUNCTION track_update_insert_version()
  RETURNS TRIGGER AS
$$

DECLARE track_name VARCHAR(200); -- name
DECLARE track_key VARCHAR(2); -- key
DECLARE track_lyrics VARCHAR(6000); -- lyrics
DECLARE modify_date TIMESTAMP; -- modify TIMESTAMP
DECLARE track_version INT; -- Version
DECLARE version_id INT; -- Version_id 
-- DECLARE track_private boolean; -- Private

    BEGIN
        SELECT NOW() INTO modify_date;
        IF (TG_OP = 'UPDATE') THEN
            SELECT  1 + (SELECT id from versions_versions ORDER BY id DESC LIMIT 1) INTO version_id;
        -- old y new
            
            
            RETURN NEW;

        ELSIF (TG_OP = 'INSERT') THEN
        -- no old
            INSERT INTO versions_versions ()
            RETURN NEW;
        END IF;
    END;
$$
LANGUAGE plpgsql;


CREATE TRIGGER track_version_control_trigger
    BEFORE UPDATE OR INSERT ON track_track 
    FOR EACH ROW EXECUTE PROCEDURE track_update_insert_version();