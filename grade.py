# 创建数据　名称　grade
use grade
# 创建集合　名称　class

# 集合中插入若干个（５－８）条即可文档　文档格式
# {name:'zhangsan',age:10,sex:'m',hobby:['a','b']}
# 年龄范围　6-15
# 爱好选择：draw sing dance basketball football pingpang
# computer 每个同学选择2-5项
db.class.insert({name:'zhangsan',age:10,sex:'m',hobby:['draw','sing']})
# 4.查找练习　
# 查看班级所有学生信息
find()
# 查看班组中年龄为8岁的学生信息
find({age:8})
# 查看班组中年龄大于10岁的学生信息
find({age:{$gt:10}})
# 查看班组中年龄在8-11岁之间的学生信息
find({age:{$gte:8,$lte:11}})
# 查看班组中年龄10岁且为男生的学生信息
find({age:10,sex:'m'})
# 查看班组中小于7岁或者大于14岁的学生
find({$or:[{age:{$lt:7}},{age:{$gt:14}}]})
# 查看班组中年龄为8岁或者11岁的学生
find({age:{$in:[8,11]}})
# 找到有2项兴趣爱好的学生
find({hobby:{$size:2}})
# 找到兴趣中有draw的学生
find({hobby:draw})
# 找到即喜欢画画又喜欢跳舞的学生
find({hobby:{$all:['draw','dance']}})
# 统计兴趣有4项的学生人数
find({hobby:{$size:4}}).count()
# 找出本班年龄第二大的学生
find().sort({age:-1}).skit(1).limit(1)
# 查看本班学生兴趣爱好涵盖哪些方面　
db.class.distinct('hobby')
# 找到年龄最大的三个学生
find().sort({age:-1}).limit(3)
# 删除所有年龄大于16或者小于7岁的学生，除非他的爱好有三项以上
remove({$or:[{age:{$gt:16}},{age:{$lt:7}}],{hobby:{$size:2}}})
