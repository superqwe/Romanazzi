import sqlite3
from pprint import pprint as pp

DB_IN = 'database.db'
DB_OUT = 'db.sqlite3'

if __name__ == '__main__':
    conn_in = sqlite3.connect(DB_IN)
    cur_in = conn_in.cursor()
    conn_out = sqlite3.connect(DB_OUT)
    cur_out = conn_out.cursor()

    # # CodiceAteco --> gs_codice_ateco
    # select = """
    # SELECT * FROM CodiceAteco
    # """
    # cur_in.execute(select)
    #
    # rows = []
    # for r in cur_in.fetchall():
    #     print(r)
    #
    #     row = [r[-1],]
    #     row.extend(list(r[:-1]))
    #     print(row)
    #     insert = 'INSERT INTO gs_codice_ateco VALUES (?, ?, ?, ?)'
    #     cur_out.execute(insert, row)
    #
    # conn_out.commit()

    # Cliente --> gs_cliente
    select = """
    SELECT * FROM Cliente
    """
    cur_in.execute(select)

    rows = []
    for r in cur_in.fetchall():
        ragione_sociale, partita_iva, email, pec, indirizzo, citta, provincia, cap, telefono, riferimento, codice_ateco, \
        numero_REA, posizione_INPS, posizione_INAIL, cassa_edile, incarico_RSPP_esterno, data_contratto, \
        data_scadenza_contratto, note, pk, pk2, cessato = r

        # convertire le date in datetime
        row = pk, ragione_sociale, partita_iva, email, pec, indirizzo, citta, provincia, cap, telefono, riferimento, \
              numero_REA, posizione_INPS, posizione_INAIL, cassa_edile, incarico_RSPP_esterno, data_contratto, \
              data_scadenza_contratto, note, cessato, codice_ateco


        insert = 'INSERT INTO gs_cliente VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        cur_out.execute(insert, row)

    conn_out.commit()
