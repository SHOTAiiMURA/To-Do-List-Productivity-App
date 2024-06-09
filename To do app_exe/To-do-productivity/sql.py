import datetime

import pymysql.cursors

conn = pymysql.connect(host='tododbpy.c94g44mqus56.ap-northeast-1.rds.amazonaws.com',
                    user='admin',
                    password = '1qaz2wsx',
                    db='Tododb',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)

#connection check
def check_connect(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("select * from Task;")

            for row in list(cur):
                print(row)
        except Exception as e:
            raise ValueError(str(e))

## followed by CRUD
### Create, Read, Update, Delete

## nt == new task
## ip == inprogress
## cp == complete
def create_task(conn,name, time, state, due_date:datetime.datetime, end_time:datetime.datetime, start_time:datetime.datetime, priority, line_id):
    ## might add task_id later to manage tasks by id
    with conn.cursor() as cur:
        try:
            cur.execute("insert into Task (name, duration, state, due_date, end_time, start_time, extended_time, priority, line_id) values ('{}', {}, '{}', cast('{}' as datetime ), cast('{}' as datetime ), cast('{}' as datetime ), 0, '{}', '{}');"
                        .format(name, time, state, due_date.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S'), start_time.strftime('%Y-%m-%d %H:%M:%S'), priority, line_id))

            conn.commit()

        except Exception as e:
            raise ValueError(str(e))
    return
def getMaxTaskID(conn,max_task_id):
  with conn.cursor() as cur:
    try:
      cur.execute("select task_id from Task where task_id = max(task_id)")

      max_task_id_list = list(cur)
      dict_data = max_task_id_list[0]
      max_task_id = dict_data["task_id"]
      return max_task_id

      #"task_id":12
    except Exception as e:
      raise ValueError(str(e))



def update_minutes(conn, task_id):
  with conn.cursor() as cur:
    try:
      cur.execute(f"select end_time from Task where task_id = {task_id};")

      print(list(cur))
      # dict_data = endtime_List[0]
      # end_timeid = dict_data["task_id"]
      # return end_timeid


    except Exception as e:
      raise ValueError(str(e))

    return


def create_empty_task(task_name, due_date, priority, line_id):
    create_task(conn, task_name, 0, "nt", datetime.datetime(1970, 1, 1), datetime.datetime(1970, 1, 1), datetime.datetime(1970, 1, 1),
                "", line_id)


def create_low_task(task_name, duration, line_id):
    create_task(conn, task_name, duration, "nt", datetime.datetime(1970, 1, 1), datetime.datetime(1970, 1, 1),
                datetime.datetime(1970, 1, 1),
                "low", line_id)


def create_medium_task(task_name, duration, line_id):
    create_task(conn, task_name, duration, "nt", datetime.datetime(1970, 1, 1), datetime.datetime(1970, 1, 1),
                datetime.datetime(1970, 1, 1),
                "medium", line_id)


def create_high_task(task_name, duration, line_id):
    create_task(conn, task_name, duration, "nt", datetime.datetime(1970, 1, 1), datetime.datetime(1970, 1, 1),
                datetime.datetime(1970, 1, 1),
                "high", line_id)

def insert_json_chooseDuration(user_task):
    return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": f"{user_task}",
            "weight": "bold",
            "color": "#555555",
            "align": "center",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "height": "1px",
                "backgroundColor": "#aaaaaa",
                "offsetTop": "7px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "position": "absolute",
                "width": "23%",
                "height": "3px",
                "backgroundColor": "#00c300",
                "offsetTop": "6px"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#00e600",
                    "cornerRadius": "7px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "14px",
                    "height": "14px",
                    "backgroundColor": "#00e600",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  }
                ],
                "position": "absolute",
                "width": "100%",
                "justifyContent": "space-between",
                "alignItems": "center"
              }
            ],
            "height": "14px",
            "offsetTop": "7px"
          },
          {
            "type": "separator"
          }
        ],
        "spacing": "lg"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "Choose Task Type",
            "size": "xl",
            "color": "#555555"
          }
        ],
        "spacing": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Duration",
                "size": "xs",
                "weight": "bold",
                "margin": "md",
                "color": "#FFFFFF",
                "position": "relative"
              },
              {
                "type": "text",
                "text": "+",
                "size": "xxs",
                "color": "#ffffff",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": "Due",
                "size": "xs",
                "color": "#ffffff",
                "weight": "bold"
              }
            ],
            "cornerRadius": "xxl",
            "width": "85px",
            "backgroundColor": "#00c300",
            "alignItems": "center",
            "position": "relative",
            "height": "60px",
            "margin": "none",
            "action": {
              "type": "postback",
              "label": "action",
              "data": f"{user_task}Duration + Due",
              "displayText": "Duration + Due"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Duration",
                "align": "center",
                "size": "md",
                "weight": "bold",
                "margin": "xxl",
                "position": "relative",
                "color": "#FFFFFF"
              }
            ],
            "backgroundColor": "#00c300",
            "cornerRadius": "xxl",
            "position": "relative",
            "width": "85px",
            "height": "60px",
            "alignItems": "center",
            "action": {
              "type": "postback",
              "label": "action",
              "data": f"{user_task},Duration",
              "displayText": "Duration"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Start + End",
                "align": "center",
                "size": "sm",
                "weight": "bold",
                "margin": "xxl",
                "position": "relative",
                "color": "#FFFFFF"
              }
            ],
            "backgroundColor": "#00c300",
            "cornerRadius": "xxl",
            "paddingStart": "none",
            "position": "relative",
            "width": "85px",
            "height": "60px",
            "alignItems": "center",
            "action": {
              "type": "postback",
              "label": "action",
              "data": f"{user_task},Start + End",
              "displayText": "Start + End"
            }
          }
        ]
      }
    ],
    "spacing": "xxl"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [],
    "justifyContent": "center",
    "alignItems": "center",
    "paddingTop": "4px"
  }
}
def insert_hour_duration(name):
  return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Hour : Minutes",
            "weight": "bold",
            "color": "#555555",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "height": "1px",
                "backgroundColor": "#aaaaaa",
                "offsetTop": "7px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "backgroundColor": "#00c300",
                "height": "3px",
                "width": "41%",
                "position": "absolute",
                "offsetTop": "6px"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#00c300",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#00c300",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "14px",
                    "height": "14px",
                    "backgroundColor": "#00e600",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "7px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  }
                ],
                "position": "absolute",
                "width": "100%",
                "justifyContent": "space-between",
                "alignItems": "center"
              }
            ],
            "height": "14px"
          }
        ],
        "spacing": "lg"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Choose Duration [Hour]",
            "size": "xl",
            "color": "#555555",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "0 hour",
                "color": "#ffffff",
                "weight": "bold",
                "size": "lg",
                "align": "center"
              }
            ],
            "width": "240px",
            "height": "44px",
            "cornerRadius": "xxl",
            "paddingTop": "md",
            "backgroundColor": "#08C656",
            "action": {
              "type": "postback",
              "label": "action",
              "data": f"{name},0 hour",
              "displayText": "0 hour"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "1 hour",
                "align": "center",
                "margin": "none",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold"
              }
            ],
            "backgroundColor": "#08C656",
            "cornerRadius": "xxl",
            "paddingTop": "md",
            "width": "240px",
            "height": "44px",
            "action": {
              "type": "postback",
              "label": "action",
              "data": f"{name},1 hour",
              "displayText": "1 hour"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "2 hour",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold",
                "align": "center"
              }
            ],
            "backgroundColor": "#08C656",
            "paddingTop": "md",
            "cornerRadius": "xxl",
            "width": "240px",
            "height": "44px",
            "action": {
              "type": "postback",
              "label": "action",
              "data": f"{name},2 hour",
              "displayText": "2 hour"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "3 hour",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold",
                "align": "center"
              }
            ],
            "backgroundColor": "#08C656",
            "cornerRadius": "xxl",
            "paddingTop": "md",
            "width": "240px",
            "height": "44px",
            "action": {
              "type": "postback",
              "label": "action",
              "data": f"{name},3 hour",
              "displayText": "3 hour"
            }
          }
        ],
        "spacing": "md"
      }
    ],
    "spacing": "xl"
  }
}
def hour_duration_postback(postback_data, task_id):
    if postback_data[-5:] == ' hour':
        duration_hour = postback_data.replace(" hour","")

