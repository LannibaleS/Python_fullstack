# 函数 ---
''''''
'''
闭包函数 --- 在内部函数饮用外部函数的变量
'''
'''
# 装饰器
    # 装饰器的作用：在不改变原来函数的调用方式的情况下，在这个函数前后添加新的功能
    # 完美的符合一个开发原则：开放封闭原则
        # 对扩展事开放的
        # 对修改是封闭的
    # 基础的装饰器
    def wrapper(func):
        def inner(*args, **kwargs):
            # 在函数被调用之前添加的代码
            ret = func(*args, **kwargs) # func是被装饰的函数，在这里被调用
            # 在函数被调用之前添加的代码
            return ret
        return inner
        
    # 完美的装饰器
    from functools import wraps
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            # 在函数被调用之前添加的代码
            ret = func(*args, **kwargs) # func是被装饰的函数，在这里被调用
            # 在函数被调用之前添加的代码
            return ret
        return inner
    
    @wrapper
    
    # 带参数的装饰器
    # @wrapper -> @wrapper(argument)
      三层嵌套
    def outer():
        def wrapper(func):
            def inner(*args, **kwargs):
                # 在函数被调用之前添加的代码
                ret = func(*args, **kwargs) # func是被装饰的函数，在这里被调用
                # 在函数被调用之前添加的代码
                return ret
            return inner
        return wrapper
    
    @outer(flag):
    def func():
        pass
        
    # 多个装饰器装饰一个函数，俄罗斯套娃
    
    
'''
