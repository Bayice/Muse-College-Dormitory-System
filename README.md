# CSC3170-Project
咱们组的Project仓库

## 项目总览：
项目具体的要求我摘录了一部分并且翻译了在末尾，大家有空的时候看一下全部的要求，我这里只大概描述一下我们要干什么
选题我这里已经有了草案并且和几位同学商量过了

这边有个想法就是，之前思廷书院的老师找我和组里面的另一个人要做一个宿舍管理系统，刚好符合“选择一个你在现实生活中遇到的，
或者一个你感兴趣的毕业后的工作(如大学、体育协会、零售业、制造业)。
你必须对组织的运作做出一定的假设，以及底层实体、属性和关系。你应该陈述并证明这些假设是明确的，而且这些假设应该是合理和现实的。”这个要求
我觉得这样省事不少，毕竟自己熟悉

而且可以直接找书院的老师要“a reasonable amount of realistic data”

顺带书院那边还承诺有工钱，如果最后能拿到了就大家分了买雪糕吃（）

这里我想大家都差不多明白我们大概要做什么，有空可以再详细想一想项目结构
我直接或者间接认识组里所有人，所以我先自任 Group Coordinator
争取清明节假期之后早点开工


## 主要DDL：
4月15号： Group Coordinator 告知TA人员配置和summary

4月20号：公布展示

4月22号：项目必须完成

4月23/25号: 10分钟的课堂展示

5月8号 11点: 交项目报告

## 组会1纪要

1.	实体：
•	宿舍楼（Dormitory）


•	属性：楼号（Dormitory_ID），舍监


•	楼层（Floor）
•	属性：楼层号（Floor_Number）、所属宿舍楼号（Dormitory_ID），男女，楼层导师


•	房间（Room）
•	属性：房间号（Room_ID）、所属宿舍楼号（Dormitory_ID）、所属楼层号（Floor_Number）、房间类型、床位数量（Bed_Count）,房间政策方针（varchar）等


•	学生（Student）
•	属性：学号（Student_ID）、姓名、性别、年龄/级、联系方式等
•	
•	床位（Bed）
•	属性：床位号（Bed_ID）、所属房间号（Room_ID）、所属宿舍楼号（Dormitory_ID）


•	舍监：id 姓名 


•	导师：id 姓名 宿舍楼 楼层 房间号


3.	关系：

4.	
•	学生与宿舍床位的关系（Student_Bed_Assignment）
•	每个学生（Student_ID）被分配到一个宿舍的一个床位（Bed_ID）
楼层 -》 宿舍楼



Role：学生，楼层导师，舍监，管理员 


学生：未分配: 查看哪个宿舍空余  分配后：查看宿舍里面哪些人，修改政策方针


楼层导师：查看它那一层的所有信息


舍监：查看它那一栋的所有信息


管理员：查看全部信息和学生，舍监，导师的修改



网页界面：用于展示给用户的用户界面（UI）


SQL数据库：用于存储和管理数据，包括学生信息、宿舍信息、申请信息等。
后端代码： 


思廷官网（扣素材用）：https://muse.cuhk.edu.cn/


## Github仓库：
https://github.com/Bayice/CSC3170-Project

我设置成了私有仓库，你们可以有空发给我你们的github名字，我有空加进去，这样方便看进度，
不会用就直接下载，但是多人编辑我还是建议git
反正暂时编程还没开始也不着急

## Overleaf项目报告编辑模板
https://www.overleaf.com/2497779772mhncyfmctddj#f4a388

我预计应该是类似Report之类的，先开个Overleaf同步编辑，点进去注册账号就可以多人实时编辑
大家应该都会latex...吧？


## 人员任务分配（草案，只是想当然的独断专行）：
编程：3-4

课堂展示：？

网页设计：梅傲涵 + 1-2，（我略会一点html顺带也可要点书院网站的素材啥的）

项目报告:1

Group Coordinator：何绪

## ER关系细节



## 聊天白板 






## 项目内容：（机翻）
假设您是一家组织的数据库设计人员，以支持其业务操作。您必须首先选择并确定组织的确切性质。你可以选择一个你在现实生活中遇到的，或者一个你感兴趣的毕业后的工作(如大学、体育协会、零售业、制造业)。
你必须对组织的运作做出一定的假设，以及底层实体、属性和关系。
你应该陈述并证明这些假设是明确的，而且这些假设应该是合理和现实的。

你的项目必须包括以下内容。
1.  分析组织的需求
2.  识别相关的实体、属性和关系以及任何约束和属性
3.  为数据库生成E-R图
4.  将E-R图转换为关系模式(明确指示主模式)键、外键、功能和/或多值依赖项，以及证明你的设计是良好的、规范的形式)
5.  用合理数量的实际数据填充模式
6.  生成关于这些关系的示例SQL查询，用于日常实践业务及活动
7.  对分析或数据的这些关系生成示例SQL查询采矿性质(这部分是可选的，并有额外的奖励点高达5%项目总标号)
8.  建议应该为关系模式的哪些数据字段建立索引哈希德，解释一下你的决定
9.  实现上面的4到6条(可能还有7条)。一个好的网页设计将承载

额外的奖励分数高达总项目分数的5%。
额外奖励(10%积分)
鉴于大型语言模型(LLM)的迅速发展，我们鼓励您
深入研究法学硕士在数据库领域的应用。额外的好处是
采用这种方法将获得10%的奖励。

PS：
LLM模型我之前搞过相关的，可以试试，但是可以说还是小白，有大佬可以自告奋勇把我踹出去（）
