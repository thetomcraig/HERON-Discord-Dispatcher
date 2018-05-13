#!/bin/sh

#
# a simple way to parse shell script arguments
# 
# please edit and use to your hearts content
# 


COMMAND="start"

function usage()
{
    echo "\t-h --help"
    echo "\t--command=<start,stop>"
    echo ""
}

while [ "$1" != "" ]; do
    PARAM=`echo $1 | awk -F= '{print $1}'`
    VALUE=`echo $1 | awk -F= '{print $2}'`
    case $PARAM in
        -h | --help)
            usage
            exit
            ;;
        --command)
            COMMAND=$VALUE
            ;;
        *)
            echo "ERROR: unknown parameter \"$PARAM\""
            usage
            exit 1
            ;;
    esac
    shift
done


# TODO - break this off into another sh file

KEY_1='NDEyMzAzNDM2OTk1MTAwNjgy.DWIYng._QQ4-O3teZmuO42S92bDLiYi6mg'
KEY_2='NDEyMzA2MDg1Mjk1MjkyNDE4.DWIYvg.ZmgLGCkonDoc1Nu6q-WqkcxnROw'

JOB_1_ID=''
JOB_2_ID=''
if [ $COMMAND = 'start' ]; then
  python discord_dispatcher.py $KEY_1 & 
  JOB_1_ID=$!
  echo $JOB_1_ID > job_ids.txt
  python discord_dispatcher.py $KEY_2 &
  JOB_2_ID=$!
  echo $JOB_2_ID >> job_ids.txt
fi


if [ $COMMAND = 'stop' ]; then
  kill -9 $(cat job_ids.txt)
fi