def choose_duration(name, hour_duration):
    return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": f"{hour_duration}"" : Minute",
            "weight": "bold",
            "color": "#555555",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "height": "1px",
                "backgroundColor": "#aaaaaa",
                "offsetTop": "7px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "backgroundColor": "#00c300",
                "height": "3px",
                "width": "41%",
                "position": "absolute",
                "offsetTop": "6px"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#08C656",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#08C656",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "14px",
                    "height": "14px",
                    "backgroundColor": "#08C656",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "7px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  }
                ],
                "position": "absolute",
                "width": "100%",
                "justifyContent": "space-between",
                "alignItems": "center"
              }
            ],
            "height": "14px"
          }
        ],
        "spacing": "lg"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Choose Duration [Minute]",
            "size": "xl",
            "color": "#555555",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "0 mins",
                "color": "#ffffff",
                "weight": "bold",
                "size": "lg",
                "align": "center"
              }
            ],
            "width": "240px",
            "height": "44px",
            "cornerRadius": "xxl",
            "paddingTop": "md",
            "backgroundColor": "#08C656",
            "action": {
              "type": "postback",
              "label": "action",
              "data": f"{name},{hour_duration},0 mins",
              "displayText": "0 minutes"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "15 mins",
                "align": "center",
                "margin": "none",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold"
              }
            ],
            "backgroundColor": "#08C656",
            "cornerRadius": "xxl",
            "paddingTop": "md",
            "width": "240px",
            "height": "44px",
            "action": {
              "type": "postback",
              "label": "action",
              "data": f"{name},{hour_duration},15 mins",
              "displayText": "15 minutes"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "25 mins",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold",
                "align": "center"
              }
            ],
            "backgroundColor": "#08C656",
            "paddingTop": "md",
            "cornerRadius": "xxl",
            "width": "240px",
            "height": "44px",
            "action": {
              "type": "postback",
              "label": "action",
              "data": f"{name},{hour_duration},25 mins",
              "displayText": "25 minutes"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "45 mins",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold",
                "align": "center"
              }
            ],
            "backgroundColor": "#08C656",
            "cornerRadius": "xxl",
            "paddingTop": "md",
            "width": "240px",
            "height": "44px",
            "action": {
              "type": "postback",
              "label": "action",
              "data": f"{name},{hour_duration},45 mins",
              "displayText": "45 minutes"
            }
          }
        ],
        "spacing": "md"
      }
    ],
    "spacing": "xl"
  }
}


