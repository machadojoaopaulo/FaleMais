USE TELZIR;

CREATE TABLE tarifas (
    id integer not null auto_increment primary key,
    dddOrigem  integer not null,
    dddDestino integer not null,
    tarifa decimal(3,2) not null
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO tarifas (dddOrigem, dddDestino, tarifa) VALUES (11, 16, 1.90);
INSERT INTO tarifas (dddOrigem, dddDestino, tarifa) VALUES (16, 11, 2.90);
INSERT INTO tarifas (dddOrigem, dddDestino, tarifa) VALUES (11, 17, 1.70);
INSERT INTO tarifas (dddOrigem, dddDestino, tarifa) VALUES (17, 11, 2.70);
INSERT INTO tarifas (dddOrigem, dddDestino, tarifa) VALUES (11, 18, 0.90);
INSERT INTO tarifas (dddOrigem, dddDestino, tarifa) VALUES (18, 11, 1.90);
