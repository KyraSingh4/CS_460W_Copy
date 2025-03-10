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
    active      BOOLEAN         NOT NULL,

    PRIMARY KEY(member_id)
);

CREATE TABLE IF NOT EXISTS charges (
    member_id   INT                 NOT NULL,
    amount      DOUBLE PRECISION    NOT NULL,
    date        DATE                NOT NULL,
    description VARCHAR(128)        NOT NULL,
    type        VARCHAR(6)          NOT NULL,

    FOREIGN KEY(member_id) REFERENCES member(member_ID)
                                   ON DELETE CASCADE
)

CREATE TABLE IF NOT EXISTS reservation (
    reservation_id  INT             NOT NULL,
    court_num       INT             NOT NULL,
    res_day         INT             NOT NULL,
    start_time      TIME            NOT NULL,
    end_time        TIME            NOT NULL,
    member_ID       INT             NOT NULL,
    type            VARCHAR(7)      NOT NULL     

    PRIMARY KEY(reservation_id)
    FOREIGN KEY(member_id) REFERENCES member(member_id)
                                    ON DELETE CASCADE
)

CREATE TABLE IF NOT EXISTS attendees (
    reservation_ID  INT             NOT NULL,
    firstname       VARCHAR(32)     NOT NULL,
    lastname        VARCHAR(32)     NOT NULL,
    member_id       INT,

    FOREIGN KEY(reservation_id) REFERENCES reservation(reservation_id)
                                    ON DELETE CASCADE
)