def minutes_duration_postback(postback_data, task_id):
  if postback_data[-5:] == ' mins':
    duration_hour = postback_data.replace(" mins", "")
def choose_priority(user_task,hour_duration,mins_duration):
  return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": f"{user_task}" "["f"{hour_duration}"":"f"{mins_duration}""]",
            "weight": "bold",
            "color": "#555555",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "height": "1px",
                "backgroundColor": "#aaaaaa",
                "offsetTop": "7px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "backgroundColor": "#00c300",
                "height": "3px",
                "width": "60%",
                "position": "absolute",
                "offsetTop": "6px"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#08C656",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#08C656",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#08C656",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "14px",
                    "height": "14px",
                    "backgroundColor": "#08C656",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "7px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  }
                ],
                "position": "absolute",
                "width": "100%",
                "justifyContent": "space-between",
                "alignItems": "center"
              }
            ],
            "height": "14px"
          }
        ],
        "spacing": "lg"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Choose Priority",
            "size": "xl",
            "color": "#555555",
            "wrap": True
          }
        ],
        "spacing": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "High",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "backgroundColor": "#FF5733",
            "cornerRadius": "xxl",
            "action": {
              "type": "postback",
              "label": "choose priority",
              "data": f"high",
              "displayText": "High Priority"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Medium",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "backgroundColor": "#33A9FF",
            "cornerRadius": "xxl",
            "action": {
              "type": "postback",
              "label": "Choose priority",
              "data": "medium",
              "displayText": "Medium Priority"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Low",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "backgroundColor": "#3AFF33",
            "cornerRadius": "xxl",
            "action": {
              "type": "postback",
              "label": "choose priority",
              "data": "low",
              "displayText": "Low Priority"
            }
          }
        ]
      }
    ],
    "spacing": "xl"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [],
    "justifyContent": "center",
    "alignItems": "center",
    "paddingTop": "4px"
  }
}

