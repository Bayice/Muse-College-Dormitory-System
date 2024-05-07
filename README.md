# CSC3170-Project
Project仓库

## 项目总览：
思廷书院的老师希望组内两位成员做一个宿舍管理系统，符合“选择一个你在现实生活中遇到的，或者一个你感兴趣的毕业后的工作(如大学、体育协会、零售业、制造业)。
你必须对组织的运作做出一定的假设，以及底层实体、属性和关系。你应该陈述并证明这些假设是明确的，而且这些假设应该是合理和现实的。”的项目要求，因此本组决定
将宿舍管理系统作为小组作业

## 主要Milestone：
4月15号： Group Coordinator 告知TA人员配置和summary

4月20号：公布展示

4月22号：项目必须完成

4月23号: 10分钟的课堂展示

5月8号 11点: 交项目报告

## 关系模型

1.	实体：


•	宿舍楼（Dormitory）


•	属性：楼号（Dormitory_ID），舍监


•	楼层（Floor）


•	属性：楼层号（Floor_Number）、所属宿舍楼号（Dormitory_ID），男女，楼层导师


•	房间（Room）


•	属性：房间号（Room_ID）、所属宿舍楼号（Dormitory_ID）、所属楼层号（Floor_Number）、房间类型(Floor_Type(上床下桌或者上下铺))、住宿学生（Student_Type）、床位数量（Bed_Count）,房间政策方针（varchar）等


•	学生（Student）


•	属性：学号（Student_ID）、姓名、性别、年龄/级、联系方式等


•	床位（Bed）


•	属性：床位号（Bed_ID）、所属房间号（Room_ID）、所属宿舍楼号（Dormitory_ID）


•	舍监：id 姓名 


•	导师：id 姓名 宿舍楼 楼层 房间号


Role：学生，楼层导师，舍监，管理员 

## 主要功能
学生：未分配: 查看哪个宿舍空余  分配后：查看宿舍里面哪些人，修改政策方针


楼层导师：查看它那一层的所有信息


舍监：查看它那一栋的所有信息


管理员：查看全部信息和学生，舍监，导师的修改

## 主要内容

网页界面：用于展示给用户的用户界面（UI）


SQL数据库：用于存储和管理数据，包括学生信息、宿舍信息、申请信息等。



## Github仓库：
https://github.com/Bayice/CSC3170-Project

## Overleaf项目报告
https://www.overleaf.com/2497779772mhncyfmctddj#f4a388

## 代码介绍
my-react-project文件夹：前端React部分代码


tool文件夹：生成fuzzing数据的文件夹


backsupport.py API支持


SQL文件夹：包含输入数据和建立数据库的代码


Data文件夹：测试中使用过的测试url和数据
