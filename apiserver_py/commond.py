# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2019/11/12 21:27
# @author  : Mo
# @function: get service of fastapi

import time
from typing import Optional

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from db_connection import Mysql_Db_Manage

app = FastAPI()
table_cmd = 'my_cmd'
black_cmd = 'black_cmd'
table_command = 'my_command'
table_share_cmd = 'cmd'
table_share_command = 'command'

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get('/test/a={a}/b={b}')
def calculate(a: int = None, b: int = None):
    c = a + b
    res = {"res": c}
    return res


@app.post('/addH')
def addH(command: str = Body(..., embed=True)):
    if command is None:
        return "-2"
    sql = "select * from " + black_cmd + " where cmd = '" + command.split(" ")[0] + "' limit 1"
    result = Mysql_Db_Manage.is_have(sql=sql)
    if result:
        return
    sql = "select * from " + table_cmd + " where cmd = '" + command.split(" ")[0] + "' limit 1"
    result = Mysql_Db_Manage.is_have(sql=sql)
    if not result:
        sql = "insert into " + table_cmd + "(cmd,`time`) values('" + str(command.split(" ")[0]) + "'," + str(
            int(time.time())) + ")"
        Mysql_Db_Manage.update_data(sql=sql)
    sql = "insert into " + table_command + "(command,`time`) values('" + str(command) + "'," + str(
        int(time.time())) + ")"
    return '2'


@app.get('/getAll')
def addH(name: Optional[str] = False,detail: Optional[str] = False):

    sql = "select * from " + table_command
    if name:
        sql += "  where command like '%" + name + "%' "
    sql += " order by time desc "
    result = Mysql_Db_Manage.select_All_data(sql=sql)
    data = []
    result_data = []
    if not detail:
        print("进入了这里")
        for line in result:
            if line['command'] not in data:
                if str(line['command']).split(" ").__len__() > 1:
                    print(line['command'])
                    data.append(line['command'])
                    result_data.append(line)

    return result_data


@app.get('/getAll/name={name}')
def getAll(name: str = None):
    sql = "select * from " + table_command + " where command like '%" + name + "%' order by time desc"
    print("返回结果是：ddd" )
    return Mysql_Db_Manage.select_All_data(sql=sql)


@app.get('/getAll/cmd={cmd}')
def getAll(cmd: str = None):
    sql = "select * from " + table_command
    # if cmd == "null":
    #     sql2 = "select * from " + table_cmd + " order by cmd asc limit 1"
    #     one_data = Mysql_Db_Manage.select_one_data(sql=sql2)
    #     cmd = one_data["cmd"]
    if cmd is not None and cmd != 'null':
        sql += " where command like '" + cmd + "%'"
    sql += " order by time desc"
    return Mysql_Db_Manage.select_All_data(sql=sql)


@app.get('/getCmdAll')
def addH(cmd: str = None):
    sql = "select * from " + table_cmd + " order by cmd asc"
    return Mysql_Db_Manage.select_All_data(sql=sql)


@app.post('/update_command')
def update_command(id: int = Body(..., embed=True), description: str = Body(..., embed=True)):
    sql = "update " + table_command + " set description = '" + description + "' where id = " + str(id)
    return '2'


@app.post('/add_share')
def add_share(command: str = Body(..., embed=True), description: str = Body(..., embed=True)):
    sql = "select * from " + table_share_cmd + " where cmd = '" + command.split(" ")[0] + "' limit 1"
    result = Mysql_Db_Manage.is_have(sql=sql)
    if not result:
        sql = "insert into table_share_cmd(cmd,`time`) values('" + command.split(" ")[0] + "'," + str(
            int(time.time())) + ")"
        Mysql_Db_Manage.update_data(sql=sql)
    sql = "insert into " + table_share_command + "(command,`time`,description) values('" + str(command) + "'," + str(
        int(time.time())) + ",'" + str(description) + "')"
    strs = Mysql_Db_Manage.update_data(sql=sql)
    return '2'


@app.get('/getShareCmdAll')
def getShareCmdAll(cmd: str = None):
    sql = "select * from " + table_share_cmd + " order by cmd asc"
    return Mysql_Db_Manage.select_All_data(sql=sql)


@app.get('/getShareAll')
def getShareAll(cmd: str = None):
    sql = "select * from " + table_share_command + " order by time desc"
    return Mysql_Db_Manage.select_All_data(sql=sql)


@app.get('/getShareAll/cmd={cmd}')
def getShareAll(cmd: str = None):
    sql = "select * from " + table_share_command
    if cmd is not None:
        sql += " where command like '" + cmd + "%'"
    sql += " order by time desc"
    return Mysql_Db_Manage.select_All_data(sql=sql)


@app.post('/addBlack')
def addBlack(cmd: str = Body(..., embed=True)):
    if cmd is not None:
        sql = "select * from " + black_cmd + " where cmd = '" + cmd + "'"
        if Mysql_Db_Manage.is_have(sql=sql):
            return 7
        sql = "insert into " + black_cmd + "(cmd,`create_time`) values('" + str(cmd) + "'," + str(
            int(time.time())) + ")"
        result = Mysql_Db_Manage.update_data(sql=sql)
        print("添加成功，返回结果是：" + str(result))
        return '2'


@app.get('/getBlackAll')
def getAll(name: Optional[str] = False):
    sql = "select * from " + black_cmd
    if name:
        sql += " where cmd like '%" + name + "%'"

    sql += " order by create_time desc"
    return Mysql_Db_Manage.select_All_data(sql=sql)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8082,
                workers=1)
