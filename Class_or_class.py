def Class_or_class():
    Python_Course = {'张三', '李四', '王五', '赵六', '钱七', '李雷', '韩梅梅'}
    C_Course = {'赵六', '李四', '麦克', '张三', '韩梅梅', '李莉', '钱七'}
    print(Python_Course, C_Course)
    print("王五的处理", Python_Course, C_Course)
    C_Course.add('王五')
    Python_Course.remove('王五')

    print("选了两门课的同学", Python_Course & C_Course)

    print("没有选C语言的同学", C_Course - Python_Course)

    print("选课的同学一共有", len(Python_Course) + len(C_Course))