# def priority_postback(postback_data, task_id):
#   if postback_data == 'high':
#   elif postback_data == 'medium':
#   elif postback_data == 'low':

## 1. task_name
## 2. duration
## 3. due_date
## 4. priority

#use for view task
def read_task(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("select name from Task")
            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
    return

## view in progress task
def read_taskListIP(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("select name from Task where state = 'ip'")
            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
    return


## view select upcoming task
def read_taskListUpComing(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("select name from Task where state ='nt' order by end_time asc")
            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
    return

## view completed task
def read_taskListCP(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("select name from Task where state = 'cp'")
            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
    return

## view high priority task
def read_highPritask(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("select name from Task where priority = 'high' order by end_time asc")
            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
    return

## view medium priority task
def read_medPritask(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("select name from Task where priority = 'medium' order by end_time asc")
            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
    return


## view low priority task
def read_lowPritask(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("select name from Task where priority = 'low' order by end_time asc")
            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
    return


## update product set price=340 where name='Grape';
## situation where user
##task_idが特定の値（ここでも%sがプレースホルダー）と一致する行のみを更新対象とします。
def update_duration(conn,extended_time):
    with conn.cursor() as cur:
        try:
            cur.execute("update Task set extended_time = IFNULL(extended_time, 0) + %s,end_time = DATE_ADD(end_time, INTERVAL %s MINUTE) where task_id = %s")

            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
        return
## Year, Month, Date, Hour, Minute
def update_due_date(conn,task_id, year, month, day, hours, minutes, seconds):
    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE Task SET due_date = %s WHERE task_id = %s")

            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
        return

## datetime(year, 0, 0)
## def update_year(conn):
##    return

## datetime(5, 0, 0)
## 1. select
## 2. datetime(year, month, 0)
def update_month(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE Task SET due_date = DATE_ADD(due_date, INTERVAL %s MONTH),start_time = DATE_ADD(start_time, INTERVAL %s MONTH),end_time = DATE_ADD(end_time, INTERVAL %s MONTH) WHERE task_id = %s")

            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
        return

def update_priority(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("SET @priority = %s; UPDATE Task SET priority = @priority WHERE task_id = %s;")

            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
        return

def update_status(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE Task SET state = %s WHERE task_id = %s")

            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
        return

def delete_task(conn,name):
    with conn.cursor() as cur:
        try:
            cur.execute(f"Delete from Task where name = {name}")

            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
        return


## def create_user(conn):
def read_check_user(conn, user_id):
    ## check if user_id is in User table
    user_data_list = []
    with conn.cursor() as cur:
        try:
            cur.execute(f"select user_id from User;")

            user_data_list = list(cur)

        except Exception as e:
            raise ValueError(str(e))

    user_list = []
    for user_data in user_data_list:
        user_list.append(user_data["user_id"])

    if user_id not in user_list:

        with conn.cursor() as cur:
            try:
                sql = f"insert into User values('{user_id}','');"
                print("[Inserting... ->]" + sql)
                cur.execute(sql)

                conn.commit()
            except Exception as e:
                raise ValueError(str(e))
        return


def delete_user(conn,user_id):
    with conn.cursor() as cur:
        try:
            cur.execute(f"DELETE FROM User WHERE user_id = {user_id}")

            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
        return


if __name__ == "__main__":
    print("Hello World")
    # create_task(conn, "Taro", 3600, "nb", datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), "medium", "bbbbbb")
    create_empty_task(12, 24,"high","ddddd")
    #update_duration(1800)
    check_connect(conn)
    read_task(conn)
    #update_duration(conn, 20)
    update_minutes(conn, 12)
    getMaxTaskID(conn, 12)

