from django.test import TestCase, Client
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from .models import Post, Category

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_Ironman = User.objects.create_user(username='Ironman', password='sehyun96')
        self.user_sehyunkim = User.objects.create_user(username='sehyunkim', password='sehyun96')

        self.category_programming = Category.objects.create(name='programming', slug='programming')
        self.category_music = Category.objects.create(name='music', slug='music')

        self.post_001 = Post.objects.create(
            title='첫번째 포스트입니다.',
            content='Hello World. We are the world.',
            author=self.user_sehyunkim,
            category = self.category_programming,
        )
        self.post_002 = Post.objects.create(
            title='두번째 포스트입니다.',
            content='1등이 전부는 아니잖아요?',
            author=self.user_Ironman,
            category=self.category_music,
        )
        self.post_003 = Post.objects.create(
            title='세번째 포스트입니다.',
            content='3등이라서 감사해요',
            author=self.user_Ironman,
        )
    def category_card_test(self, soup):
        categories_card = soup.find('div', id='categories-card')
        self.assertIn('Categories', categories_card.text)
        self.assertIn(f'{self.category_programming.name} ({self.category_programming.post_set.count()})', categories_card.text)
        self.assertIn( f'{self.category_music.name} ({self.category_music.post_set.count()})', categories_card.text )
        self.assertIn( f'미분류 (1)', categories_card.text)


    def navbar_test(self, soup):
        # 1.4 내비게이션 바가 있다.
        navbar = soup.nav
        # 1.5 Blog, About me라는 문구가 내비게이션 바에 있다.
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        # 1.6 각 문구가 내비게이션 바에 있는지 확인한 후, 각 url과 연결되어 있는지 확인한다.
        # 'Do It Django' -> 대문 페이지('/')
        # 'Home'         -> 대문 페이지('/')
        # 'Blog'         -> 블로그 페이지('/blog/')
        # 'About Me'     -> about_me 페이지('/about_me')
        logo_btn = navbar.find('a', text='Do It Django')
        self.assertEqual(logo_btn.attrs['href'], '/')

        home_btn = navbar.find('a', text='Home')
        self.assertEqual(home_btn.attrs['href'], '/')

        blog_btn = navbar.find('a', text='Blog')
        self.assertEqual(blog_btn.attrs['href'], '/blog/')

        about_me_btn = navbar.find('a', text='About Me')
        self.assertEqual(about_me_btn.attrs['href'], '/about_me/')

    def test_post_list(self):
        # # 1.1 포스트 목록 페이지를 가져온다.
        # response = self.client.get('/blog/')
        # # 1.2 정상적으로 페이지가 로드된다.
        # self.assertEqual(response.status_code, 200)
        # # 1.3 페이지 타이틀은 'Blog'이다.
        # soup = BeautifulSoup(response.content, 'html.parser')
        # self.assertEqual(soup.title.text, 'Blog')
        #
        # self.navbar_test(soup)
        #
        # # 2.1 메인 영역에 게시물이 하나도 없다면
        # self.assertEqual(Post.objects.count(), 0)
        # # 2.2 '아직 게시물이 없습니다'라는 문구가 보인다.
        # main_area = soup.find('div', id='main-area')
        # self.assertIn('아직 게시물이 없습니다', main_area.text)
        #
        # # 3.1 게시물이 2개 있다면
        #
        # self.assertEqual(Post.objects.count(), 2)
        #
        # # 3.2 포스트 목록 페이지를 새로고침할 때
        # response = self.client.get('/blog/')
        # soup = BeautifulSoup(response.content, 'html.parser')
        # self.assertEqual(response.status_code, 200)
        #
        # # 3.3 메인 영역에 포스트 2개의 타이틀이 존재한다.
        # main_area = soup.find('div', id='main-area')
        # self.assertIn(post_001.title, main_area.text)
        # self.assertIn(post_002.title, main_area.text)
        #
        # # 3.4 '아직 게시물이 없습니다'라는 문구는 더 이상 보이지 않는다.
        # self.assertNotIn('아직 게시물이 없습니다', main_area.text)
        #
        # self.assertIn(self.user_sehyunkim.username.upper(), main_area.text)
        # self.assertIn(self.user_Ironman.username.upper(), main_area.text)
        ########################################################################
        # 포스트가 3개 있다면
        self.assertEqual(Post.objects.count(), 3)

        # blog 주소를 response 변수에 가져와서
        response = self.client.get('/blog/')
        # 잘 접속했는지 확인하고
        self.assertEqual(response.status_code, 200)
        # BeautifulSoup을 통해 내용을 soup에 가져와서
        soup = BeautifulSoup(response.content, 'html.parser')

        # 네비게이션 테스트를 진행하고
        self.navbar_test(soup)
        # 카테고리 카드 테스트를 진행
        self.category_card_test(soup)

        main_area = soup.find('div', id='main-area')
        self.assertNotIn('아직 게시물이 없습니다', main_area.text)

        post_001_card = main_area.find('div', id='post-1')
        self.assertIn(self.post_001.title, post_001_card.text)
        self.assertIn(self.post_001.category.name, post_001_card.text)

        post_002_card = main_area.find('div', id='post-2')
        self.assertIn(self.post_002.title, post_002_card.text)
        self.assertIn(self.post_002.category.name, post_002_card.text)

        post_003_card = main_area.find('div', id='post-3')
        self.assertIn(self.post_003.title, post_003_card.text)
        self.assertIn(self.post_003.category.name, post_003_card.text)

        self.assertIn(self.user_example_user2)
        self.assertIn(self.user_sehyunkim)
        self.assertIn(self.user_Ironman)

        # 포스트가 없는 경우
        Post.objects.all().delete()
        self.assertEqual(Post.objects.count(), 0)
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다', main_area.text)



    def test_post_detail(self):
        # 1.1 포스트가 하나 있다.
        post_001 = Post.objects.create(
            title='첫번째 포스트입니다.',
            content='Hello World. We are the world.',
        )
        # 1.2 그 포스트의 url은 '/blog/1/'이다.
        self.assertEqual(post_001.get_absolute_url(), '/blog/1/')

        # 2.  첫번째 포스트의 상세 페이지 테스트
        # 2.1 첫번째 포스트의 url로 접근하면 정상적으로 작동한다(status code: 200)
        response = self.client.get(post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        # 2.2 포스트 목록 페이지와 똑같은 내비게이션 바가 있다.
        self.navbar_test(soup)

        # 2.3 첫번째 포스트의 제목이 웹 브라우저 탭 타이틀에 들어 있다.
        self.assertIn(post_001.title, soup.title.text)

        # 2.4 첫번째 포스트의 제목이 포스트 영역에 있다.
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area')
        self.assertIn(post_001.title, post_area.text)

        # 2.5 첫번째 포스트의 작성자(author)가 포스트 영역에 있다(아직 구현 X)
        # 아직 작성 불가

        # 2.6 첫번째 포스트의 내용(content)이 포스트 영역에 있다.
        self.assertIn(post_001.content, post_area.text)

