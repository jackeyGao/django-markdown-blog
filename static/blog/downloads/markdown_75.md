python paramiko SSH客户端模块使用


#####背景

今天在找fabric文档的时候， 找到了以前用paramiko封装的Linux下运维自动化任务的ssh工具。 其实在fabric面前， 这些代码显得非常脆弱， fabric封装的的确非常到位。
但至少没有认识fabric之前， 这段代码一直用的好好的。  
应该是拷贝网上的代码， 简单修改后就成这样了。 原文链接我忘记掉了。

自动化框架建议直接用[fabric](http://www.jackeygao.com/page/fabric%20%E5%88%9D%E6%8E%A2/)， 如果想了解请继续阅读。

样例中： 

* paramiko进行ssh连接操作目标主机
* tornado.template来生成配置文件

**code**

    :::python

	import paramiko
	from tornado import template
	import os

	#全部变量，指定配置文件的模板为当前目录下的templates文件
    template_path=os.path.join(os.path.dirname(__file__), "templates")  

    #远程执行命令
    class remote():  

        def __init__(self, server, port, username, password):
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(server, port, username, password)
    		
            self.t = paramiko.Transport((server, port))
            self.t.connect(username = username, password = password)
            self.sftp = paramiko.SFTPClient.from_transport(self.t)
    	
    	#执行命令
        def execute(self, shellcmd):   
            stdin, stdout, stderr = self.ssh.exec_command(shellcmd)
            self.ssh.close()
            return stdout.readlines()
        
        #上传文件
        def upload(self,localfile, remotefile):  
            remotepath = remotefile
            localpath = localfile
            ret = self.sftp.put(localpath, remotepath)
            self.t.close()
            return ret
        
        #下载文件
        def download(server, port, username, password, remotefile, localfile):  
            remotepath = remotefile
            localpath = localfile
            ret = self.sftp.get(remotepath, localpath)
            self.t.close()
            return ret

	#生成配置文件内容
	def genconfigstring(configtemplate, configvalues):
	    global template_path
	    loader = template.Loader(template_path)
	    ret = loader.load(configtemplate).generate(**configvalues)
	    #print ret
	    return ret
	
	def genconfigfile(configfile, configtemplate, configvalues):
	    configstring = genconfigstring(configtemplate, dianing_nginx)
	    fp_config = open(configfile, 'w')
	    fp_config.write(configstring )
	    fp_config.close()
	
	
	if __name__ == "__main__":
	    #配置项
	    dianing_nginx = {
	    'user' : 'www',
	    'group' : 'www',
	    'keepalive_timeout' : '3',
	    'access_log' : '/data1/logs/access.log',
	    'server_name' : 'www.dianying.at v.dianying.at',
	    'www_root' : '/data/dianying/wwwroot/',
	    }
	
	    config_file = "test.nginx"    #要生成的配置文件名
	    genconfigfile(config_file, "nginx.template", dianing_nginx)        #生成配置文件
	    #上传配置文件至/root/nginx/目录下
	    remote = remote('192.168.0.204', 22, 'root', 'Q0gxxxxxxq3jMTpassword')
	    print remote.execute('echo "HELLO";')
	    print remote.upload(config_file, "/root/" + config_file)
	

<hr align="left">

如果[本文](http://mdblog.sinaapp.com/page/python paramiko SSH客户端模块使用/)对你有帮助，欢迎对Jackey进行无负担小额赞助 [支付宝][alipay]

版权声明：**自由转载-非商用-非衍生-保持署名** | [Creative Commons BY-NC-ND 3.0][creativecommons]

[creativecommons]:http://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh
[alipay]:https://me.alipay.com/jackeygao