DROP DATABASE IF EXISTS aced;

CREATE DATABASE aced
    ENCODING utf8;


CREATE TABLE IF NOT EXISTS member (
    member_id   INT             NOT NULL,
    firstname   VARCHAR(32)     NOT NULL,
    lastname    VARCHAR(32)     NOT NULL,
    email       VARCHAR(64)     NOT NULL,
    phonenum    VARCHAR(12)     NOT NULL,
    optIN       BOOLEAN         NOT NULL,

    PRIMARY KEY(member_id)
)