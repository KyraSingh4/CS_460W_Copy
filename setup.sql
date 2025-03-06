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
);

CREATE TABLE IF NOT EXISTS charges (
    member_id   INT                 NOT NULL,
    amount      DOUBLE PRECISION    NOT NULL,
    date        DATE                NOT NULL,
    description  VARCHAR(128)        NOT NULL,

    FOREIGN KEY(member_id) REFERENCES member(member_ID)
                                   ON DELETE CASCADE
)