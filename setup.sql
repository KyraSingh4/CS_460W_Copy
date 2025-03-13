CREATE USER aceduser WITH PASSWORD 'acedpassword';
GRANT ALL PRIVILEGES ON DATABASE aced TO aceduser;
GRANT ALL PRIVILEGES ON TABLE member TO aceduser;
GRANT ALL PRIVILEGES ON TABLE charges TO aceduser;
GRANT ALL PRIVILEGES ON TABLE reservation TO aceduser;
GRANT ALL PRIVILEGES ON TABLE attendees TO aceduser;

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
    date        DATE                NOT NULL DEFAULT CURRENT_DATE,
    description VARCHAR(128)        NOT NULL,
    type        VARCHAR(6)          NOT NULL,

    FOREIGN KEY(member_id) REFERENCES member(member_ID)
                                   ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS reservation (
    reservation_id  INT             NOT NULL,
    court_num       INT             NOT NULL,
    res_day         INT             NOT NULL,
    start_time      TIME            NOT NULL,
    end_time        TIME            NOT NULL,
    member_ID       INT             NOT NULL,
    type            VARCHAR(7)      NOT NULL,

    PRIMARY KEY(reservation_id),
    FOREIGN KEY(member_id) REFERENCES member(member_id)
                                    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS attendees (
    reservation_ID  INT             NOT NULL,
    firstname       VARCHAR(32)     NOT NULL,
    lastname        VARCHAR(32)     NOT NULL,
    member_id       INT,

    FOREIGN KEY(reservation_id) REFERENCES reservation(reservation_id)
                                    ON DELETE CASCADE
);

INSERT INTO member VALUES (
    1,
    'President',
    'Staff',
    'president@aced.com',
    '111-111-1111',
    FALSE,
    TRUE
    );

INSERT INTO member VALUES (
    2,
    'Billing',
    'Staff',
    'billing@aced.com',
    '111-111-1112',
    FALSE,
    TRUE
    );