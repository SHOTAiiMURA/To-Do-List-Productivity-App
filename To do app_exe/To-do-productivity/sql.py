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
def create_task(conn, name, time, state, due_date:datetime.datetime, end_time:datetime.datetime, start_time:datetime.datetime, priority, line_id):
    ## might add task_id later to manage tasks by id
    with conn.cursor() as cur:
        try:
            cur.execute("insert into Task (name, duration, state, due_date, end_time, start_time, extended_time, priority, line_id) values ('{}', {}, '{}', cast('{}' as datetime ), cast('{}' as datetime ), cast('{}' as datetime ), 0, '{}', '{}');"
                        .format(name, time, state, due_date.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S'), start_time.strftime('%Y-%m-%d %H:%M:%S'), priority, line_id))

            conn.commit()
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
              "data": "Duration + Due",
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
              "data": "Duration",
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
              "data": "Start + End",
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

def delete_task(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("Delete from Task where name = %s")

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


def delete_user(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("DELETE FROM User WHERE user_id = %s")

            conn.commit()
        except Exception as e:
            raise ValueError(str(e))
        return


if __name__ == "__main__":
    print("Hello World")
    # create_task(conn, "Taro", 3600, "nb", datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), "medium", "bbbbbb")
    create_empty_task("Laundry", 24,"High","ddddd")
    #update_duration(1800)
    check_connect(conn)
    read_task(conn)
    update_duration(conn, 20)

