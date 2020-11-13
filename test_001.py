import pytest,allure

class Test_Abc:
    #添加测试步骤
    @allure.step(title="第一个测试")
    #添加严重级别(高)
    @allure.severity(allure.severity_level.BLOCKER)
    def test_abc_001(self):
        #添加测试描述
        allure.attach("试一下","这是一个描述")
        assert 1

    #添加bug地址链接
    @allure.issue('http://www.163.com')
    #添加测试用例文件所在链接,如:
    @allure.testcase('http://www.baidu.com/test_01')
    #添加严重级别(低)
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_abc_002(self):
        # 添加测试描述
        allure.attach("试一下", "这是一个描述")
        assert 1


# if __name__ == '__main__':
#     pytest.main(['-s','-q','--alluredir', 'report', 'test_001.py'])
    #进入生成的report目录上一级目录，命令行输入allure generate report/ -o report/html --clean
    #即将json文件转换为可视报告

    #allure generate report/ -c -o report/html