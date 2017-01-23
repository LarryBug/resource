#-*- coding:utf-8 -*-
from string import Template

#从标准库的string模块导入到Template类
def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

#提供一个可要选的字符串作为参数
def include_header(the_title):
    #打开模板 提供标题
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))
#页面本身存在templates/header.html中，可以根据需求改title

def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    #打开模板 读入文件 还如link种的 键 值
    for key in the_links:
        #将连接转换为字符串
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))
    #使用字符串为参数，创建html footer。页面本身存在templates/footer.html中，参数用于创建一个标记

def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')
    #将表单数据发到这个URL

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')
    #提交按钮

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')
    #单选按钮

def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)
    #把列表转换为html无序列表

def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')
    #返回h2 标题

def para(para_text):
    return('<p>' + para_text + '</p>')
