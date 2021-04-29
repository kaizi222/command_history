#!/bin/bash
function my_history(){
    if [ -f "/opt/history.log" ];then
        last_command=`tail -n 1 /opt/history.log |cut -c 21-`
    fi
    date_time="$(date "+%Y-%m-%d %T")"
    msg="######### $(history 1 | { read x cmd; echo "$cmd";})"
    if [ "${last_command}" != "${msg}" ];then
        echo "${date_time} ${msg}" >> /opt/history.log
    fi
}
function send_command(){
    command=$(history 1 | { read x cmd; echo "$cmd";})
    data='{"command":"'${command}'"}'
    curl -X POST -d "${data}" http://192.168.1.15:8082/addH >/dev/null 2>&1
}
export PROMPT_COMMAND=send_command
