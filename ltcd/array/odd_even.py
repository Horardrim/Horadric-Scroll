def odd_num(num):
    for i in range(1, num):
        if i % 2 == 0:
            yield i

def even_num(num):
    for i in range(1, num):
        if i % 2 == 1:
            yield i

def odd_or_even():
    while True:
        received = yield
        if (received % 2 == 0):
            print(f"Received: {received} is odd")
        else:
            print(f"Received: {received} is even")

# 创建生成器对象
gen = odd_or_even()

# 启动生成器
next(gen)  # 必须先调用 next() 或 send(None) 启动生成器

# 使用 send() 方法发送值
gen.send(16)
gen.send(15)
gen.close()

if __name__ == "__main__":
    for i in odd_num(11):
        print(i)

    for i in even_num(11):
        print(i)

    odd_gen = odd_num(12)
    while True:
        try:
            value = next(odd_gen)
            print(value)
        except StopIteration:
            break
        except Exception as e:
            print(f"Other exception {e.args}")
            break

    

