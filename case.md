# 案例学习 二&三 中所遇问题集结
## 学习中遇问题是铁律
### 自学是一个人的狂欢

老师给我们设计了三个实战案例，第一个是关于**自动化**的，基本上都是在本地操作，问题不是很大。我这篇**Markdown**文章主要汇集，我在*案例学习 二&三*中遇到的**魔术问题**。
由于*案例 二&三*中的问题真的是接二连三地往出蹦，所以把它们都汇集起来，并且放到*GitHub*上，应该是一个好想法。

有希望给后来者提供丁点帮助的意思，也有给老师分担的意思（我们那么多人，一个人有那么多问题，一个问题又有那么多细节，一个细节中又有那么多的不可控和不确定...所以老师肯定会很累）。

---

首先说*案例二*：
我们要做星座和亮星的数据抓取，老师选定的是**Wikipedia**网站的星座数据。问题是我估计有不少同学跟我一样应该进不去**Wikipedia**。怎么办？用百度吗！我倒是试了一下，可是百度的网页首先是不规范，其次是数据准确性不高，最后是抓回来的星座数据没办法跟亮星数据合并，因为百度的星座列表中的数据不全。

终于，有一天我灵光乍现，找到了[香港天文馆官网的星座列表](https://www.lcsd.gov.hk/CE/Museum/Space/zh_CN/web/spm/starshine/resources/constemyth/constellations.html)。可问题来了，香港天文馆的星座列表里缺少英文简写，因为如果没有星座英文简写的话，没办法和亮星表关联。怎么办？于是我又开始找。*只要你真心想做一件事，上帝都会赶来帮你的*。中文不行我就试着搜英文，一通乱搜，结果就真找到了[Astropixels](http://www.astropixels.com/constellations/constellationslist.html)。
这两个网站我附上超链接，里面的数据很规范，可用！
接着问题又来了哈。我从Astropixels抓回来的数据不全啊。郁闷了，怎么向前一步这么难呢？于是向老师提交了第一个issue。老师说，那是因为Astropixels的页面是iframe内嵌网页，抓回来的数据是嵌套其中的。
难怪我要的table根本就无法通过soup找到！
好吧！于是我又开始寻找解决的办法，一番折腾，学习了一下iframe网页是怎么回事，然后找到了解决办法：
```python
url = 'http://www.astropixels.com/constellations/constellationslist.html'
headers = {
    'Cookie': 'visid_incap_158103=MQ/Z6oTZR/eXFSbnAYPgWDRjrV4AAAAAQUIPAAAAAAAZol8D2Nkr/PEey1pNH+2G; nlbi_158103=/5wCOH1ZO3CTpcjgv1keDwAAAACciN3PACpa8pZ96oc6bFFY; incap_ses_575_158103=V7Xnfg1E9EIwpDGXBNH6B40msV4AAAAA80VmVmLobuM/QMfkyYaY2w==; ___utmvc=L/fcXh26SLO8d8TL6hHf2IL43Oj03+YiK4YYmTiH4bumd0R5tMLqOmuUhYlz44d8o8CWWQnnfbQ0+sRF8b2515jLBgnvMODGYmiS49B38Dqofi+c7hsLyGzOOeA8cLdimzzjNTaUFN47e3/tunQm84dd5aWxHExGh6iWrH9tXKeHo3OYB0l7+1gs+Ho6FQ39awtYsFCJn+oLyB6OagM+4e60IHOw0ZEVfDtmO0ZkYhLLFBddGCNkfK5Ze8k+mLRxQEz0Lu/9TWSPHReHIonfRSt93gYhK14he2AbzP7D+tthdMer3V8SIMmXVDegFhOE1U60/uaHyHBUZwYzzIX6op50VXEy6EC+PEKw/V0QoiYOSvH00kLAschSwTVaVgFChflfwlV0jOPzxhDZt4SfOXaik3d2/B8x69fk0bJYzoA/9q3FOUSOtIJUtdatxQ/AR0j5rl67qRHwMYLR4k8QvmXtkSd4n6TZva65I9VT6CVwEkyv5veuA2po5AKFkiFBHb4Q/un4AkPQgQZPVs9aDDZUWQKn+X78vFcJa/DpcSYTPtO60QnIJYhT6KaRwRMrAjoD8N4BBkStq/oiFu9y1tfMl911LTqwf26G10GZxKDQwjueyZ1c6dllMyrYQw3lHndLy+vKctkN/PqUXJTdYlPplMnrGkRuRMRiRtd4bD4Lue8ogPZjdOtBTvf9p/HGQ7hophLQJqh2lwUli6sl7t/XWmCF7BSFh28y6oSaTjnaz2gDRzvIaQzcT6zVNgdG/czm97twsP2md5f45C/v9T/Yv1M/UlccDWqlyPPw6bfPbhJIF07JubJzuwzMMTl4KChg0Z1tVlyQHTRtWkFKhf+vipkR2/jfoCp2qccapPQkDoXkdZ1PGweXMj+NLPpqSndTgKsnJOJxw3P8ZkHEB1B+NGVlrP8uTvQ9D08LUm2KFe9DqzoBYNcEdUOem7XxMFIW/1ELttYJWfVyQrckoqeEhq/RH8gwkmWA9eshVAyOd67qBHez8XfTkhU3TxKlYUVKhLrpvM/X92oiydYvEcvIRv9fuBHtHPbyqIdpLieoitbNO+Sg3y+shMfwSmhIh5slqcjRKFYhmCLFv+zX7pXggkWWy2qit6MkgeeCX6BG5oJ2jZlWBpAO5Vp5rRODEXH/WPnEuHeO/xi4HTmH82BrWZWT9oM7UEW+54+87rZr3ns4YBTQfR5ql5Y2yVWSg9beINMHTE7Y5guHW4tYdbL19Oza8rnMAK5gEmHgvrAv0czW95rlfq0Z0zsnPpVWhoT0ays5/+Gn1WsQ66W/dj7hs5J6ZwNTpyOpFuMU7B1u4qCQGZRi51pDvz0MnKu0GcDGx39bW409/ba65EsFi+prbbKdUowS0RQ7s7rWojy9jlVDA7KOdT+uTXM4TCn9lS3QHHIcI0WH9Kh9JVFOhijqAPmSHd24QExU2yxpdk6TpN8kS3MN1+gd0EL1l9loAEZKv01o8/izOEy8Fq4MLIcYn9AMZRdZyzU3Q6B7LjCuPHz5Bu5Tm4d+pTunMTktlRLZyLDiWHM4oN5mAq+pLIs4JJTGPoHMs7N32snSThcqtK1UWRfdBSlTW2oz0WcFje9AjnTMdIgJEMxa6wTO2dX1oLjkYJR+kkksZGlnZXN0PTExNDA4MCxzPTg0NjI5Y2E0ODk3OTY2OTQ3YTk5ODU5YmE3OTU1ZjdjNmY1YjYzN2FhNzkxYTI2M2E4OTU3ODY0N2Q3M2E5YWI3ODk1YWI5NzgzODI3MTZk',
    'Host': 'www.astropixels.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}
response = requests.get(url, headers=headers)
```
就是说在get方法中加入参数headers。
你肯定会追问这些参数从哪里来？

你打开**开发者工具**--->点击**Network**--->左边Name栏中找出你要的网页，点击之，右上出现选项Headers/Response/Preview等等，你点击Headers，里面就有你要的参数。

到这一步，我以为我这下就顺利了吗？
没有，问题又接踵而来了。当我第二天copy Cookie的时候，发现Cookie不完整，傻眼了，怎么回事？仔细一看status code，发现是304 Not Modified，什么鬼？
原来：
> 在客户端向服务端发送http请求时，若返回状态码为304 Not Modified 则表明此次请求为条件请求。在请求头中有两个请求参数：If-Modified-Since 和 If-None-Match。
> 当客户端缓存了目标资源但不确定该缓存资源是否是最新版本的时候, 就会发送一个条件请求。在进行条件请求时,客户端会提供给服务器一个If-Modified-Since请求头,其值为服务器上次返回的Last-Modified响应头的值,还会提供一个If-None-Match请求头,值为服务器上次返回的ETag响应头的值。

> 服务器会读取到这两个请求头中的值,判断客户端缓存的资源是否是最新的,如果是,服务器就会返回HTTP/304 Not Modified响应头, 但没有响应体.客户端收到304响应后,就会从本地缓存中读取对应的资源。 所以，当访问资源出现304，其实就是先在本地缓存了访问资源。

> 另一种情况是,如果服务器认为客户端缓存的资源已经过期了,那么服务器就会返回HTTP/200 OK响应,响应体就是该资源当前最新的内容.客户端收到200响应后,就会用新的响应体覆盖掉旧的缓存资源.
只有在客户端缓存了对应资源且该资源的响应头中包含了Last-Modified或ETag的情况下,才可能发送条件请求.如果这两个头都不存在,则必须无条件请求该资源,服务器也就必须返回完整的资源数据.另外，有时候我们浏览器调试的时候不希望本地缓存，设置取消缓存即可。

> 选中no cache，那么请求资源时，请求头中的Cache-Control为no-cache，表明不使用缓存，则直接获取服务器资源。另外，若没选中no cache，Cache-Control有二种情况：

> 1、max-age>0 直接从游览器缓存中提取 

> 2、max-age<=0 向服务器发送http请求时，如果该资源有修改的话返回200 ,无的话返回304. 

搜到一位无名IT大神的论述，我看完有点晕，于是我提炼总结了一下，上面就是领悟到的精髓。
解决办法就是：
选中Disable cache就行了

304的问题解决了，由于我躁动了一下，把cookie给删了，这纯属找事！怎么办？怎么显示cookie？
在解决这个问题的过程中，我知道了**跨站请求伪造**（又被称为 CSRF 或者 XSRF ）
就是一个域网站向另一个域网站发起请求的简单功能。攻击者通过一些技术手段欺骗用户使用浏览器去访问一个自己曾经认证过的网站并执行一些敏感操作（如转账）。

一个域网站向另一个域网站发起请求的方式有很多，例如点击一个超链接、加载静态资源、提交表单以及直接发起 ajax 请求等。
Same-Site Cookies 出现以前我们并没有一种简单而有效的方式去阻止 CSRF 攻击，其中一种方式是通过检查 origin 和 referer 来校验，缺点是依赖浏览器发送正确的字段，而这并不总是准确有效的；另一种方式则是通过给表单添加随机 token 的方式来校验，但是部署比较麻烦。

Same-Site Cookies 的出现就是为了解决这个问题，它可以完全有效的阻止 CSRF 攻击。

Chrome 对未设置 SameSite 的 cookie，视作 SameSite:Lax 处理

如果你的项目中有如下跨域场景：

1. 跨域的 ajax 请求；
2. 跨域嵌入的 iframe；
3. 跨域的图片资源请求；
4. 跨域的 POST FORM 表单；
如果存在这类跨域场景，且在服务端接收请求的时候，需要使用流量中的 cookie，则需要注意：这个 cookie 在设置的时候，是否明确有：
`SameSite:None; Secure` 这两个属性。如果没有的话，就会受到此策略影响。


解决办法：
1. 在 chrome 地址栏输入 `chrome://flags`
2. 在配置项中，搜索 `samesite`
3. 修改缺省设置

ok，至此我终于完成了星座数据的抓取，当然亮星的数据抓取没啥问题。

顺便这里再附上一些操作DataFrame的知识点：
DataFrame的行索引index

当DataFrame的行索引用数字标记时

```df = df[df.index % 2 == 0]```-->保留奇数行

```df = df[df.index % 2 ==1]```-->保留偶数行

当DataFrame的行索引非数字标记时

```df = df[[i % 2 == 0 for i in range(len(df.index))]]```-->保留奇数行

```df = df[[i % 2 == 1 for i in range(len(df.index))]]```-->保留偶数行

DataFrame的列索引columns

筛选奇数列或偶数列

```df = df.iloc[:, [i % 2 == 0 for i in range(len(df.columns))]]```-->保留奇数行

```df = df.iloc[:, [i % 2 == 1 for i in range(len(df.columns))]]```-->保留偶数行

按列merge：

```df = pd.concat([df_en, df_cn], axis=1)```

Drop掉不想要的列：

```df = df.drop(['no', 'area_%', 'area_rank', 'index', 'name', 'area_', 'location', 'amount'], axis=1)```

问题接着来，存入数据库的时候，我遇到了报错，原因是我在处理dataframe时设置了`df.set_index('column', inplace=True)`
```python
df = pd.read_csv('bs.csv')
df.to_sql("bs", conn, index=False)

df = pd.read_csv('mer.csv')
df.to_sql("mer", conn, index=False)
```
我猜代码有冲突，所以修改了一下，就解决了。

接下来是查星星的类源程序里的问题。因为我愣是发现不了我写的sql语句前面少了f，应该要写成这样才对`sql = f''`
还有异常处理少写了except，哎...因为脑袋短路，所以耗费了我很长时间。

如果我知道我哪儿有问题不可怕，至多郁闷一下下，找解决方法就行，可如果计算机告诉我，我有问题，而我检查5678遍，检查不出来时，这时就昏天黑地了，要么怀疑自己的智商，要么会瞬间觉得计算机在跟自己对着干哈哈哈哈...

---

说说案例三中的问题：

第一次做这个练习时，老师说要创建.gitignore文件，不知道怎么的，我没创建好，结果把很多文件都add进了暂存区域，这如何是好？于是就想着要不把repo删掉。学习了一下[怎么删除repo](https://help.github.com/en/github/administering-a-repository/deleting-a-repository)
这是GitHub官网的文章，如何删除repo。
删了之后，我就在当前工作目录下向我GitHub账户里的另一个repo提交文件，结果你懂得，错的一塌糊涂，当然，当时的我肯定不知道自己有多蠢，估计计算机也很纳闷。

**后知后觉地在笔记里写道：工作目录下init一个git仓库，如果此git仓库与GitHub上的一个远程仓库关联，那么此工作目录就与GitHub上的那个远程仓库对应起来了，以后只能从此工作目录向GitHub上的那个仓库push commit。因为此工作目录下的git仓库与GitHub上的那个远程仓库关联。**

做计算器的网页没遇到什么问题，问题又出在查星星这里。

我把存有星星数据的sqlite数据库copy到当前工作目录里的时候，发现数据库是空的，查不出来，我就想是不是要把所有的csv文件都得copy过来呢？折腾了半天，无济于事。静下心来，捋顺了一下逻辑，因为我按照老师的做法把sqlite数据库copy在了data子目录下，所以查星星的类变量db的路径要加上data子目录才行。（又是后知后觉）
测试之后成功，高兴的不要不要的。
顺便附上：怎么从其他目录copy文件到当前目录的命令

```powershell
PS C:\Users\Administrator\Code\learn-git> cp ..\stupid\fool.txt .\none\
```
当前工作目录：`learn-git`

输入命令：
```powershell
cp ..\stupid\fool.txt .\none\
```
cp是copy的意思

`cp ..\stupid\fool.txt .\none\`意思是：把上一层目录(即Code子目录)下的stupid子目录下的fool.txt文件copy到当前目录(即learn-git子目录)下的none子目录中

问题肯定有尽头，我遇到的最后一个问题是：在前后端分离做网页的过程中，我的纯前端网页无法显示，你猜问题出在哪吗？
老师的地址是`localhost:7777/static/celestial.html`
我要是写成这样就是`Error Reponse`错误。

琢磨半天之后，才知道我应该这么写`localhost:8080/static/css/celestial.html`
因为celestial.html文件在css子目录下。


OK，一路跋山涉水，坎坎坷坷，终于完成了案例实战练习。展示一下成果：

<img src="https://user-images.githubusercontent.com/49601464/81913673-de2fd880-9602-11ea-9ad1-5083e837befc.png">

<img src="https://user-images.githubusercontent.com/49601464/81913735-f273d580-9602-11ea-8621-e1871bf11bc9.png">

学习需要死磕，你会眼睁睁地看着自己发生变化，你会亲眼见证自己的愚蠢，你会体会到解决问题的喜悦。这个过程中，你有时会否定自己，有时又会自信满满，会郁闷，会不知所措，会开心，会得意...

我的心法就是：动手动手动手...遇到问题别躁动，别心生怕意，不断地试，不断地摸索，不断地重复，不断地总结,记录,积累。

如果说，我照着老师的课件顺顺利利的完成练习，我估计，我是不会知道上面列出的那些知识点的。遇到报错是好的，早遇到早解决，就算解决不了，也有了不怕的心理准备。





