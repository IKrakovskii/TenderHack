#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler
import mysql.connector as mysql
import socketserver
import requests
import json
import os
import numpy as np
import pandas as pd


class MyHTTPHandler(BaseHTTPRequestHandler):
    def __init__(self):
        work_dir = os.getcwd()
        contracts_file = os.path.join(os.path.join(work_dir, 'Data'), 'Контракты_Иркутск.csv')
        self.contracts_df = pd.read_csv(contracts_file,
                                        delimiter=',',
                                        dtype={
                                            "id": int,
                                            "contract_number": str,
                                            "date_public_contract": str,
                                            "date_sign_contract": str,
                                            "price": float,
                                            "inn_client": str,
                                            "kpp_client": str,
                                            "name_client": str,
                                            "inn_provider": str,
                                            "kpp_provider": str,
                                            "name_provider": str,
                                            "cte": str})

    def __call__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_POST(self):
        pass

    def do_GET(self):
        if '/api/contracts' in self.path:
            get = self.path.replace('/api/contracts' + '?', '')
            get = {i.split('=')[0]: i.split('=')[1] for i in get.split('&')}
            if get['startIndex'] == '':
                get['startIndex'] = 0
            else:
                try:
                    get['startIndex'] = int(get['startIndex'])
                except:
                    get['startIndex'] = 0

            if get['minPrice'] == '':
                get['minPrice'] = 0
            else:
                try:
                    get['minPrice'] = int(get['minPrice'])
                except:
                    get['minPrice'] = 0

            if get['maxPrice'] == '':
                get['maxPrice'] = self.contracts_df['price'].max()
            else:
                try:
                    get['maxPrice'] = int(get['maxPrice'])
                except:
                    get['maxPrice'] = self.contracts_df['price'].max()
            ascending = True
            if get['sortOrder'] == 'desc':
                ascending = False

            answer_json = {'error': 1, 'total': 0, 'data': []}
            answer_df = self.contracts_df[
                (self.contracts_df['price'] >= get['minPrice']) & (self.contracts_df['price'] <= get['maxPrice'])]
            answer_df = answer_df.reindex()
            answer_df = answer_df.iloc[get['startIndex']:get['startIndex'] + 100, :-1]
            answer_df = answer_df.sort_values(by=get['sortBy'], ascending=ascending)
            if answer_df.shape[0] != 0:
                answer_json['error'] = 0
                for i in range(answer_df.shape[0]):
                    answer_json['data'].append(dict(zip(list(answer_df.columns), answer_df.iloc[i, :].to_list())))
                answer_json['total'] = len(answer_json['data'])
            else:
                answer_json = {'error': 1, 'total': 0, 'data': []}
            self.send_my_mess(str(answer_json), type_content='application/json')

        elif 'api/contract/' in self.path:
            # answer_df = 
            pass

    def send_my_mess(self, message, type_content='text/html'):
        if type_content == 'application/json':
            message = message.replace("'", '"')
        answer_mess = message.encode('utf-8')
        answer_code = 200
        self.send_response(answer_code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', type_content)
        self.send_header('Content-Length', str(len(answer_mess)))
        self.end_headers()
        self.wfile.write(answer_mess)


def start_server(port):
    handler = MyHTTPHandler()
    server = socketserver.TCPServer(('', port), handler)
    print(f'Server start at port: {port}')
    server.serve_forever()


if __name__ == '__main__':
    from multiprocessing import Process, Pipe

    a, b = Pipe()


    def start_server(port: int):
        try:
            handler = MyHTTPHandler()
            server = socketserver.TCPServer(('', port), handler)
            print(f'Server start at port: {port}')
            server.serve_forever()
        except Exception as ex:
            b.send(ex)


    PORT = 8008
    while True:
        p = Process(target=start_server, args=(PORT,))
        p.start()
        print(a.recv())
        p.join()
