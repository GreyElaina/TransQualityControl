# 翻译检查小工具
如你所见，打算书写一些小工具，对翻译部分进行检查。实际上 weblate 本身自带一部分质量管控，但是较为简单，主要是对标点符号，空格之类的检查。  
其次本人对 weblate 本身源代码不熟悉，在其基础上增加检测难度实在太大，而且之前 phi 尝试做转义字符检测就失败了（更别说我了XD）  
暂定检查的可能有这些，检查后尝试生成一个 md 文件（或者 html 网页？集成 travis？推送到 github page 上面？）

1. 转义字符检查：转义字符的错误可谓是非常常见，而且部分不对应或者多出会导致游戏崩溃。
2. 重名 key 检查：是的，这个问题实际上非常常见！
3. 文件位置检查：不要以为这个文件很容易，之前已经犯过很多次错了。
4. 分行错误：这个是因为脚本排序时候偶然发生的错误
5. 机器翻译自动评估：也许会用 BLEU 算法，难度较大，需要一定的算法基础（胡乱写的）。  

我添加的内容:  
1.你可以通过指定projectDir(缩写:D)来生成不同时间,不同版本的json,如:

 - python3 main.py --projectDir L:\Project-Trans
 - python3 main.py -D L:\Project-Trans
2.你可以通过指定output(缩写:O)来指定json输出到哪里,如:

 - python3 main.py --output E:
 - python3 main.py -O E: