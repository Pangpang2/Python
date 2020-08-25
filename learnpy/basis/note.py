#凡是可作用于for循环的对象都是Iterable类型
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#
#深拷贝和浅拷贝是‘容器类型’的说法
#浅拷贝直接复制elem的地址， 修改可变对象，由于不会重新创建对象，所以会影响两个 [:]  list/dir/set copy.copy()
#深拷贝重新创建可变对象，所以两个完全独立 copy.deepcopy()
#
#1. 你使用过with 语句吗
# 答：with 语句一般用在对资源进行访问的场合，在代码执行中不管是否有异常发生都会执行必要的清理操作，比如文件的自动关闭

# 2.为什么with 语句能使文件正确关闭
# 答：Python 对一些内建对象进行改进，加入了对上下文管理器的支持，可以用于 with 语句中。
#     1. with 语句执行时，执行context_expr 上下文表达式（with 后语句）获取上下文管理器，
#     2. 调用上下文管理器__enter__()， 如果使用了as 语句，则将__enter__()方法的返回值赋值给as子句中的 target(s)
#     3. 执行语句体
#     4.不管是否发生异常都会执行__exit__()方法，执行清理工作。如果执行过程中没有出现异常，或者语句体中执行了语句       break/continue/return，则以 None 作为参数调用 __exit__(None, None, None) ；如果执行过程中出现异常，则使用       sys.exc_info 得到的异常信息为参数调用 __exit__(exc_type, exc_value, exc_traceback)
#     5.出现异常时，如果 __exit__(type, value, traceback) 返回 False，则会重新抛出异常，让with 之外的语句逻辑来处理异常，         这也是通用做法；如果返回 True，则忽略异常，不再对异常进行处理

# 3.函数式编程
#   函数式编程的一个特点就是，允许将函数作为一个参数传入另一个参数，也允许返回一个函数。map() reduce() sorted() filter()

# 4.赋值 浅拷贝 深拷贝
#   赋值是创建了对象的一个引用，两个引用指向同一个地址空间
#   浅拷贝 和深拷贝是容器类型的概念
#   浅拷贝 创建了一个新对象，对象中的元素使用的是原始元素的引用地址。对于不可变类型的数据，元素引用地址相同，对任何一 个对象的操作都会影响另一个对象[:] 工厂函数（list/dir/set）copy.copy()
#   深拷贝 创建一个新对象， 对象中的元素会从新生成。两个对象完全独立。

# 5.函数装饰器的作用
#   函数装饰器本质上是一个python 函数。函数的参数是 被修饰的函数，返回一个函数。可以在不改变函数的前提下增加函数的功能。装饰器，就可以抽离出大量与函数功能本身无关的   雷同代码并继续重用。

# 6.新式类和旧式类的区别， 如何确保使用的是新式类
#   为了统一类(class)和类型(type)，
#   新式类和旧式类还有一个区别就是再多继承的时候，查找要调用的方法(MRO)。新式类是广度优先的查找算法。旧式类的查找方法是深度优先的

#   1.放在模块最前面__metaclass__ = type
#   2.继承object 类
#   3.python 3 ,默认的都是新式类

# 7.__new__ 和 __init__的区别

#   __new__ 创建实例并将实例返回， __init__初始化实例，在__new__后执行。
#   __init__(self,)
#   __new__(cls, *args, **kwd):
#       return super(Person, cls).__new__(cls, *args, **kwd)

# 8.python 内存管理  http://python.jobbole.com/82061/
#   Python的GC模块主要运用了“引用计数”（reference counting）来跟踪和回收垃圾。在引用计数的基础上，还可以通过“标记-清除”（mark and       sweep）解决容器对象可能产生的循环引用的问题。通过“分代回收”（generation collection）以空间换取时间来进一步提高垃圾回收的效率

#   引用计数：每个对象都有一个引用计数  ， 创建对象时引用计数加1，，引用销毁时减1，引用计数为0 立刻被回收
#   标记-清除： 交叉引用如：a=[] b=[] a.append(b) b.append(a)
#   分代回收
# 9.Git 常见命令  checkout branch - pull -- modify- add- commit - pull - merge- push -
#   1.git checkout master
#     git pull --ff-only
#     git checkout -b v-yuetli/feature
#   2.git status
#     git add
#     git commit
#   3.git checkout master
#     git pull --ff-only
#     git checkout v-yuetli/feature
#     git merge master
#   4.git checkout v-yuetli/feature
#     git push -u origin v-yuetli/feature
#   5.pull reguest https://msasg.visualstudio.com/Bing_Ads/_git/AdsAppUI/pullrequestcreate
#   6.back to B version and remove C and D :
#     git reset B --hard
#   7.reset file to specific version
#     git log  file  (get the command id )
#     git checkout [command id] file
#     d43db74479bac28aaeac6987c9992bc9b89b05a5
# 1. enlistment code
#     cmd run
#   git clone <远程库地址>
#      执行命令的结果： 从远程库（Remote）copy 一份代码到本地仓库（Repository）, 本地会有一个master 分支

# 2. 创建自己的分支
#     git checkout -b <分支名称>
#    执行命令的结果： 从本地仓库创建一个分支

#   创建完自己的分之后， run git branch 命令查看本地分支



#    分支之间的切换可以通过命令 git  checkout  <分支名>
# 3. 修改代码
#   执行checkout  命令以后，当前的分支称为工作区（workspace）, 可以进行代码修改（注意： 修改代码不可在master 上修改）
# 4.提交代码
#   通过 git add 和git commit 命令将分支修改代码上传到本地仓库（Repository）
#   通过git push -u origin <本地分支名> , 远程库（Remote） 会产生一个与本地分支名相同的分支
# 5. 代码Review




#   pull request 相当于发起codeflow
#    我们这个项目提供了一个网址，会有“New pull request” 的按钮，点击


