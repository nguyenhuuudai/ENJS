#biz app
# khai báo 1 cấu trúc dữ liệu, lưu trữ thông tin
posts = []

def get_posts():
    return posts

def add_post(title,content):
    # {expresstion}
    post = {'title':title, ' content':content}
    posts.append(post)