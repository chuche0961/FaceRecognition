import pickle
from flask import Flask, request

def Web(dictionary_ForName, attend_students):
    all_students_ID = []
    all_students_name = []
    for key, value in dictionary_ForName.items():
        all_students_ID.append(key)
        all_students_name.append(value) 

    # attend_students = ['410878065', '410878065', '410878065']
    absent_students = []

    #簽到表
    app = Flask(__name__)
    @app.route('/', methods=['GET'])
    def display_students():
        table = '<table style="border: 1px solid black"><tr><th style="border: 1px solid black">學號</th><th style="border: 1px solid black">姓名</th><th style="border: 1px solid black">出席情况</th></tr>'
        for i, u in enumerate(all_students_ID):
            student_id = all_students_ID[i]
            student_name = all_students_name[i]

            table += '<tr><td style="border: 1px solid black">{}</td>'.format(student_id)
            table += '<td style="border: 1px solid black">{}</td>'.format(student_name)

            if u in attend_students:
                table += '<td style="border: 1px solid black">出席</td></tr>'
            else:
                table += '<td style="border: 1px solid black">缺席</td></tr>'
                absent_students.append(student_name)
        table += '</table>'
        # Create a string for displaying absent students with line breaks and increased font size
        absent_students_text = '<p>以下為缺席的學生:</p>'
        for i, student in enumerate(absent_students):
            if i % 3 == 0:
                absent_students_text += '<br>'
            absent_students_text += '<span style="font-size: 16px;">{} ,</span>'.format(student)
        # Combine the table and absent students text
        display_text = '<div style="display: flex; flex-direction: row;"><div>{}</div><div>{}</div></div>'.format(table, absent_students_text)

        # 返回签到表格到网页
        return display_text
    app.run()

